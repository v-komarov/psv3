CREATE FUNCTION sc_AddSer2Worker(varchar(30),varchar(24)) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

-- Услуга (название) --
ser_ ALIAS FOR $1;

-- Код бригады --
wk_kod ALIAS FOR $2;

--- Код услуги ---
kod_ser varchar(24);


--- Результат поиска кода услуги по названию ---
a int4;

--- Проверка наличия данной услуги в бригаде ----
n int4;


--- Проверка наличия данной услуги в бригаде помеченной как удаленная ----
nn int4;




BEGIN 


--- Определение кода услуги по названию ---
SELECT INTO a count(*) FROM ps_services WHERE btrim(ps_services_name)=btrim(ps_RusUpper(ser_));
IF a=1 THEN
SELECT INTO kod_ser ps_rec_id FROM ps_services WHERE btrim(ps_services_name)=btrim(ps_RusUpper(ser_));
ELSE
RETURN 'CANT FIND KOD THIS SERVICE';
END IF;



--- Определение есть ли уже удаленная такая услуга в бригаде ---
SELECT INTO nn count(*) FROM sc_spec WHERE sc_worker_kod=wk_kod AND sc_service=kod_ser AND sc_rec_delete='delete';
--- Если такая услуга есть - снимаем отметку удаления ---
IF nn=1 THEN
UPDATE sc_spec SET sc_rec_delete='' WHERE sc_worker_kod=wk_kod AND sc_service=kod_ser;
RETURN 'OK';
END IF;



--- Определение есть ли уже такая услуга в бригаде (вообще не было) ---
SELECT INTO n count(*) FROM sc_spec WHERE sc_worker_kod=wk_kod AND sc_service=kod_ser AND sc_rec_delete<>'delete';


--- Если такой услуги нет - добавляем ---
IF n=0 THEN
INSERT INTO sc_spec(sc_rec_id,sc_worker_kod,sc_service) VALUES(sc_GenKeyCheckSC(2),wk_kod,kod_ser);
RETURN 'OK';
ELSE
RETURN 'CANT ADD THIS SERVICE';
END IF;

END;$BODY$

LANGUAGE 'plpgsql'






