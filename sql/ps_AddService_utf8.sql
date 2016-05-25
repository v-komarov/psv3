CREATE FUNCTION ps_AddService(varchar(30)) RETURNS text

AS 
$BODY$

DECLARE

---- Переменные -----

-- Услуга (название) --
ser_ ALIAS FOR $1;

--- Код услуги плана ---
kod_ser varchar(24);

--- Результат совпадения поиска услуг по названию ----
n int4;


BEGIN 


--- Поиск услуги по названию ---

SELECT INTO n count(*) FROM ps_services WHERE btrim(ps_services_name)=btrim(ps_RusUpper(ser_));


--- Если такой услуги нет - добавляем ---
IF n=0 THEN


INSERT INTO ps_services(ps_rec_id,ps_services_name) VALUES(ps_GenKeyCheck(4),btrim(ps_RusUpper(ser_)));


RETURN 'OK';

ELSE

RETURN 'CANT ADD THIS SERVICE';


END IF;

END;$BODY$

LANGUAGE 'plpgsql'






