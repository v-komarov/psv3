CREATE OR REPLACE FUNCTION sc_AddTaskWorker(varchar(24),varchar(24)) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

--- Код записи --
kod_task ALIAS FOR $1;

--- код исполнителя ---
kod_worker ALIAS FOR $2;

--- Код статуса, который сейчас ---
status_now int2;

--- Вспомогательная переменная ---
n int2;

--- Уникальный ключ записи ---
genk varchar(24);



BEGIN 


--- Проверка поступивших данных на корректность ---
IF length(kod_task)=0 OR length(kod_worker)=0 THEN
	RETURN 'ERRORDATA';
END IF;


--- Определение кода статуса который сейчас ---
SELECT INTO status_now sc_status_task FROM sc_task WHERE sc_rec_id=kod_task;


--- Если заявка закрыта уже месяц - то изменение запрещено ---
SELECT INTO n date_part('day',(now()-sc_date_task_close)) FROM sc_task WHERE sc_rec_id=kod_task;
IF n>30 AND status_now=1 THEN
	RETURN 'NOTACCESS';
END IF;


--- Определение есть ли уже такая запись ---
SELECT INTO n count(*) FROM sc_worker WHERE sc_worker_kod=kod_worker AND sc_task_kod=kod_task AND sc_rec_delete!='delete';
IF n!=0 THEN
	RETURN 'NOTACCESS';
END IF;


--- Определение есть ли такая удаленная запись ---
SELECT INTO n count(*) FROM sc_worker WHERE sc_worker_kod=kod_worker AND sc_task_kod=kod_task AND sc_rec_delete='delete';
IF n!=0 THEN
	SELECT INTO genk sc_rec_id FROM sc_worker WHERE sc_worker_kod=kod_worker AND sc_task_kod=kod_task AND sc_rec_delete='delete';
	UPDATE sc_worker SET
	sc_rec_delete='',
	sc_update_time=now(),
	sc_update_author=current_user
	WHERE sc_rec_id=genk
	;
	
	RETURN 'OK';
END IF;



--- Первоначально такой ключ существует ---
n:=1;
--- Получение уникального ключа ---
WHILE n<>0 LOOP
	genk:=ps_GenKey24();
	SELECT INTO n count(*) FROM sc_worker WHERE sc_rec_id=genk;
END LOOP;


--- Добавление записи ---
INSERT INTO sc_worker(
sc_rec_id,
sc_worker_kod,
sc_task_kod
)
VALUES(
genk,
kod_worker,
kod_task
);



RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql';



