CREATE TABLE ps_loadpay4_log (
    ps_date_pay timestamp NOT NULL DEFAULT current_timestamp,
    ps_abonent_kod varchar(24) NOT NULL,
    ps_service_kod varchar(24) NOT NULL,
    ps_sum numeric(10,2) NOT NULL,
    ps_lsp varchar(8) NOT NULL DEFAULT '',
    ps_date_load timestamp NOT NULL DEFAULT current_timestamp,
    ps_error varchar(100) NOT NULL DEFAULT '',
    ps_ok int NOT NULL DEFAULT 0
);


--- Для таблицы ps_loadpay4_log ---
CREATE INDEX ps_loadpay4_log_i0 ON ps_loadpay4_log USING btree (ps_date_pay,ps_abonent_kod,ps_service_kod,ps_sum);
CREATE INDEX ps_loadpay4_log_i1 ON ps_loadpay4_log USING btree (ps_date_load);
CREATE INDEX ps_loadpay4_log_i2 ON ps_loadpay4_log USING btree (ps_ok);
CREATE INDEX ps_loadpay4_log_i3 ON ps_loadpay4_log USING btree (ps_date_pay);
CREATE INDEX ps_loadpay4_log_i4 ON ps_loadpay4_log USING btree (ps_abonent_kod);
CREATE INDEX ps_loadpay4_log_i5 ON ps_loadpay4_log USING btree (ps_service_kod);



CREATE OR REPLACE VIEW ps_show_loadpay4 AS
SELECT
ps_date_pay AS date_pay,
ps_date_load AS date_load,
to_char(ps_date_pay,'DD.MM.YYYY') AS date_pay_str,
to_char(ps_date_load,'DD.MM.YYYY') AS date_load_str,
ps_lsp AS lsp,
CASE 
WHEN ps_service_kod='' THEN ''
ELSE (SELECT ps_services_name FROM ps_services WHERE ps_rec_id=ps_service_kod)
END AS service_name,
CASE WHEN ps_sum IS NULL THEN 0
ELSE ps_sum
END AS sum_pay,
btrim(to_char(ps_sum,'99999999.00')) AS sum_pay_str,
ps_error AS load_error,
ps_ok AS load_ok 
FROM
ps_loadpay4_log
ORDER BY ps_date_pay,ps_lsp;



CREATE OR REPLACE FUNCTION ps_LoadPay4(varchar(8),varchar(1),timestamp,varchar(10)) RETURNS text

AS 
$BODY$

DECLARE

---- Переменные -----

-- Внешний код абонента ---
kod_ab ALIAS FOR $1;

-- Внешний код услуги --
ser_ ALIAS FOR $2;

-- Дата платежа --
date_pay ALIAS FOR $3;

-- Вносимая на лицевой счет сумма как строка ---
sum_money ALIAS FOR $4;

-- Наименование услуги --
ser_name varchar(30);

-- Вспомогательная переменная для определения количества найденых абонентов ---
x int2;

-- Код записи абонента ---
kod_rec varchar(24);

-- Тарифный план (код) --
kod_tp varchar(24);

-- Код услуги ---
kod_ser varchar(24);

-- Общий баланс абонента -- 
balans numeric(10,2);

-- Вносимая сумма тип numeric --
money_sum numeric(10,2);

-- Сумма на лицевом счете до внесения денег ---
balans_before numeric(10,2);

-- Сумма на лицевом счете после внесения денег ---
balans_after numeric(10,2);

-- Вспомогательная переменная при определении кода услуги по названию ---
a int4;

-- Вспомогательная переменная при определении наличия услуги в тарифном плане абонента ---
n int4;

-- Вспомогательная переменная при определении наличия лицевого счета по услуге ---
b int4;

-- Вспомогательные переменные ---
n1 int2;
n2 int2;
n3 int2;
n4 int2;





BEGIN 

--- Проверка полученных значений на не нулевые длинны строк ---
IF length(kod_ab)=0 OR length(ser_)=0 OR date_pay IS NULL OR length(sum_money)=0 THEN
	--- Запись в лог ---
	INSERT INTO ps_loadpay4_log(ps_date_pay,ps_abonent_kod,ps_service_kod,ps_sum,ps_lsp,ps_error,ps_ok) VALUES(date_pay,'','',0.00,'','ОБЩАЯ ОШИБКА ДАННЫХ',0);
	RETURN 'ERROR IN DATA';
END IF;


--- Перевод суммы денег строки в тип numeric ---
money_sum := to_number(sum_money,'9999990.00');

IF money_sum=0 THEN
	--- Запись в лог ---
	INSERT INTO ps_loadpay4_log(ps_date_pay,ps_abonent_kod,ps_service_kod,ps_sum,ps_lsp,ps_error,ps_ok) VALUES(date_pay,'','',0.00,kod_ab,'ОШИБКА ЗНАЧЕНИЯ СУММЫ',0);
	RETURN 'ERROR IN DATA';
END IF;




--- Определение кода абонента ---
SELECT INTO x count(*) FROM ps_abonent_list WHERE ps_lsp=kod_ab AND ps_rec_delete<>'delete';
IF x<>1 THEN
	--- Запись в лог ---
	INSERT INTO ps_loadpay4_log(ps_date_pay,ps_abonent_kod,ps_service_kod,ps_sum,ps_lsp,ps_error,ps_ok) VALUES(date_pay,'','',money_sum,kod_ab,'АБОНЕНТ НЕ НАЙДЕН',0);
	RETURN 'CANT FIND ABONENT';
ELSE
	SELECT INTO kod_rec ps_rec_id FROM ps_abonent_list WHERE ps_lsp=kod_ab AND ps_rec_delete<>'delete';
