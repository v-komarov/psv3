CREATE FUNCTION in_CheckInternet(varchar(24)) RETURNS text

AS '

DECLARE

---- Переменные -----

-- Код учетной записи (код абонента) --
kod_r ALIAS FOR $1;

-- Код услуги INTERNET --
kod_s varchar(24);

-- Значение лицевого счета ---
sum_ls numeric(10,2);

-- Флаг есть ли в тарифном плане INTERNET услуга ---
internet_ok int2;

-- Флаг наличия учетной записи ---
internet_rec int2;

-- Код тарифа с максимальной ценой --
cost_kod int4;



BEGIN 

-- Определение кода услуги INTERNET ---
SELECT INTO kod_s ps_rec_id FROM ps_services WHERE btrim(ps_services_name)=\'INTERNET\';



-- Есть ли в тарифном плане абонента услуга INTERNET ---
SELECT INTO internet_ok count(*) FROM ps_abonent_list a, ps_tarif_plan t, ps_services s WHERE a.ps_rec_id=kod_r AND a.ps_tarif_plan=t.ps_tarif_plan_kod AND t.ps_rec_delete<>\'delete\'  AND t.ps_service_kod=s.ps_rec_id AND btrim(s.ps_services_name)=\'INTERNET\';




IF internet_ok=0 THEN
-- Если такой услуги в тарифном плане нет , то не должно быть активной учетной записи --
SELECT INTO internet_rec count(*) FROM in_account WHERE in_rec_id=kod_r;
IF internet_rec<>0 THEN
UPDATE in_account SET in_rec_delete=\'delete\' WHERE in_rec_id=kod_r;
END IF;
-- Если такая услуга есть, то нужно создать учетную запись либо активировать существующую --
ELSE	
	SELECT INTO internet_rec count(*) FROM in_account WHERE in_rec_id=kod_r;
	IF internet_rec=0 THEN
	--- Определение кода тарифа с максимальной ценой ---
	SELECT INTO cost_kod in_rec_id FROM in_traf_cost order by in_cost_1mb desc LIMIT 1;
	INSERT INTO in_account(in_rec_id,in_user_login,in_user_passwd,in_cost_kod) VALUES(kod_r,substr(in_GenLogin(),1,8),substr(in_GenPass(),1,8),cost_kod);
	END IF;		

	--- В зависимости от лицевого счета блокируется или разблокируется учетная запись ---
	-- Определение суммы лицевого счета услуги INTERNET ---
	SELECT INTO sum_ls sum(ps_ls_sum) FROM ps_ls WHERE ps_abonent_kod=kod_r AND ps_service_kod=kod_s; 
	IF sum_ls<=0 THEN
	UPDATE in_account SET in_rec_delete=\'delete\' WHERE in_rec_id=kod_r;
	ELSE
	UPDATE in_account SET in_rec_delete=\'\' WHERE in_rec_id=kod_r;
	END IF;

END IF;



RETURN \'OK\';



END;'

LANGUAGE 'plpgsql'






