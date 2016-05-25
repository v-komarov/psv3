CREATE FUNCTION ps_DelPayIntoOther(varchar(24)) RETURNS text

AS 
$BODY$

DECLARE

---- Переменные -----

-- Идентификатор записи в таблице --
ps_rec_id_ ALIAS FOR $1;


BEGIN 


-- Отметка что запись удалена ---
UPDATE ps_pay_in_other SET ps_rec_delete='delete' WHERE ps_rec_id=ps_rec_id_;


RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql'






