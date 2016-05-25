CREATE OR REPLACE FUNCTION mr_DelCost(varchar(24)) RETURNS text

AS $BODY$

--- Удаление цены материала ---


DECLARE

---- Переменные -----

-- Код записи --
rec_kod ALIAS FOR $1;

--- Дата начала действия цены ---
start_date date;

--- Вспомогательная переменная ----
n int;






BEGIN 


--- Проверка поступивших данных ---
IF length(rec_kod)=0 THEN
	RETURN 'ERRORDATA';
END IF;


--- Определение даты начала дейсвия цены ---
SELECT INTO start_date mr_date_start FROM mr_mate_cost WHERE mr_rec_id=rec_kod;


--- Дата не должна быть в прошлом ---
IF current_date>start_date THEN
	RETURN 'NOTACCESS';
END IF;


--- "Удаление" записи ---
UPDATE mr_mate_cost
SET
mr_rec_delete='delete',
mr_update_time=current_timestamp,
mr_update_author=current_user
WHERE
mr_rec_id=rec_kod;


RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql';



