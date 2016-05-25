CREATE FUNCTION ps_AddMoneyOut(varchar(24),varchar(30),varchar(10)) RETURNS text

AS 

$BODY$

DECLARE

---- Переменные -----

-- Код абонента - идентификатор строки ---
kod_ab ALIAS FOR $1;

-- Услуга (название) --
ser_ ALIAS FOR $2;

-- Вычитаемая из лицевого счета сумма как строка ---
sum_money ALIAS FOR $3;

-- Тарифный план (код) --
kod_tp varchar(24);

-- Код услуги ---
kod_ser varchar(24);

-- Общий баланс абонента -- 
balans numeric(10,2);

-- Вычитаемая сумма тип numeric --
money_sum numeric(10,2);

-- Сумма на лицевом счете до удержания денег ---
balans_before numeric(10,2);

-- Сумма на лицевом счете после удержания денег ---
balans_after numeric(10,2);

-- Вспомогательная переменная при определении кода услуги по названию ---
a int4;

-- Вспомогательная переменная при определении наличия услуги в тарифном плане абонента ---
n int4;

-- Вспомогательная переменная при определении наличия лицевого счета по услуге ---
b int4;


BEGIN 

--- Проверка полученных значаний на не нулевые длинны строк ---
IF char_length(kod_ab)=0 OR char_length(ser_)=0 OR char_length(sum_money)=0 THEN
RETURN 'ERROR IN DATA';
END IF;


--- Перевод суммы денег строки в тип numeric ---
money_sum := to_number(sum_money,'9999990.00');

IF money_sum=0 THEN
RETURN 'ERROR IN DATA';
END IF;

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


--- Сумма на лицевом счете до удержания денег ---
SELECT INTO balans_before ps_ls_sum FROM ps_ls WHERE ps_abonent_kod=kod_ab AND ps_service_kod=kod_ser;


--- Сумма на лицевом счете после удержания денег ---
balans_after := balans_before - money_sum;



--- Фиксация изменений в базе (финансовая транзакция) --

--- Добавление платежа как такового ---
INSERT INTO ps_pay_out(ps_rec_id,ps_abonent_kod,ps_tarif_plan_kod,ps_service_kod,ps_service_cost,ps_balans_before,ps_balans_after,ps_info) VALUES(ps_GenKeyCheck(7),kod_ab,kod_tp,kod_ser,money_sum,balans_before,balans_after,'ОПЕРАТОР');

--- Измеение состояния лицевого счета по услуге ---
UPDATE ps_ls SET ps_ls_sum=balans_after WHERE ps_abonent_kod=kod_ab AND ps_service_kod=kod_ser;



--- Общий баланс абонента ---
SELECT INTO balans sum(ps_ls_sum) FROM ps_ls WHERE ps_abonent_kod=kod_ab;


--- Изменение общего баланса абонента ---
UPDATE ps_abonent_list SET ps_balans_total=balans WHERE ps_rec_id=kod_ab;



--- Обработка если услуга INTERNET 9-11-2007 ---
--IF btrim(ser_)='INTERNET' THEN
--- Если услуга Internet - проверяем и корректируем доступ абонента --
--PERFORM in_CheckInternet(kod_ab);
--END IF;





RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql'






