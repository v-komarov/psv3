CREATE OR REPLACE FUNCTION ps_LoadPay2(varchar(30),varchar(5),varchar(4),varchar(30),timestamp,numeric(10,2)) RETURNS text

AS 
$BODY$

DECLARE

---- Переменные -----

-- Улица ---
ul_ab ALIAS FOR $1;

-- Дом --
dom_ab ALIAS FOR $2;

-- Квартира ---
kv_ab ALIAS FOR $3;

--- Название услуги ---
service_name ALIAS FOR $4;

-- Дата платежа --
date_pay ALIAS FOR $5;

-- Вносимая на лицевой счет сумма ---
money_sum ALIAS FOR $6;


-- Вспомогательная переменная для определения количества найденых абонентов ---
x int2;


--- Номер лицевого счета ---
lsp_ab varchar(8);



-- Код записи абонента ---
kod_rec varchar(24);

-- Тарифный план (код) --
kod_tp varchar(24);

-- Код услуги ---
kod_ser varchar(24);

-- Общий баланс абонента -- 
balans numeric(10,2);

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






BEGIN 

--- Проверка полученных значений на не нулевые длинны строк ---
IF length(ul_ab)=0 OR length(dom_ab)=0 OR length(kv_ab)=0 OR length(service_name)=0 OR date_pay IS NULL OR money_sum IS NULL THEN
	--- Запись в лог ---
	INSERT INTO ps_loadpay2_log(ps_date_pay,ps_ul,ps_dom,ps_kv,ps_service_name,ps_sum,ps_lsp,ps_error,ps_ok) VALUES(date_pay,ul_ab,dom_ab,kv_ab,'',0.00,'','ОБЩАЯ ОШИБКА ДАННЫХ',0);
	RETURN 'ERROR IN DATA';
END IF;




--- Определение кода абонента ---
SELECT INTO x count(*) FROM ps_abonent_list WHERE btrim(ps_ul)=btrim(ul_ab) AND btrim(ps_dom)=btrim(dom_ab) AND btrim(ps_kv)=btrim(kv_ab) AND ps_rec_delete<>'delete';
IF x<>1 THEN
	--- Запись в лог ---
	INSERT INTO ps_loadpay2_log(ps_date_pay,ps_ul,ps_dom,ps_kv,ps_service_name,ps_sum,ps_lsp,ps_error,ps_ok) VALUES(date_pay,ul_ab,dom_ab,kv_ab,'',money_sum,'','АБОНЕНТ НЕ НАЙДЕН',0);
	RETURN 'CANT FIND ABONENT';
ELSE
	SELECT INTO kod_rec,lsp_ab ps_rec_id,ps_lsp FROM ps_abonent_list WHERE btrim(ps_ul)=btrim(ul_ab) AND btrim(ps_dom)=btrim(dom_ab) AND btrim(ps_kv)=btrim(kv_ab) AND ps_rec_delete<>'delete';
END IF;



--- Определение кода тарифного плана по коду абонента ---
SELECT INTO kod_tp ps_tarif_plan FROM ps_abonent_list WHERE ps_rec_id=kod_rec;


--- Определение кода услуги по названию ---
SELECT INTO kod_ser ps_rec_id FROM ps_services WHERE btrim(ps_services_name)=btrim(service_name) AND ps_rec_delete!='delete';





--- Определение определена ли данная услуга в тарифном плане по которому работает абонент ---
SELECT INTO n count(*) FROM ps_tarif_plan WHERE ps_tarif_plan_kod=kod_tp AND ps_service_kod=kod_ser;
IF n=0 THEN
	--- Запись в лог ---
	INSERT INTO ps_loadpay2_log(ps_date_pay,ps_ul,ps_dom,ps_kv,ps_service_name,ps_sum,ps_lsp,ps_error,ps_ok) VALUES(date_pay,ul_ab,dom_ab,kv_ab,service_name,money_sum,lsp_ab,'УСЛУГИ НЕТ В ТАРИФНОМ ПЛАНЕ',0);
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
SELECT INTO n count(*) FROM ps_loadpay2_log 
WHERE
ps_date_pay=date_pay AND
btrim(ps_ul)=btrim(ul_ab) AND
btrim(ps_dom)=btrim(dom_ab) AND
btrim(ps_kv)=btrim(kv_ab) AND
btrim(ps_service_name)=btrim(service_name) AND
ps_sum=money_sum AND 
ps_ok=1;

IF n!=0 THEN
	--- Запись в лог ---
	INSERT INTO ps_loadpay2_log(ps_date_pay,ps_ul,ps_dom,ps_kv,ps_service_name,ps_sum,ps_lsp,ps_error,ps_ok) VALUES(date_pay,ul_ab,dom_ab,kv_ab,service_name,money_sum,lsp_ab,'ТАКОЙ ПЛАТЁЖ УЖЕ ЕСТЬ',0);
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
3);


--- Измеение состояния лицевого счета по услуге ---
UPDATE ps_ls SET ps_ls_sum=balans_after WHERE ps_abonent_kod=kod_rec AND ps_service_kod=kod_ser;

--- Изменение общего баланса абонента ---
UPDATE ps_abonent_list SET ps_balans_total=(balans+money_sum) WHERE ps_rec_id=kod_rec;



--- Запись в лог ---
INSERT INTO ps_loadpay2_log(ps_date_pay,ps_ul,ps_dom,ps_kv,ps_service_name,ps_sum,ps_lsp,ps_error,ps_ok) VALUES(date_pay,ul_ab,dom_ab,kv_ab,service_name,money_sum,lsp_ab,'',1);




RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql';






