CREATE OR REPLACE FUNCTION in_DelMac(varchar(24)) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

-- Идентификатор записи ---
kod ALIAS FOR $1;




BEGIN 


--- Проверка поступивших данных на корректность ---
IF length(kod)=0 THEN
	RETURN 'ERRORDATA';
END IF;




--- Пометка записи как удаленной ---
UPDATE in_mac_list SET in_rec_delete='delete',in_update_time=now(),in_update_author=current_user WHERE in_rec_id=kod;





RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql'






