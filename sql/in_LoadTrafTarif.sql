CREATE FUNCTION in_LoadTrafTarif() RETURNS text


---- �������� ������� �������� ������� �� VPNBilling ������� Zope � VPNBilling ������� wxPython ---


AS '

DECLARE

---- ���������� -----



--- ���������� ��� �������� ������������� ����������� ���������� ������� ---
row_data upd_tarif_plan%ROWTYPE;


--- ��������������� ���������� ---
n int2;



BEGIN



--- ����� ������ INTERNET ---
SELECT INTO n count(*) FROM ps_services WHERE btrim(ps_services_name)=\'INTERNET\';

IF n!=1 THEN
--- ���� ����� ������ ��� - ��������� ---
PERFORM ps_addservice(\'INTERNET\');
END IF;


--- ��������������� �������� ������ � ������� ������� �� ������ ---
DELETE FROM in_traf_cost;


--- ������� ������ �� ������ ---
FOR row_data IN SELECT * FROM upd_tarif_plan WHERE holding=\'tspk\' LOOP
	INSERT INTO in_traf_cost(in_rec_id,in_cost_name,in_cost_1mb) VALUES(row_data.id_tarif_plan,btrim(row_data.tplan_name),row_data.pay_1mb);
END LOOP;



RETURN \'OK\';


END;'

LANGUAGE 'plpgsql'






