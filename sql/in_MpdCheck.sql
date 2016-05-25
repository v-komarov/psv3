CREATE OR REPLACE FUNCTION in_mpdcheck(varchar(32),inet)
  RETURNS int2 AS
'


/*

	Проверка и отключение mpd сессии

*/



DECLARE


---- идентификатор сессии : pptpX (X: 0..50) ----
ses_id_ ALIAS FOR $1;


---- IP adres mpd сервера (Radius клиент) ----
nas_ip_address_ ALIAS FOR $2;


--- Радиус логин ---
rad_login_ varchar(24);

--- Трафик в текущей сессии ---
traf_ int8;

--- Остаток на лицевом счете ---
sum_ls numeric(10,2);

--- Стоимость по тарифному плану 1МБайта ----
cost_1mb numeric(8,2);


--- Код учетной записи абонента ---
abonent_kod varchar(24);


--- Код услуги INTERNET ---
internet_kod varchar(24);


--- Код тарифа на трафик ---
kod_tarif int4;


--- Вспомогательная переменная ---
n int2;





BEGIN 



SELECT INTO n count(*) FROM radacct WHERE substr(acctsessionid,(strpos(acctsessionid,\'-\'))+1)=btrim(ses_id_) AND nasipaddress=nas_ip_address_ AND acctstoptime IS NULL GROUP BY acctstarttime ORDER BY acctstarttime DESC LIMIT 1;
IF n<>0 THEN


	---- Определение трафика в текущей сесии и логина ----
	SELECT INTO traf_,rad_login_ acctoutputoctets,btrim(username) FROM radacct WHERE substr(acctsessionid,(strpos(acctsessionid,\'-\'))+1)=btrim(ses_id_) AND nasipaddress=nas_ip_address_ AND acctstoptime IS NULL ORDER BY acctstarttime DESC LIMIT 1;



	--- Определение кода услуги INTERNET ---
	SELECT INTO internet_kod ps_rec_id FROM ps_services WHERE ps_rec_delete<>\'delete\' AND btrim(ps_services_name)=\'INTERNET\';



	--- Определение кода учетной записи абонента и кода тарифа трафика ---
	SELECT INTO abonent_kod,kod_tarif in_rec_id,in_cost_kod FROM in_account WHERE btrim(in_user_login)=btrim(rad_login_);


	---- Определение стоимости 1Мбайта и остатка на лицевом счете ----
	SELECT INTO cost_1mb in_cost_1mb FROM in_traf_cost WHERE in_rec_id=kod_tarif;
	SELECT INTO sum_ls ps_ls_sum FROM ps_ls WHERE ps_abonent_kod=abonent_kod AND ps_service_kod=internet_kod;



	----- Если в тарифном плане стоимоть 1МБайта равна 0 -----
	IF cost_1mb=0 THEN
		----- Линк не отключаем ----
		RETURN 1;
	END IF;



	--- Проверка: хватает денег или нет ---
	IF (sum_ls)<(traf_/1024/1024*cost_1mb) THEN

		----- Линк отключаем -----
		RETURN 0;

	ELSE
		----- Линк не отключаем -----
		RETURN 1;

	END IF;



END IF;

RETURN 1;

END;'
  LANGUAGE 'plpgsql';
