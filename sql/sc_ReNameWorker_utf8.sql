CREATE FUNCTION sc_ReNameWorker(varchar(30), varchar(30)) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

-- Бригада (название) старое --
wk_ ALIAS FOR $1;


-- Бригада (название) новое --
wknew_ ALIAS FOR $2;



--- Результат совпадения поиска бригад по названию ----
n int4;


BEGIN 


--- Поиск бригады по названию ---

SELECT INTO n count(*) FROM sc_worker WHERE btrim(sc_worker.sc_worker_name)=btrim(ps_RusUpper(wknew_));


--- Если такой бригады нет - меняем название ---
IF n=0 THEN


UPDATE sc_worker SET sc_worker_name=btrim(ps_RusUpper(wknew_)) WHERE sc_worker_name=btrim(ps_RusUpper(wk_));


RETURN 'OK';

ELSE

RETURN 'CANT RENAME THIS WORKER';


END IF;

END;$BODY$

LANGUAGE 'plpgsql'



