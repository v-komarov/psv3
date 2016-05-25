CREATE FUNCTION sc_WriteWorker(varchar(24), varchar(50), varchar(12)) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

-- Код бригады --
wk_kod ALIAS FOR $1;


-- Телефон --
wk_phone ALIAS FOR $2;


-- Пинкод --
wk_pinkod ALIAS FOR $3;



BEGIN 


UPDATE sc_worker SET sc_worker_phone=btrim(wk_phone), sc_pinkod=wk_pinkod WHERE sc_rec_id=wk_kod;


RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql'



