CREATE OR REPLACE FUNCTION ps_GetMoneyDayBefore() RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

--- Остаток на лицевом счете услуги стал... ---
money_after numeric(10,2);

--- Суммарный баланс абонента стал... ---
money_total numeric(10,2);


--- Переменная для хранения промежуточных данных строк ---
row_data ps_show_abonent_service%ROWTYPE;


--- Дней в этом месяце ---
day_month int;



BEGIN 


--- Дней в месяце ---
SELECT INTO day_month date_part('day',date_trunc('month' , current_date)-date_trunc('month' , current_date - interval '1 month'))+1;



--- Перебор всех абонентов и сервисов со значением day_before с положительным или отрицательном балансом  по услуге, конечно кроме удаленных ---
FOR row_data IN SELECT * FROM ps_show_abonent_service WHERE ps_type_count='day_before' LOOP

	--- Остаток на лицевом счете услуги стал... ---
	money_after:=row_data.ps_ls_sum-row_data.ps_cost/day_month;




	--- Записываем финансовую транзакцию ---
	INSERT INTO ps_pay_out(ps_rec_id,ps_abonent_kod,ps_tarif_plan_kod,ps_service_kod,ps_service_cost,ps_balans_before,ps_balans_after,ps_info) VALUES(ps_GenKeyCheck(7),row_data.ps_rec_id,row_data.kodtp,row_data.kodser,row_data.ps_cost/day_month,row_data.ps_ls_sum,money_after,'ПРОГРАММНО');
	UPDATE ps_ls SET ps_ls_sum=money_after WHERE ps_abonent_kod=row_data.ps_rec_id AND ps_service_kod=row_data.kodser;


	--- Определение суммарного баланса абонента ---
	SELECT INTO money_total sum(ps_ls_sum) FROM ps_ls WHERE ps_ls.ps_abonent_kod=row_data.ps_rec_id;

	UPDATE ps_abonent_list SET ps_balans_total=money_total WHERE ps_abonent_list.ps_rec_id=row_data.ps_rec_id;


END LOOP;




--- Завершение ---
RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql'






