CREATE OR REPLACE FUNCTION ps_Act(varchar(24),date,date,varchar(30))
  RETURNS setof record AS
$BODY$

/*

Акт сверки по услуге

*/


DECLARE


--- Идентификатор абонента ---
rec_id ALIAS FOR $1;

--- Период ---
date_start ALIAS FOR $2;

--- Период ---
date_stop ALIAS FOR $3;

--- Название услуги ---
name_service ALIAS FOR $4;

--- Переменная для хранения строк ---
rec record;
r record;

--- Переменная для вида ps_show_pay_in ---
row_data_in ps_show_pay_in%ROWTYPE;

--- Переменная для вида ps_show_pay_out ---
row_data_out ps_show_pay_out%ROWTYPE;

--- Баланс по услуги ---
service_balans numeric(10,2) := 0.00; 

--- Вспомогательная по балансу ---
tmp_balans numeric(10,2) := 0.00;

--- Код услуги ---
kod_service varchar(24);

--- Порядковый номер записи ---
n int := 0;





BEGIN


CREATE TEMP TABLE tmp_table (
ps_rec_id int NOT NULL DEFAULT 0,
ps_oper_name varchar(50) NOT NULL DEFAULT '',
ps_oper_kod int NOT NULL DEFAULT 1,
ps_date date NOT NULL DEFAULT current_date,
ps_date_str varchar(10) NOT NULL DEFAULT '',
ps_service varchar(30) NOT NULL DEFAULT '',
ps_sum numeric(10,2) NOT NULL DEFAULT 0.00,
ps_kassa varchar(50) NOT NULL DEFAULT '',
ps_balans numeric(10,2) NOT NULL DEFAULT 0.00
);



IF length(name_service)=0 THEN
   RETURN;
END IF;

--- Определение кода услуги ---
SELECT INTO kod_service ps_rec_id FROM ps_services WHERE btrim(ps_services_name)=btrim(name_service);


--- Определение баланса по этой услуге ---
SELECT INTO service_balans ps_ls_sum FROM ps_ls WHERE ps_abonent_kod=rec_id AND ps_service_kod=kod_service;



--- Проверка поступивших данных на корректность ---
IF length(rec_id)!=0 THEN
	--- Поступления ---
	FOR row_data_in IN SELECT * FROM ps_show_pay_in WHERE btrim(service)=btrim(name_service) AND ps_abonent_kod=rec_id AND data2>=date_start LOOP
		INSERT INTO tmp_table(
		ps_rec_id,
		ps_oper_name,
		ps_oper_kod,
		ps_date,
		ps_date_str,
		ps_service,
		ps_sum,
		ps_kassa) 
		VALUES(
		n,
		'ПЛАТЕЖ',
		1,
		row_data_in.data2,
		row_data_in.data,
		row_data_in.service,
		to_number(btrim(row_data_in.sum),'9999990.00'),
		row_data_in.kassa);

		n := n + 1;

	END LOOP;

	--- Удержания ---
	FOR row_data_out IN SELECT * FROM ps_show_pay_out WHERE btrim(service)=btrim(name_service) AND ps_abonent_kod=rec_id AND data2>=date_start LOOP
		INSERT INTO tmp_table(
		ps_rec_id,
		ps_oper_name,
		ps_oper_kod,
		ps_date,
		ps_date_str,
		ps_service,
		ps_sum)
		VALUES(
		n,
		'УДЕРЖАНИЕ',
		2,
		row_data_out.data2,
		row_data_out.data,
		row_data_out.service,
		to_number(btrim(row_data_out.sum),'9999990.00'));

		n := n + 1;

	END LOOP;



	--- Расстановка сумм баланса ---
	FOR r IN (SELECT * FROM tmp_table ORDER BY ps_date DESC) LOOP

	    UPDATE tmp_table SET ps_balans=service_balans WHERE ps_rec_id=r.ps_rec_id;

	    IF r.ps_oper_kod=1 THEN
		service_balans := service_balans - r.ps_sum;
	    ELSE 
		service_balans := service_balans + r.ps_sum;
	    END IF;

	END LOOP;

	--- Убрать строки за интервалом дат ---
	DELETE FROM tmp_table WHERE ps_date>date_stop;


END IF;






FOR rec IN SELECT * FROM tmp_table ORDER BY ps_date LOOP
      RETURN NEXT rec;

END LOOP;






END;$BODY$
  LANGUAGE 'plpgsql';
  