CREATE FUNCTION ps_DelSerFromTPlan(varchar(24)) RETURNS text

AS 
$BODY$

DECLARE

---- Переменные -----

-- Код строки --
kod_ ALIAS FOR $1;


-- Код услуги --
kod_ser varchar(24);


-- Название услуги ---
name_ser varchar(30);


-- Код тарифного плана ---
kod_tp varchar(24);


--- Переменная для хранения промежуточных данных строк ---
row_data ps_abonent_list%ROWTYPE;




BEGIN 


UPDATE ps_tarif_plan SET ps_rec_delete='delete' WHERE ps_rec_id=kod_;


--- Обработка INTERNET услуги при удалении ---
--- Определение кода удаляемой услуги ---
SELECT INTO kod_ser ps_service_kod FROM ps_tarif_plan WHERE ps_rec_id=kod_;
--- Определение названия услуги, которая удаляется ---
SELECT INTO name_ser ps_services_name FROM ps_services WHERE ps_rec_id=kod_ser;



--- Если услуга это INTERNET, то проверяем и корректируем доступ для абонентов этого тарифного плана ---
--IF btrim(name_ser)='INTERNET' THEN
	-- Определение кода тарифного плана ---
--	SELECT INTO kod_tp ps_tarif_plan_kod FROM ps_tarif_plan WHERE ps_rec_id=kod_;
--	FOR row_data IN SELECT * FROM ps_abonent_list WHERE ps_tarif_plan=kod_tp AND ps_rec_delete<>'delete' LOOP
--	PERFORM in_CheckInternet(row_data.ps_rec_id);
--	END LOOP;

--END IF;



RETURN 'OK';



END;$BODY$

LANGUAGE 'plpgsql'






