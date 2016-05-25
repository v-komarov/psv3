CREATE FUNCTION in_LoadTrafTarif() RETURNS text


---- Загрузка тарифов Интернет трафика из VPNBilling вариант Zope в VPNBilling вариант wxPython ---


AS '

DECLARE

---- Переменные -----



--- Переменные для хранения промежуточных результатов построчной выборки ---
row_data upd_tarif_plan%ROWTYPE;


--- Вспомогательная переменная ---
n int2;



BEGIN



--- Поиск услуги INTERNET ---
SELECT INTO n count(*) FROM ps_services WHERE btrim(ps_services_name)=\'INTERNET\';

IF n!=1 THEN
--- Если такой услуги нет - добавляем ---
PERFORM ps_addservice(\'INTERNET\');
END IF;


--- Предварительное удаление данных и таблицы тарифов за трафик ---
DELETE FROM in_traf_cost;


--- Перенос оплаты за трафик ---
FOR row_data IN SELECT * FROM upd_tarif_plan WHERE holding=\'tspk\' LOOP
	INSERT INTO in_traf_cost(in_rec_id,in_cost_name,in_cost_1mb) VALUES(row_data.id_tarif_plan,btrim(row_data.tplan_name),row_data.pay_1mb);
END LOOP;



RETURN \'OK\';


END;'

LANGUAGE 'plpgsql'






