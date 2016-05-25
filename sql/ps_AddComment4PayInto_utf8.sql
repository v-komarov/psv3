CREATE FUNCTION ps_AddComment4PayInto(varchar(24),varchar(30)) RETURNS text

AS 

$BODY$

DECLARE

---- Переменные -----

-- Идентификатор записи в таблице --
ps_rec_id_ ALIAS FOR $1;

--- Текст коментария (примечания) - 30 символов ---
info_ ALIAS FOR $2;


BEGIN 


UPDATE ps_pay_in SET ps_info=substr(btrim(info_),1,30) WHERE ps_rec_id=ps_rec_id_;


RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql'






