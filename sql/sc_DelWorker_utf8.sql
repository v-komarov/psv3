CREATE OR REPLACE FUNCTION sc_DelWorker(varchar(24)) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

-- Код записи ---
kod_rec ALIAS FOR $1;




BEGIN 


--- Проверка поступивших данных на корректность ---
IF length(kod_rec)=0 THEN
	RETURN 'ERRORDATA';
END IF;





-- измнение записи ---
UPDATE sc_worker_list
SET
sc_rec_delete='delete',
sc_update_time=now(),
sc_update_author=current_user
WHERE
sc_rec_id=kod_rec
;


RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql'






