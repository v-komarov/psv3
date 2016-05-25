CREATE OR REPLACE FUNCTION mr_AddGroup(varchar(100)) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

-- Название группы --
group_name ALIAS FOR $1;


--- Вспомогательная переменная ----
n int;

--- Идентификатор строки ---
genk int;





BEGIN 


--- Проверка поступивших данных ---
IF length(group_name)=0 THEN
	RETURN 'ERRORDATA';
END IF;


--- А есть ли группа с таким же названием? ---
SELECT INTO n count(*) FROM mr_group_list WHERE ps_RusUpper(btrim(mr_group_name))=ps_RusUpper(btrim(group_name));
IF n!=0 THEN
	RETURN 'NOTACCESS';
END IF;

--- Определение идентификатора строки ---
SELECT INTO n count(*) FROM mr_group_list;
IF n=0 THEN
	genk := 1;
ELSE
	SELECT INTO genk max(mr_rec_id)+1 FROM mr_group_list;
END IF;


--- Добавление записи ---
INSERT INTO mr_group_list(mr_rec_id,mr_group_name) VALUES(genk,ps_RusUpper(btrim(group_name)));

RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql';



