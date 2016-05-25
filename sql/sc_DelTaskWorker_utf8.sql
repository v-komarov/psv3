CREATE OR REPLACE FUNCTION sc_DelTaskWorker(varchar(24),varchar(24)) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

--- Код заявки --
kod_task ALIAS FOR $1;

--- Код записи ---
kod_rec ALIAS FOR $2;

--- Код статуса, который сейчас ---
status_now int2;

--- Вспомогательная переменная ---
n int2;




BEGIN 


--- Проверка поступивших данных на корректность ---
IF length(kod_task)=0 OR length(kod_rec)=0 THEN
	RETURN 'ERRORDATA';
END IF;


--- Определение кода статуса который сейчас ---
SELECT INTO status_now sc_status_task FROM sc_task WHERE sc_rec_id=kod_task;


--- Если заявка закрыта уже месяц - то изменение запрещено ---
SELECT INTO n date_part('day',(now()-sc_date_task_close)) FROM sc_task WHERE sc_rec_id=kod_task;
IF n>30 AND status_now=1 THEN
	RETURN 'NOTACCESS';
END IF;



UPDATE sc_worker SET
sc_rec_delete='delete',
sc_update_time=now(),
sc_update_author=current_user
WHERE sc_rec_id=kod_rec
;
	



RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql';



