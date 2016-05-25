CREATE OR REPLACE FUNCTION mr_DelMateIn(varchar(24)) RETURNS text

AS $BODY$

--- Удаление записи поступления материала ---


DECLARE

---- Переменные -----

-- Код записи --
rec_kod ALIAS FOR $1;

--- Владелец склада ---
store_own varchar(50);

--- Код материала ---
mate_kod int;

--- Код склада ---
store_kod int;

--- Код единиц измерения ---
eds_kod varchar(3);

--- Суммарный остаток материала ---
sum_q numeric(10,2);

--- Вспомогательная переменная ----
n int;

--- Сгенерированный ключ ---
genk varchar(24);





BEGIN 


--- Проверка поступивших данных ---
IF length(rec_kod)=0 THEN
	RETURN 'ERRORDATA';
END IF;


--- Определение кода склада,метериала,ед. измерения ---
SELECT INTO mate_kod,eds_kod,store_kod mr_mate_kod,mr_eds_kod,mr_store_kod FROM mr_mate_in WHERE mr_rec_id=rec_kod;


--- Определение владельца ---
SELECT INTO store_own mr_store_man_login FROM mr_store_list WHERE mr_rec_id=store_kod;


--- Поступление на склад только владельцу ---
IF store_own!=current_user THEN
	RETURN 'NOTACCESS';
END IF;


--- Определение : был ли уже расход по этой партии ---
SELECT INTO n count(*) FROM mr_mate_out_party WHERE mr_rec_delete='' AND mr_party_kod=rec_kod;
IF n!=0 THEN
	RETURN 'NOTACCESS';
END IF;


--- "Удаление" записи из таблици поступлений ---
UPDATE mr_mate_in
SET
mr_rec_delete='delete',
mr_update_time=current_timestamp,
mr_update_author=current_user
WHERE
mr_rec_id=rec_kod;


--- "Удаление" записи из таблицы поступлений партий ---
UPDATE mr_mate_in_party
SET
mr_rec_delete='delete',
mr_update_time=current_timestamp,
mr_update_author=current_user
WHERE
mr_party_kod=rec_kod;




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
	genk:=ps_GenKey24();
	SELECT INTO n count(*) FROM mr_story_q WHERE mr_rec_id=genk;
END LOOP;


--- Расчёт суммарного остатка по этому материалу ---
SELECT INTO n count(*) FROM mr_mate_in_party WHERE mr_mate_kod=mate_kod AND mr_store_kod=store_kod AND mr_rec_delete='';
IF n!=0 THEN
	SELECT INTO sum_q sum(mr_mate_q) FROM mr_mate_in_party WHERE mr_mate_kod=mate_kod AND mr_store_kod=store_kod AND mr_rec_delete='';
ELSE
	sum_q := 0;
END IF;


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
genk,
3,
rec_kod,
mate_kod,
eds_kod,
sum_q,
store_kod);




RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql';



