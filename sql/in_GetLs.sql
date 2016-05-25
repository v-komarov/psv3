CREATE FUNCTION in_GetLs(varchar(24)) RETURNS numeric(10,2)

AS '

DECLARE

---- Переменные -----

-- Код учетной записи (код абонента) --
kod_r ALIAS FOR $1;

-- Код услуги INTERNET --
kod_s varchar(24);

-- Значение лицевого счета ---
sum_ls numeric(10,2);



BEGIN 

-- Определение кода услуги INTERNET ---
SELECT INTO kod_s ps_rec_id FROM ps_services WHERE btrim(ps_services_name)=\'INTERNET\';


-- Определение суммы лицевого счета услуги INTERNET ---
SELECT INTO sum_ls sum(ps_ls_sum) FROM ps_ls WHERE ps_abonent_kod=kod_r AND ps_service_kod=kod_s; 


RETURN sum_ls;



END;'

LANGUAGE 'plpgsql'






