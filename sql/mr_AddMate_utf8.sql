CREATE OR REPLACE FUNCTION mr_AddMate(varchar(200),varchar(100),varchar(90)) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

-- Название материала --
mate_name ALIAS FOR $1;

--- Название ед измерения ---
eds_name ALIAS FOR $2;

--- Название группы ---
group_name ALIAS FOR $3;

--- Код ед. измерения ---
eds_kod varchar(3);

--- Код группы ---
group_kod int;


--- Вспомогательная переменная ----
n int;

--- Идентификатор строки ---
genk int;





BEGIN 


--- Проверка поступивших данных ---
IF length(group_name)=0 OR length(eds_name)=0 OR length(mate_name)=0 THEN
	RETURN 'ERRORDATA';
END IF;


--- Прорка на наличие движения по данному материала ---


--- А есть ли материал с таким же названием? ---
SELECT INTO n count(*) FROM mr_mate_list WHERE ps_RusUpper(btrim(mr_mate_name))=ps_RusUpper(btrim(mate_name));
IF n!=0 THEN
	RETURN 'NOTACCESS';
END IF;


--- Определение кодов группы и ед. измерения ---
SELECT INTO group_kod mr_rec_id FROM mr_group_list WHERE btrim(mr_group_name)=btrim(group_name);
SELECT INTO eds_kod mr_rec_id FROM mr_eds_list WHERE btrim(mr_eds_name)=btrim(eds_name);


--- Определение идентификатора строки ---
SELECT INTO n count(*) FROM mr_mate_list;
IF n=0 THEN
	genk := 1;
ELSE
	SELECT INTO genk max(mr_rec_id)+1 FROM mr_mate_list;
END IF;


--- Добавление записи ---
INSERT INTO mr_mate_list(mr_rec_id,mr_mate_name,mr_eds_kod,mr_group_kod) VALUES(genk,btrim(mate_name),eds_kod,group_kod);

RETURN 'OK#'||btrim(to_char(genk,'99990'));


END;$BODY$

LANGUAGE 'plpgsql';



