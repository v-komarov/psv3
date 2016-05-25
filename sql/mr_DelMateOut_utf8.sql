CREATE OR REPLACE FUNCTION mr_DelMateOut(varchar(24)) RETURNS text

AS $BODY$

--- Удаление записи расхода материала ---


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

--- Идентификатор заявки ---
task_kod varchar(24);

--- Переменные строк ---
row_data mr_mate_out_party%ROWTYPE;

--- Статус заявки ---
status_now int2;

--- Промежуточная переменная для хранения остаток по партиям ---
q_tmp numeric(10,2);

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
SELECT INTO task_kod,mate_kod,eds_kod,store_kod mr_task_kod,mr_mate_kod,mr_eds_kod,mr_store_kod FROM mr_mate_out WHERE mr_rec_id=rec_kod;

--- Если заявка закрыта уже месяц - то изменение запрещено ---
SELECT INTO status_now sc_status_task FROM sc_task WHERE sc_rec_id=task_kod;
SELECT INTO n date_part('day',(now()-sc_date_task_close)) FROM sc_task WHERE sc_rec_id=task_kod;
IF n>30 AND status_now=1 THEN
	RETURN 'NOTACCESS';
END IF;


--- Определение владельца ---
SELECT INTO store_own mr_store_man_login FROM mr_store_list WHERE mr_rec_id=store_kod;


--- Поступление на склад только владельцу ---
IF store_own!=current_user THEN
	RETURN 'NOTACCESS';
END IF;





--- "Удаление" записи из таблици расхода ---
UPDATE mr_mate_out
SET
mr_rec_delete='delete',
mr_update_time=current_timestamp,
mr_update_author=current_user
WHERE
mr_rec_id=rec_kod;


--- Возврат товара на склад по партиям ---
FOR row_data IN SELECT * FROM mr_mate_out_party WHERE mr_rec_delete='' AND mr_out_kod=rec_kod LOOP
	--- Остаток по партии ---
	SELECT INTO q_tmp mr_mate_q FROM mr_mate_in_party WHERE mr_party_kod=row_data.mr_party_kod;
	--- Возврат ---
	UPDATE mr_mate_in_party
	SET 
	mr_mate_q=(q_tmp+row_data.mr_mate_q),
	mr_update_time=current_timestamp,
	mr_update_author=current_user
	WHERE
	mr_party_kod=row_data.mr_party_kod;
END LOOP;



--- "Удаление" записи из таблицы расхода партий ---
UPDATE mr_mate_out_party
SET
mr_rec_delete='delete',
mr_update_time=current_timestamp,
mr_update_author=current_user
WHERE
mr_out_kod=rec_kod;




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
genk,
5,
rec_kod,
mate_kod,
eds_kod,
sum_q,
store_kod);




RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql';



