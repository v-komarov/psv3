CREATE OR REPLACE FUNCTION ps_EnterOstatok(varchar(24),varchar(30),varchar(10)) RETURNS text

AS 
$BODY$

DECLARE

---- Переменные -----

-- Код абонента - идентификатор строки ---
kod_ab ALIAS FOR $1;

-- Услуга (название) --
ser_ ALIAS FOR $2;

-- Вносимый на лицевой счет остаток как строка ---
sum_money ALIAS FOR $3;

-- Тарифный план (код) --
kod_tp varchar(24);

-- Код услуги ---
kod_ser varchar(24);

-- Общий баланс абонента -- 
balans numeric(10,2);

-- Вносимый остаток тип numeric --
money_sum numeric(10,2);


-- Вспомогательная переменная при определении кода услуги по названию ---
a int4;

-- Вспомогательная переменная при определении наличия услуги в тарифном плане абонента ---
n int4;

-- Вспомогательная переменная при определении наличия лицевого счета по услуге ---
b int4;

-- Вспомогательные переменные для подсчета кол-ва строк в ps_pay_in и ps_pay_out --
nn0 int4;
nn1 int4;


BEGIN 

--- Проверка полученных значаний на не нулевые длинны строк ---
IF char_length(kod_ab)=0 OR char_length(ser_)=0 OR char_length(sum_money)=0 THEN
RETURN 'ERROR IN DATA';
END IF;


--- Перевод суммы денег строки в тип numeric ---
money_sum := to_number(sum_money,'9999990.00');

--IF money_sum=0 THEN
--RETURN 'ERROR IN DATA';
--END IF;

--- Определение кода тарифного плана по коду абонента ---
SELECT INTO kod_tp ps_tarif_plan FROM ps_abonent_list WHERE ps_rec_id=kod_ab;


--- Определение кода услуги по ее названию ---
SELECT INTO a count(*) FROM ps_services WHERE btrim(ps_services_name)=btrim(ser_);
IF a=0 THEN
RETURN 'CANT FIND SERVICE KOD';
END IF;
SELECT INTO kod_ser ps_rec_id FROM ps_services WHERE btrim(ps_services_name)=btrim(ser_);


--- Определение определена ли данная услуга в тарифном плане по которому работает абонент ---
SELECT INTO n count(*) FROM ps_tarif_plan WHERE ps_tarif_plan_kod=kod_tp AND ps_service_kod=kod_ser;
IF n=0 THEN
RETURN 'ERROR TARIF PLAN';
END IF;


--- Определение наличия необходимого лицевого счета по услуге ---
SELECT INTO b count(*) FROM ps_ls WHERE ps_abonent_kod=kod_ab AND ps_service_kod=kod_ser;
IF b=0 THEN
INSERT INTO ps_ls(ps_rec_id,ps_abonent_kod,ps_service_kod) VALUES(ps_GenKeyCheck(5),kod_ab,kod_ser);
END IF;


--- Определение имеются ли записи платежей и удержаний по данной услуге ---
SELECT INTO nn0 count(*) FROM ps_pay_in WHERE ps_abonent_kod=kod_ab AND ps_service_kod=kod_ser AND ps_rec_delete<>'delete';
SELECT INTO nn1 count(*) FROM ps_pay_out WHERE ps_abonent_kod=kod_ab AND ps_service_kod=kod_ser AND ps_rec_delete<>'delete';


--- Если имеют место действующие записи платежей и удержаний по данной услуге, то вносить начальный остаток нельзя ---
IF (nn0<>0) OR (nn1<>0) THEN
RETURN 'CANT THIS ACTION';
END IF;


--- Фиксация изменений в базе (финансовая транзакция) --

--- Измеение состояния лицевого счета по услуге - внесение начального остатка ---
UPDATE ps_ls SET ps_ls_sum=money_sum WHERE ps_abonent_kod=kod_ab AND ps_service_kod=kod_ser;


--- Определение общего баланса абонента как суммы лицевых счетов ---
SELECT INTO balans sum(ps_ls_sum) FROM ps_ls WHERE ps_abonent_kod=kod_ab;

--- Изменение общего баланса абонента ---
UPDATE ps_abonent_list SET ps_balans_total=balans WHERE ps_rec_id=kod_ab;


--- Регистрация события в заметках ---
INSERT INTO ps_messages(ps_rec_id,ps_abonent_kod,ps_mess_txt) VALUES(ps_GenKeyCheck(8),kod_ab,'ВВОД ОСТАТКА '||sum_money||' ПО УСЛУГЕ '||ser_);




--- Обработка если услуга INTERNET 9-11-2007 ---
--IF btrim(ser_)='INTERNET' THEN
--- Если услуга Internet - проверяем и корректируем доступ абонента --
--PERFORM in_CheckInternet(kod_ab);
--END IF;





RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql'






