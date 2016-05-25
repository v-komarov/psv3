CREATE OR REPLACE FUNCTION mr_AddMateOut(text,int,int,numeric(10,2),varchar(24)) RETURNS text

AS $BODY$

--- Расход материала ---


DECLARE

---- Переменные -----

-- Код выбранной строки --
row_kod ALIAS FOR $1;

--- Код материала ---
mate_kod ALIAS FOR $2;

--- Код склада ---
store_kod ALIAS FOR $3;

--- Значение количества ---
q ALIAS FOR $4;

--- Идентификатор заявки ---
task_kod ALIAS FOR $5;

--- Значение отпускной цены ---
mate_cost numeric(10,2);

--- Владелец склада ---
store_own varchar(50);

--- Код единиц измерения ---
eds_kod varchar(3);

--- Суммарный остаток материала ---
sum_q numeric(10,2);

--- Остаток материала для операций по партиям ---
q_tmp numeric(10,2);

--- Расход по партии ---
q_party numeric(10,2);

--- Переменные строк ---
row_data mr_mate_in_party%ROWTYPE;

--- Статус заявки ---
status_now int2;


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
IF store_kod IS NULL OR length(row_kod)=0 OR mate_kod IS NULL OR q IS NULL OR q<=0.00 THEN
	RETURN 'ERRORDATA';
END IF;


--- Если заявка закрыта уже месяц - то изменение запрещено ---
SELECT INTO status_now sc_status_task FROM sc_task WHERE sc_rec_id=task_kod;
SELECT INTO n date_part('day',(now()-sc_date_task_close)) FROM sc_task WHERE sc_rec_id=task_kod;
IF n>30 AND status_now=1 THEN
	RETURN 'NOTACCESS';
END IF;


--- Определение владельца ---
SELECT INTO store_own mr_store_man_login FROM mr_store_list WHERE mr_rec_id=store_kod;


--- Отпуск со склада только владельцу ---
IF store_own!=current_user THEN
	RETURN 'NOTACCESS';
END IF;


--- Определение кода единицы измерения ---
SELECT INTO eds_kod mr_eds_kod FROM mr_mate_list WHERE mr_rec_id=mate_kod;


--- Определение отпускной цены ---
SELECT INTO mate_cost sc.mate_cost FROM sc_show_mate_store sc WHERE rec_id=row_kod;

--- Проверка  превышения количества остатков на складе ---
SELECT INTO sum_q mate_q FROM sc_show_mate_store WHERE rec_id=row_kod;
IF q>sum_q THEN
	RETURN 'NOTACCESS';
END IF;




--- Добавление записи в таблицу расхода ---
--- Определение идентификатора строки ---
--- Первоначально такой ключ существует ---
n:=1;
--- Получение уникального ключа ---
WHILE n<>0 LOOP
	genk:=ps_GenKey24();
	SELECT INTO n count(*) FROM mr_mate_out WHERE mr_rec_id=genk;
END LOOP;


--- Добавление записи ---
INSERT INTO mr_mate_out(
mr_rec_id,
mr_task_kod,
mr_mate_kod,
mr_eds_kod,
mr_abonent_cost,
mr_mate_q,
mr_store_kod) 
VALUES(
genk,
task_kod,
mate_kod,
eds_kod,
mate_cost,
q,
store_kod);

--- Остаток для операций ---
q_tmp := q;

--- Добавление записи в таблицу расхода партий, фиксирование остатков по партиям ---
FOR row_data IN SELECT * FROM mr_mate_in_party WHERE mr_mate_kod=mate_kod AND mr_store_kod=store_kod AND mr_mate_q!=0.00 AND mr_rec_delete='' ORDER BY mr_create_time LOOP

	IF q_tmp!=0.00 THEN

		---- В зависимости от вариантов остатка ---
		IF q_tmp=row_data.mr_mate_q THEN

			UPDATE mr_mate_in_party
			SET 
			mr_mate_q=0.00,
			mr_update_time=current_timestamp,
			mr_update_author=current_user
			WHERE
			mr_rec_id=row_data.mr_rec_id;
			q_party := q_tmp;
			q_tmp := 0.00;

		ELSIF q_tmp<row_data.mr_mate_q THEN

			UPDATE mr_mate_in_party
			SET 
			mr_mate_q=(row_data.mr_mate_q-q_tmp),
			mr_update_time=current_timestamp,
			mr_update_author=current_user
			WHERE
			mr_rec_id=row_data.mr_rec_id;
			q_party := q_tmp;
			q_tmp := 0.00;
	
		ELSE
			UPDATE mr_mate_in_party
			SET 
			mr_mate_q=0.00,
			mr_update_time=current_timestamp,
			mr_update_author=current_user
			WHERE
			mr_rec_id=row_data.mr_rec_id;
			q_tmp := q_tmp - row_data.mr_mate_q;
			q_party := row_data.mr_mate_q;


		END IF;


		--- Определение идентификатора строки ---
		--- Первоначально такой ключ существует ---
		n:=1;
		--- Получение уникального ключа ---
		WHILE n<>0 LOOP
			genk2:=ps_GenKey24();
			SELECT INTO n count(*) FROM mr_mate_out_party WHERE mr_rec_id=genk2;
		END LOOP;

		--- Добавление записи ---
		INSERT INTO mr_mate_out_party(
		mr_rec_id,
		mr_party_kod,
		mr_out_kod,
		mr_mate_kod,
		mr_eds_kod,
		mr_abonent_cost,
		mr_mate_q,
		mr_store_kod) 
		VALUES(
		genk2,
		row_data.mr_party_kod,
		genk,
		mate_kod,
		eds_kod,
		mate_cost,
		q_party,
		store_kod);




	END IF;

END LOOP;







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
4,
genk,
mate_kod,
eds_kod,
sum_q,
store_kod);




RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql';



