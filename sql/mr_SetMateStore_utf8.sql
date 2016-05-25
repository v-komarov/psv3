CREATE OR REPLACE FUNCTION mr_SetMateStore(int,varchar(100),numeric(10,2),numeric(10,2)) RETURNS text

AS $BODY$

--- Ввод остатков материала ---


DECLARE

---- Переменные -----

-- Код материала --
mate_kod ALIAS FOR $1;

--- Название склада ---
store_name ALIAS FOR $2;

--- Значение количества ---
mate_q ALIAS FOR $3;

--- Значение цены ---
mate_cost ALIAS FOR $4;

--- Владелец склада ---
store_own varchar(50);

--- Код склада ---
store_kod int;

--- Код единиц измерения ---
eds_kod varchar(3);

--- Суммарный остаток материала ---
sum_q numeric(10,2);

--- Вспомогательная переменная ----
n int;

--- Идентификатор строки ---
genk varchar(24);

--- Идентификатор строки ---
genk2 varchar(24);

--- Идентификатор строки ---
genk3 varchar(24);






BEGIN 


--- Проверка поступивших данных ---
IF mate_kod IS NULL OR length(store_name)=0 OR mate_cost IS NULL OR mate_cost<=0.00 OR mate_q IS NULL OR mate_q<=0.00 THEN
	RETURN 'ERRORDATA';
END IF;


--- Определение кода склада и владельца ---
SELECT INTO store_kod,store_own mr_rec_id,mr_store_man_login FROM mr_store_list WHERE btrim(mr_store_name)=btrim(store_name);


--- Поступление на склад только владельцу ---
IF store_own!=current_user THEN
	RETURN 'NOTACCESS';
END IF;


--- Определение кода единицы измерения ---
SELECT INTO eds_kod mr_eds_kod FROM mr_mate_list WHERE mr_rec_id=mate_kod;



--- Добавление записи в таблицу ввода остатков ---
--- Определение идентификатора строки ---
--- Первоначально такой ключ существует ---
n:=1;
--- Получение уникального ключа ---
WHILE n<>0 LOOP
	genk:=ps_GenKey24();
	SELECT INTO n count(*) FROM mr_mate_set_store WHERE mr_rec_id=genk;
END LOOP;


--- Добавление записи в таблицу остатков ---
INSERT INTO mr_mate_set_store(
mr_rec_id,
mr_mate_kod,
mr_eds_kod,
mr_mate_cost,
mr_mate_q,
mr_store_kod) 
VALUES(
genk,
mate_kod,
eds_kod,
mate_cost,
mate_q,
store_kod);


--- "Удаление" предыдущих остатков по данному материалу из таблицы партий ---
UPDATE mr_mate_in_party
SET
mr_rec_delete='delete',
mr_update_time=current_timestamp,
mr_update_author=current_user
WHERE
mr_mate_kod=mate_kod;


--- Добавление записи в таблицу партий ---
--- Определение идентификатора строки ---
--- Первоначально такой ключ существует ---
n:=1;
--- Получение уникального ключа ---
WHILE n<>0 LOOP
	genk2:=ps_GenKey24();
	SELECT INTO n count(*) FROM mr_mate_in_party WHERE mr_rec_id=genk2;
END LOOP;


--- Добавление записи ---
INSERT INTO mr_mate_in_party(
mr_rec_id,
mr_party_kod,
mr_mate_kod,
mr_eds_kod,
mr_mate_cost,
mr_mate_q,
mr_store_kod) 
VALUES(
genk2,
genk,
mate_kod,
eds_kod,
mate_cost,
mate_q,
store_kod);




--- Добавление записи в таблицу истории операций ---
--- Коды :
--- 1 - Ввод остатка
--- 2 - Поступление на склад
--- 3 - Удаление поступления на склад
--- 4 - Расход со склада
--- 5 - Удаление расхода со склада
--- Определение идентификатора строки ---
--- Первоначально такой ключ существует ---
n:=1;
--- Получение уникального ключа ---
WHILE n<>0 LOOP
	genk3:=ps_GenKey24();
	SELECT INTO n count(*) FROM mr_story_q WHERE mr_rec_id=genk3;
END LOOP;


--- Расчёт суммарного остатка по этому материалу ---
SELECT INTO sum_q sum(mr_mate_q) FROM mr_mate_in_party WHERE mr_mate_kod=mate_kod AND mr_store_kod=store_kod AND mr_rec_delete='';

--- Добавление записи ---
INSERT INTO mr_story_q(
mr_rec_id,
mr_operation_kod,
mr_master_kod,
mr_mate_kod,
mr_eds_kod,
mr_mate_q,
mr_store_kod) 
VALUES(
genk3,
1,
genk,
mate_kod,
eds_kod,
sum_q,
store_kod);




RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql';



