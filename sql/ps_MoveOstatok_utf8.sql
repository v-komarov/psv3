CREATE OR REPLACE FUNCTION ps_MoveOstatok(varchar(24),varchar(30)) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

-- Идентификатор записи в таблице лицевых счетов --
ps_rec_id_ ALIAS FOR $1;

-- Наименование услуги, куда должнен переводиться остаток ---
ser_name ALIAS FOR $2;

-- Код абонента ---
kod_ab varchar(24);

-- Код услуги, куда должен быть перемещен остаток ---
kod_ser varchar(24);

-- Код записи лицевого счета куда должен переместиться остаток ---
kod_ls_2 varchar(24);

-- Сумма на лицевом остаток ---
ls_sum_ostatok numeric(10,2);

-- Сумма на лицевом счете до перемещения ---
ls_sum_before numeric(10,2);

-- Сумма на лицевом счете после перемещения ---
ls_sum_after numeric(10,2);

-- Вспомогательная переменная ---
i int2;

-- Название услуги, с которой происходит перемещение (для сообщения) --
ser_name_old varchar(30);

-- INTERNET -----
internet_name varchar(30) := 'INTERNET';


BEGIN 


-- Проверка существования такой услуги ---
SELECT INTO i count(*) FROM ps_services WHERE btrim(ps_services_name)=btrim(ser_name);
IF i<>1 THEN
RETURN 'CANT FIND SERVICE KOD';
END IF;


-- Определение кода услуги по наименованию --
SELECT INTO kod_ser ps_rec_id FROM ps_services WHERE btrim(ps_services_name)=btrim(ser_name);


-- Определение кода абонента, суммы остатка, название услуги ---
SELECT INTO kod_ab ps_abonent_kod FROM ps_ls WHERE ps_rec_id=ps_rec_id_;
SELECT INTO ls_sum_ostatok ps_ls_sum FROM ps_ls WHERE ps_rec_id=ps_rec_id_;
SELECT INTO ser_name_old ps_services_name FROM ps_ls,ps_services WHERE ps_ls.ps_rec_id=ps_rec_id_ AND ps_ls.ps_service_kod=ps_services.ps_rec_id;


-- Определение кода записи лицевого счета куда переносим остаток ---
SELECT INTO kod_ls_2 ps_rec_id FROM ps_ls WHERE ps_abonent_kod=kod_ab AND ps_service_kod=kod_ser;
-- Такая запись одна или нет --
SELECT INTO i count(*) FROM ps_ls WHERE ps_abonent_kod=kod_ab AND ps_service_kod=kod_ser;
IF i<>1 THEN
RETURN 'CANT DO THIS';
END IF;


-- Определение суммы лицевого счета --
SELECT INTO ls_sum_before ps_ls_sum FROM ps_ls WHERE ps_rec_id=kod_ls_2;
-- Сумма, котрая должна стать ---
ls_sum_after:=ls_sum_before+ls_sum_ostatok;


-- Изменение лицевых счетов абонента ---
UPDATE ps_ls SET ps_ls_sum=ls_sum_after WHERE ps_rec_id=kod_ls_2;
UPDATE ps_ls SET ps_ls_sum=0 WHERE ps_rec_id=ps_rec_id_;


--- Регистрация события в заметках ---
INSERT INTO ps_messages(ps_rec_id,ps_abonent_kod,ps_mess_txt) VALUES(ps_GenKeyCheck(8),kod_ab, btrim(to_char(ls_sum_ostatok,'99990.99')||' '||ser_name_old||' -> '||ser_name));




--- Обработка если услуга INTERNET 9-11-2007 ---
--IF (btrim(ser_name)=btrim(internet_name)) OR (btrim(ser_name_old)=btrim(internet_name)) THEN
--- Если услуга Internet - проверяем и корректируем доступ абонента --
--PERFORM in_CheckInternet(kod_ab);
--END IF;




RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql'






