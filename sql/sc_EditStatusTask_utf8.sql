CREATE FUNCTION sc_EditStatusTask(varchar(24), varchar(30)) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

-- Код заявки (код строки) --
kod_ ALIAS FOR $1;


-- Название статуса --
status_ ALIAS FOR $2;


-- Код статуса ---
status_kod int2;



BEGIN 


--- Поиск кода статуса по названию ---
SELECT INTO status_kod sc_rec_id FROM sc_status WHERE btrim(sc_status)=btrim(status_);


--- Если заявка закрывается ---
IF status_kod=1 THEN
UPDATE sc_list SET sc_date_close=current_timestamp WHERE sc_rec_id=kod_;
END IF;


--- Собственно изменение статуса ---
UPDATE sc_list SET sc_status=status_kod WHERE sc_rec_id=kod_;


RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql'



