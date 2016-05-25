CREATE FUNCTION in_DelTrafPay(varchar(24),varchar(25)) RETURNS text

AS '

/*
	Удаляет удержание за трафик в пределах одной сессии
*/


DECLARE

---- Переменные -----

-- Код учетной записи (код абонента) --
kod_abonent ALIAS FOR $1;

-- Дата и время сессии --
time_ses ALIAS FOR $2;

-- Код учетной записи лицевого счета ---
kod_ls varchar(24);

-- Общий баланс ---
balans numeric(10,2);

-- Код услуги INTERNET --
kod_internet varchar(24);

-- Сумма лицевого счета до... -
sum_before numeric(10,2);

-- Сумма лицевого счета после... -
sum_after numeric(10,2);

-- Сумма сессии ---
sum_ses numeric(8,2);




BEGIN 

-- Определение кода услуги INTERNET ---
SELECT INTO kod_internet ps_rec_id FROM ps_services WHERE btrim(ps_services_name)=\'INTERNET\';

-- Код лицевого счета ---
SELECT INTO kod_ls ps_rec_id FROM ps_ls WHERE ps_abonent_kod=kod_abonent AND ps_service_kod=kod_internet;

-- Определение суммы лицевого счета услуги INTERNET ---
SELECT INTO sum_before ps_ls_sum FROM ps_ls WHERE ps_rec_id=kod_ls; 

-- Определение суммы удаляемой сессии --
SELECT INTO sum_ses in_sum FROM in_pay_traf WHERE in_rec_abonent=kod_abonent AND substr(in_date_time,1,19)=substr(time_ses,1,19);

-- Сумма на лицевом счете, котороя должна стать... -
sum_after := sum_before+sum_ses;

-- Изменение лицевого счета и отметка записи удержаний за трафик как удаленной --
UPDATE ps_ls SET ps_ls_sum=sum_after WHERE ps_rec_id=kod_ls;
UPDATE in_pay_traf SET in_rec_delete=\'delete\' WHERE substr(in_date_time,1,19)=substr(time_ses,1,19) AND in_rec_abonent=kod_abonent;

-- Определение нового баланса --
SELECT INTO balans sum(ps_ls_sum) FROM ps_ls WHERE ps_abonent_kod=kod_abonent;
UPDATE ps_abonent_list SET ps_balans_total=balans WHERE ps_rec_id=kod_abonent;



RETURN \'OK\';



END;'

LANGUAGE 'plpgsql'






