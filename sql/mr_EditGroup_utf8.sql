CREATE OR REPLACE FUNCTION mr_EditGroup(int,varchar(100)) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

-- Идентификатор записи ---
rec_id ALIAS FOR $1;

-- Название группы --
group_name ALIAS FOR $2;


--- Вспомогательная переменная ----
n int;

--- Идентификатор строки ---
genk int;





BEGIN 


--- Проверка поступивших данных ---
IF length(group_name)=0 OR rec_id IS NULL THEN
	RETURN 'ERRORDATA';
END IF;


--- А есть ли группа с таким же названием? ---
SELECT INTO n count(*) FROM mr_group_list WHERE ps_RusUpper(btrim(mr_group_name))=ps_RusUpper(btrim(group_name)) AND mr_rec_id!=rec_id;
IF n!=0 THEN
	RETURN 'NOTACCESS';
END IF;


--- Изменение записи ---
UPDATE mr_group_list
SET 
mr_group_name=ps_RusUpper(btrim(group_name)),
mr_update_time=current_timestamp,
mr_update_author=current_user
WHERE
mr_rec_id=rec_id;


RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql';



