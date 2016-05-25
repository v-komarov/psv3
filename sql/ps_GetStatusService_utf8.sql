CREATE FUNCTION ps_GetStatusService(varchar(24),varchar(24)) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

-- Код абонента - идентификатор строки ---
kod_ab ALIAS FOR $1;

-- Код услуги --
kod_ser ALIAS FOR $2;

-- Вспомогательная переменная ---
b int4;


BEGIN 

--- Проверка услуги : присутствует ли в тарифном плане абонента, удалена или нет из тарифного плана ---
SELECT INTO b count(*) FROM ps_show_abonent_service WHERE ps_rec_id=kod_ab AND kodser=kod_ser;


IF b=1 THEN
RETURN 'ВКЛЮЧЕНО';
END IF;


IF b=0 THEN
RETURN 'ОТКЛЮЧЕНО';
END IF;


                           
RETURN 'ERROR';


END;$BODY$

LANGUAGE 'plpgsql'






