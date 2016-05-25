CREATE FUNCTION sc_DelSerFromWorker(varchar(24)) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

-- Код строки --
kod_ ALIAS FOR $1;





BEGIN 


UPDATE sc_spec SET sc_rec_delete='delete' WHERE sc_rec_id=kod_;



RETURN 'OK';



END;$BODY$

LANGUAGE 'plpgsql'






