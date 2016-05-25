CREATE OR REPLACE FUNCTION sc_EditWorker(varchar(24),varchar(30),varchar(30),varchar(30)) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

-- Код записи ---
kod_rec ALIAS FOR $1;

-- Фамилия ---
name_1 ALIAS FOR $2;

-- Имя ---
name_2 ALIAS FOR $3;

-- Отчества --
name_3 ALIAS FOR $4;

-- Сгенерированный уникальный ключ ---
genk varchar(24);

--- Вспомогательная переменная ---
n int2;





BEGIN 


--- Проверка поступивших данных на корректность ---
IF length(name_1)=0 OR length(name_2)=0 OR length(name_3)=0 OR length(kod_rec)=0 THEN
	RETURN 'ERRORDATA';
END IF;



--- Проверка есть ли уже такой ФИО ---
SELECT INTO n count(*) FROM sc_worker_list WHERE btrim(sc_name_1)=ps_RusUpper(btrim(name_1)) AND btrim(sc_name_2)=ps_RusUpper(btrim(name_2)) AND btrim(sc_name_3)=ps_RusUpper(btrim(name_3)) AND sc_rec_delete!='delete' AND sc_rec_id!=kod_rec;
IF n!=0 THEN
	RETURN 'ERRORDATA';
END IF;

--- Если такая запись есть, но помеченная как удаленная ---
SELECT INTO n count(*) FROM sc_worker_list WHERE btrim(sc_name_1)=ps_RusUpper(btrim(name_1)) AND btrim(sc_name_2)=ps_RusUpper(btrim(name_2)) AND btrim(sc_name_3)=ps_RusUpper(btrim(name_3)) AND sc_rec_delete='delete' AND sc_rec_id!=kod_rec;
IF n!=0 THEN
	RETURN 'NOTACCESS';
END IF;




-- измнение записи ---
UPDATE sc_worker_list
SET
sc_name_1=ps_RusUpper(btrim(name_1)),
sc_name_2=ps_RusUpper(btrim(name_2)),
sc_name_3=ps_RusUpper(btrim(name_3)),
sc_update_time=now(),
sc_update_author=current_user
WHERE
sc_rec_id=kod_rec
;


RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql'






