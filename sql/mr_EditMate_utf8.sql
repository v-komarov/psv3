CREATE OR REPLACE FUNCTION mr_EditMate(int,varchar(200),varchar(100),varchar(90)) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

-- Идентификатор строки ---
rec_id ALIAS FOR $1;

-- Название материала --
mate_name ALIAS FOR $2;

--- Название ед измерения ---
eds_name ALIAS FOR $3;

--- Название группы ---
group_name ALIAS FOR $4;

--- Код ед. измерения ---
eds_kod varchar(3);

--- Код группы ---
group_kod int;

--- Вспомогательная переменная ----
n int;

--- Иддентификатор наличия движения по данному материалу ---
story_ok int;





BEGIN 


--- Проверка поступивших данных ---
IF length(group_name)=0 OR length(eds_name)=0 OR length(mate_name)=0 OR rec_id IS NULL THEN
	RETURN 'ERRORDATA';
END IF;


--- Проверка на наличие движения по данному материала ---
SELECT INTO story_ok count(*) FROM mr_story_q WHERE mr_mate_kod=rec_id AND mr_rec_delete='';


--- А есть ли материал с таким же названием? ---
SELECT INTO n count(*) FROM mr_mate_list WHERE ps_RusUpper(btrim(mr_mate_name))=ps_RusUpper(btrim(mate_name)) AND mr_rec_id!=rec_id;
IF n!=0 THEN
	RETURN 'NOTACCESS';
END IF;


--- Определение кодов группы и ед. измерения ---
SELECT INTO group_kod mr_rec_id FROM mr_group_list WHERE btrim(mr_group_name)=btrim(group_name);
SELECT INTO eds_kod mr_rec_id FROM mr_eds_list WHERE btrim(mr_eds_name)=btrim(eds_name);


IF story_ok=0 THEN
	--- Движений не было ---
	UPDATE mr_mate_list
	SET
	mr_mate_name=btrim(mate_name),
	mr_eds_kod=eds_kod,
	mr_group_kod=group_kod,
	mr_update_time=current_timestamp,
	mr_update_author=current_user
	WHERE mr_rec_id=rec_id;
ELSE
	--- Движения были - единицы измерения не меняем ---
	UPDATE mr_mate_list
	SET
	mr_mate_name=btrim(mate_name),
	mr_group_kod=group_kod,
	mr_update_time=current_timestamp,
	mr_update_author=current_user
	WHERE mr_rec_id=rec_id;
END IF;



RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql';



