CREATE FUNCTION in_DelTrafPay(varchar(24),varchar(25)) RETURNS text

AS '

/*
	������� ��������� �� ������ � �������� ����� ������
*/


DECLARE

---- ���������� -----

-- ��� ������� ������ (��� ��������) --
kod_abonent ALIAS FOR $1;

-- ���� � ����� ������ --
time_ses ALIAS FOR $2;

-- ��� ������� ������ �������� ����� ---
kod_ls varchar(24);

-- ����� ������ ---
balans numeric(10,2);

-- ��� ������ INTERNET --
kod_internet varchar(24);

-- ����� �������� ����� ��... -
sum_before numeric(10,2);

-- ����� �������� ����� �����... -
sum_after numeric(10,2);

-- ����� ������ ---
sum_ses numeric(8,2);




BEGIN 

-- ����������� ���� ������ INTERNET ---
SELECT INTO kod_internet ps_rec_id FROM ps_services WHERE btrim(ps_services_name)=\'INTERNET\';

-- ��� �������� ����� ---
SELECT INTO kod_ls ps_rec_id FROM ps_ls WHERE ps_abonent_kod=kod_abonent AND ps_service_kod=kod_internet;

-- ����������� ����� �������� ����� ������ INTERNET ---
SELECT INTO sum_before ps_ls_sum FROM ps_ls WHERE ps_rec_id=kod_ls; 

-- ����������� ����� ��������� ������ --
SELECT INTO sum_ses in_sum FROM in_pay_traf WHERE in_rec_abonent=kod_abonent AND substr(in_date_time,1,19)=substr(time_ses,1,19);

-- ����� �� ������� �����, ������� ������ �����... -
sum_after := sum_before+sum_ses;

-- ��������� �������� ����� � ������� ������ ��������� �� ������ ��� ��������� --
UPDATE ps_ls SET ps_ls_sum=sum_after WHERE ps_rec_id=kod_ls;
UPDATE in_pay_traf SET in_rec_delete=\'delete\' WHERE substr(in_date_time,1,19)=substr(time_ses,1,19) AND in_rec_abonent=kod_abonent;

-- ����������� ������ ������� --
SELECT INTO balans sum(ps_ls_sum) FROM ps_ls WHERE ps_abonent_kod=kod_abonent;
UPDATE ps_abonent_list SET ps_balans_total=balans WHERE ps_rec_id=kod_abonent;



RETURN \'OK\';



END;'

LANGUAGE 'plpgsql'






