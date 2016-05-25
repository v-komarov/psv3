CREATE FUNCTION ps_GetMoneyMonthBefore() RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

--- Остаток на лицевом счете услуги стал... ---
money_after numeric(10,2);

--- Суммарный баланс абонента стал... ---
money_total numeric(10,2);


--- Переменная для хранения промежуточных данных строк ---
row_data ps_show_abonent_service%ROWTYPE;


--- Переменная для хранения промежуточных данных строк INTERNET 9-11-2007 ---
row_data2 in_account%ROWTYPE;



BEGIN 

--- Перебор всех абонентов и сервисов со значением month_before, конечно кроме удаленных ---
FOR row_data IN SELECT * FROM ps_show_abonent_service WHERE ps_type_count='month_before' LOOP

--- Остаток на лицевом счете услуги стал... ---
money_after:=row_data.ps_ls_sum-row_data.ps_cost;




--- Записываем финансовую транзакцию ---
INSERT INTO ps_pay_out(ps_rec_id,ps_abonent_kod,ps_tarif_plan_kod,ps_service_kod,ps_service_cost,ps_balans_before,ps_balans_after,ps_info) VALUES(ps_GenKeyCheck(7),row_data.ps_rec_id,row_data.kodtp,row_data.kodser,row_data.ps_cost,row_data.ps_ls_sum,money_after,'ПРОГРАММНО');
UPDATE ps_ls SET ps_ls_sum=money_after WHERE ps_abonent_kod=row_data.ps_rec_id AND ps_service_kod=row_data.kodser;


--- Определение суммарного баланса абонента ---
SELECT INTO money_total sum(ps_ls_sum) FROM ps_ls WHERE ps_ls.ps_abonent_kod=row_data.ps_rec_id;

UPDATE ps_abonent_list SET ps_balans_total=money_total WHERE ps_abonent_list.ps_rec_id=row_data.ps_rec_id;


END LOOP;




	--- Проверка и отключение при отрицательном балансе для абонентов INTERNET услуги 9-11-2007 ---
	--- Создание набора данных для проверки ---
--	FOR row_data2 IN SELECT * FROM in_account WHERE in_rec_delete<>'delete' LOOP
--	PERFORM in_CheckInternet(row_data2.in_rec_id);
--	END LOOP;



RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql'






