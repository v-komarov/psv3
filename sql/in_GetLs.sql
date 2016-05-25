CREATE FUNCTION in_GetLs(varchar(24)) RETURNS numeric(10,2)

AS '

DECLARE

---- ���������� -----

-- ��� ������� ������ (��� ��������) --
kod_r ALIAS FOR $1;

-- ��� ������ INTERNET --
kod_s varchar(24);

-- �������� �������� ����� ---
sum_ls numeric(10,2);



BEGIN 

-- ����������� ���� ������ INTERNET ---
SELECT INTO kod_s ps_rec_id FROM ps_services WHERE btrim(ps_services_name)=\'INTERNET\';


-- ����������� ����� �������� ����� ������ INTERNET ---
SELECT INTO sum_ls sum(ps_ls_sum) FROM ps_ls WHERE ps_abonent_kod=kod_r AND ps_service_kod=kod_s; 


RETURN sum_ls;



END;'

LANGUAGE 'plpgsql'






