CREATE OR REPLACE FUNCTION sc_EditTask(varchar(24), timestamp, varchar(30), int, varchar(50), varchar(3), varchar(100), numeric(10,2), int, numeric(10,2), text) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

--- Код записи --
kod_task ALIAS FOR $1;

--- Дата и время заявки ---
datetime_task ALIAS FOR $2;

--- Статус заявки ---
status_task ALIAS FOR $3;

--- Тип заявки ---
type_task ALIAS FOR $4;

--- название заявки ---
name_task ALIAS FOR $5;

--- Подъезд ---
p_task ALIAS FOR $6;

--- Телефон ---
phone_task ALIAS FOR $7;

--- План человеко-часы ---
plan_chch ALIAS FOR $8;

--- План количество исполнителей ---
plan_workers ALIAS FOR $9;

--- Факт человеко-часы ---
fact_chch ALIAS FOR $10;

--- Примечание ---
note_task ALIAS FOR $11;

--- Код статуса, который сейчас ---
status_now int2;

--- Код статуса, который устанавливается ---
status_kod int2;

--- Флаг удаления заявки ---
delete_flag varchar(6);

--- Вспомогательная переменная ---
n int2;


BEGIN 


--- Проверка поступивших данных на корректность ---
IF length(kod_task)=0 OR length(name_task)=0 OR type_task=0 OR length(status_task)=0 OR plan_chch<=0 OR plan_workers<=0 THEN
	RETURN 'ERRORDATA';
END IF;


--- Определение кода статуса который сейчас ---
SELECT INTO status_now sc_status_task FROM sc_task WHERE sc_rec_id=kod_task;

--- Определение кода статуса, который устанавливается ---
SELECT INTO status_kod sc_rec_id FROM sc_status WHERE btrim(sc_status)=btrim(status_task);

--- Определение удаления заявки ---
SELECT INTO delete_flag sc_rec_delete FROM sc_task WHERE sc_rec_id=kod_task;


--- Если заявка закрыта - то изменение запрещено ---
IF status_now=1 THEN
	RETURN 'NOTACCESS';
END IF;


--- Если заявка удалена, - то изменение запрещено ---
IF delete_flag!='' THEN
	RETURN 'NOTACCESS';
END IF;


--- Если закрываем ---
IF status_kod=1 THEN
	--- Дополнительная проверка данных ---
	IF fact_chch<=0 THEN
		RETURN 'ERRORDATA';
	END IF;
	UPDATE sc_task SET sc_date_task_close=now() WHERE sc_rec_id=kod_task;
END IF;



--- Если вновь открываем ---
IF status_now!=0 AND status_kod=0 THEN
	UPDATE sc_task SET sc_date_task_open=now() WHERE sc_rec_id=kod_task;
END IF;


--- Изменение записи ---
UPDATE sc_task SET
sc_plan_time=datetime_task,
sc_text_task=ps_RusUpper(btrim(name_task)),
sc_status_task=status_kod,
sc_type_task=type_task,
sc_p=btrim(p_task),
sc_phone=btrim(phone_task),
sc_plan_chch=plan_chch,
sc_plan_workers=plan_workers,
sc_fact_chch=fact_chch,
sc_task_note=note_task,
sc_update_time=now(),
sc_update_author=current_user
WHERE sc_rec_id=kod_task
;




RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql'



