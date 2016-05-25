CREATE OR REPLACE FUNCTION sc_AddWorker(varchar(30),varchar(30),varchar(30)) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

-- Фамилия ---
name_1 ALIAS FOR $1;

-- Имя ---
name_2 ALIAS FOR $2;

-- Отчества --
name_3 ALIAS FOR $3;

-- Сгенерированный уникальный ключ ---
genk varchar(24);

--- Вспомогательная переменная ---
n int2;





BEGIN 


--- Проверка поступивших данных на корректность ---
IF length(name_1)=0 OR length(name_2)=0 OR length(name_3)=0 THEN
	RETURN 'ERRORDATA';
END IF;



--- Проверка есть ли уже такой ФИО ---
SELECT INTO n count(*) FROM sc_worker_list WHERE btrim(sc_name_1)=ps_RusUpper(btrim(name_1)) AND btrim(sc_name_2)=ps_RusUpper(btrim(name_2)) AND btrim(sc_name_3)=ps_RusUpper(btrim(name_3)) AND sc_rec_delete!='delete';
IF n!=0 THEN
	RETURN 'ERRORDATA';
END IF;

--- Если такая запись есть, но помеченная как удаленная ---
SELECT INTO n count(*) FROM sc_worker_list WHERE btrim(sc_name_1)=ps_RusUpper(btrim(name_1)) AND btrim(sc_name_2)=ps_RusUpper(btrim(name_2)) AND btrim(sc_name_3)=ps_RusUpper(btrim(name_3)) AND sc_rec_delete='delete';
IF n!=0 THEN
	SELECT INTO genk sc_rec_id FROM sc_worker_list WHERE btrim(sc_name_1)=ps_RusUpper(btrim(name_1)) AND btrim(sc_name_2)=ps_RusUpper(btrim(name_2)) AND btrim(sc_name_3)=ps_RusUpper(btrim(name_3)) AND sc_rec_delete='delete';
	UPDATE sc_worker_list SET sc_rec_delete='',sc_update_time=now(),sc_update_author=current_user WHERE sc_rec_id=genk;
	RETURN 'OK';
END IF;



--- Первоначально такой ключ существует ---
n:=1;
--- Получение уникального ключа ---
WHILE n<>0 LOOP
	genk:=ps_GenKey24();
	SELECT INTO n count(*) FROM sc_worker_list WHERE sc_rec_id=genk;
END LOOP;



-- Добавление записи ---
INSERT INTO sc_worker_list(
sc_rec_id,
sc_name_1,
sc_name_2,
sc_name_3
)
VALUES(
genk,
ps_RusUpper(btrim(name_1)),
ps_RusUpper(btrim(name_2)),
ps_RusUpper(btrim(name_3))
);


RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql'






