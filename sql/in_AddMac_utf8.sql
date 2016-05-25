CREATE OR REPLACE FUNCTION in_AddMac(varchar(24),int,varchar(20)) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

-- Идентификатор учетной записи абонента ---
kod_ab ALIAS FOR $1;

-- Тип MAC адреса: 1-INTERNET, 2-IPTV ---
tip ALIAS FOR $2;

-- MAC --
mac ALIAS FOR $3;

-- Сгенерированный уникальный ключ ---
genk varchar(24);

--- Вспомогательная переменная ---
n int2;





BEGIN 


--- Проверка поступивших данных на корректность ---
IF length(kod_ab)=0 OR length(mac)=0 THEN
	RETURN 'ERRORDATA';
END IF;



--- Проверка есть ли уже такой мак адрес ---
SELECT INTO n count(*) FROM in_mac_list WHERE btrim(in_mac)=btrim(lower(mac)) AND in_type=tip AND in_rec_delete!='delete';
IF n!=0 THEN
	RETURN 'ERRORDATA';
END IF;

--- Если такая запись есть, но помеченная как удаленная ---
SELECT INTO n count(*) FROM in_mac_list WHERE btrim(in_mac)=btrim(lower(mac)) AND in_type=tip AND in_rec_delete='delete';
IF n!=0 THEN
	SELECT INTO genk in_rec_id FROM in_mac_list WHERE btrim(in_mac)=btrim(lower(mac)) AND in_type=tip AND in_rec_delete='delete';
	UPDATE in_mac_list SET in_rec_delete='',in_update_time=now(),in_update_author=current_user WHERE in_rec_id=genk;
	RETURN 'OK';
END IF;



--- Первоначально такой ключ существует ---
n:=1;
--- Получение уникального ключа ---
WHILE n<>0 LOOP
	genk:=ps_GenKey24();
	SELECT INTO n count(*) FROM in_mac_list WHERE in_rec_id=genk;
END LOOP;



-- Добавление записи ---
INSERT INTO in_mac_list(
in_rec_id,
in_abonent_kod,
in_type,
in_mac
)
VALUES(
genk,
kod_ab,
tip,
lower(btrim(mac))
);


RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql'






