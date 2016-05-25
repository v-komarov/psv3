CREATE FUNCTION ps_Del4PayInto(varchar(24)) RETURNS text

AS 
$BODY$

DECLARE

---- Переменные -----

-- Идентификатор записи в таблице --
ps_rec_id_ ALIAS FOR $1;

-- Сумма, которая должна быть удалена ---
del_sum numeric(10,2);

-- Код абонента ---
kod_ab varchar(24);

-- Код услуги ---
kod_ser varchar(24);

-- Сумма на лицевом счете до удаления ---
ls_sum_before numeric(10,2);

-- Сумма на лицевом счете после удаления ---
ls_sum_after numeric(10,2);

-- Сумма общего баланса --
balans numeric(10,2);

-- Название услуги ---
ser_name varchar(30);


BEGIN 


-- Определение суммы, которая должна быть удалена --
SELECT INTO del_sum ps_service_sum FROM ps_pay_in WHERE ps_rec_id=ps_rec_id_;

-- Определение кода абонента ---
SELECT INTO kod_ab ps_abonent_kod FROM ps_pay_in WHERE ps_rec_id=ps_rec_id_;

-- Определение кода сервиса ---
SELECT INTO kod_ser ps_service_kod FROM ps_pay_in WHERE ps_rec_id=ps_rec_id_;



-- Определение суммы лицевого счета --
SELECT INTO ls_sum_before ps_ls_sum FROM ps_ls WHERE ps_abonent_kod=kod_ab AND ps_service_kod=kod_ser;
-- Сумма, котрая должна стать ---
ls_sum_after:=ls_sum_before-del_sum;

-- Изменение лицевого счета абонента ---
UPDATE ps_ls SET ps_ls_sum=ls_sum_after WHERE ps_abonent_kod=kod_ab AND ps_service_kod=kod_ser;


-- Определение общего баланса абонента ---
SELECT INTO balans sum(ps_ls_sum) FROM ps_ls WHERE ps_abonent_kod=kod_ab;


-- Изменение общего баланса абонента --
UPDATE ps_abonent_list SET ps_balans_total=balans WHERE ps_rec_id=kod_ab;


-- Отметка что запись удалена ---
UPDATE ps_pay_in SET ps_rec_delete='delete' WHERE ps_rec_id=ps_rec_id_;



--- Обработка если услуга INTERNET 9-11-2007 ---
SELECT INTO ser_name ps_services_name FROM ps_services WHERE ps_rec_id=kod_ser;
--IF btrim(ser_name)='INTERNET' THEN
--- Если услуга Internet - проверяем и корректируем доступ абонента --
--PERFORM in_CheckInternet(kod_ab);
--END IF;





RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql'