END IF;



--- Определение кода тарифного плана по коду абонента ---
SELECT INTO kod_tp ps_tarif_plan FROM ps_abonent_list WHERE ps_rec_id=kod_rec;



-- Подстановка услуги ---
IF ser_='0' THEN
	ser_name := 'ТЕЛЕВИДЕНИЕ';
ELSIF ser_='2' THEN
	ser_name := 'ДОМОФОН';
ELSIF ser_='1' THEN
	ser_name := 'IPTV';
ELSE

    --- Запись в лог ---
    INSERT INTO ps_loadpay4_log(ps_date_pay,ps_abonent_kod,ps_service_kod,ps_sum,ps_lsp,ps_error,ps_ok) VALUES(date_pay,kod_rec,'',money_sum,kod_ab,'ОШИБКА УСЛУГИ',0);
    RETURN 'ERROR SERVICE';		

		
END IF;




--- Определение кода услуги по ее названию ---
SELECT INTO a count(*) FROM ps_services WHERE btrim(ps_services_name)=btrim(ser_name);
IF a=0 THEN
	--- Запись в лог ---
	INSERT INTO ps_loadpay4_log(ps_date_pay,ps_abonent_kod,ps_service_kod,ps_sum,ps_lsp,ps_error,ps_ok) VALUES(date_pay,kod_rec,'',money_sum,kod_ab,'ОШИБКА УСЛУГИ',0);
	RETURN 'CANT FIND SERVICE KOD';
END IF;
SELECT INTO kod_ser ps_rec_id FROM ps_services WHERE btrim(ps_services_name)=btrim(ser_name);





--- Определение определена ли данная услуга в тарифном плане по которому работает абонент ---
SELECT INTO n count(*) FROM ps_tarif_plan WHERE ps_tarif_plan_kod=kod_tp AND ps_service_kod=kod_ser;
IF n=0 THEN
	--- Запись в лог ---
	INSERT INTO ps_loadpay4_log(ps_date_pay,ps_abonent_kod,ps_service_kod,ps_sum,ps_lsp,ps_error,ps_ok) VALUES(date_pay,kod_rec,kod_ser,money_sum,kod_ab,'УСЛУГИ НЕТ В ТАРИФНОМ ПЛАНЕ',0);
	RETURN 'ERROR TARIF PLAN';
END IF;


--- Определение наличия необходимого лицевого счета по услуге ---
SELECT INTO b count(*) FROM ps_ls WHERE ps_abonent_kod=kod_rec AND ps_service_kod=kod_ser;
IF b=0 THEN
	INSERT INTO ps_ls(ps_rec_id,ps_abonent_kod,ps_service_kod) VALUES(ps_GenKeyCheck(5),kod_rec,kod_ser);
END IF;


--- Сумма на лицевом счете до внесения денег ---
SELECT INTO balans_before ps_ls_sum FROM ps_ls WHERE ps_abonent_kod=kod_rec AND ps_service_kod=kod_ser;


--- Сумма на лицевом счете после внесения денег ---
balans_after := balans_before + money_sum;


--- Общий баланс абонента ---
SELECT INTO balans ps_balans_total FROM ps_abonent_list WHERE ps_rec_id=kod_rec;



--- Проверка есть ли уже такой платеж в логе внешних платежей ---
SELECT INTO n count(*) FROM ps_loadpay_log 
WHERE
ps_date_pay=date_pay AND
ps_abonent_kod=kod_rec AND
ps_service_kod=kod_ser AND
ps_sum=money_sum;

IF n!=0 THEN
	--- Запись в лог ---
	INSERT INTO ps_loadpay4_log(ps_date_pay,ps_abonent_kod,ps_service_kod,ps_sum,ps_lsp,ps_error,ps_ok) VALUES(date_pay,kod_rec,kod_ser,money_sum,kod_ab,'ТАКОЙ ПЛАТЁЖ УЖЕ ЕСТЬ',0);
	RETURN 'EXIST';
END IF;


--- Фиксация изменений в базе (финансовая транзакция) --

--- Добавление платежа как такового ---
INSERT INTO ps_pay_in(
ps_rec_id,
ps_abonent_kod,
ps_tarif_plan_kod,
ps_service_kod,
ps_service_sum,
ps_balans_before,
ps_balans_after,
ps_info,
ps_kassa_kod) 
VALUES(
ps_GenKeyCheck(6),
kod_rec,
kod_tp,
kod_ser,
money_sum,
balans_before,
balans_after,
'ВНЕШНИЙ',
5);


--- Измеение состояния лицевого счета по услуге ---
UPDATE ps_ls SET ps_ls_sum=balans_after WHERE ps_abonent_kod=kod_rec AND ps_service_kod=kod_ser;

--- Изменение общего баланса абонента ---
UPDATE ps_abonent_list SET ps_balans_total=(balans+money_sum) WHERE ps_rec_id=kod_rec;



--- Запись в лог ---
INSERT INTO ps_loadpay4_log(ps_date_pay,ps_abonent_kod,ps_service_kod,ps_sum,ps_lsp,ps_ok) VALUES(date_pay,kod_rec,kod_ser,money_sum,kod_ab,1);



RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql'




INSERT INTO ps_kassa_list(ps_rec_id,ps_kassa_name) VALUES(5,'CITYPAY');



GRANT SELECT,UPDATE,INSERT ON ps_loadpay4_log TO operatortspk;
GRANT SELECT,UPDATE,INSERT ON ps_loadpay4_log TO petrovich;

GRANT SELECT ON ps_show_loadpay4 TO operatortspk;
GRANT SELECT ON ps_show_loadpay4 TO petrovich;

