CREATE FUNCTION in_UpdatePasswd(varchar(24)) RETURNS text

AS '

DECLARE

---- Переменные -----

-- Идентификатор строки ---
rec_id ALIAS FOR $1;



BEGIN 


UPDATE in_account SET in_user_passwd=in_GenPass() WHERE in_rec_id=rec_id;


RETURN \'OK\';



END;'

LANGUAGE 'plpgsql'






