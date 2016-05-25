CREATE OR REPLACE FUNCTION in_GetMonthTraf(varchar(24)) RETURNS int4

AS '

DECLARE

---- ���������� -----

-- �������� ������ --
kod_ab ALIAS FOR $1;

-- ������ � ������� ������ ---
traf int4;

BEGIN 


-- ������ � ������� ������ ---
SELECT INTO traf round(sum(in_traf),0) FROM in_pay_traf WHERE date_part(\'year\',in_date_time)=date_part(\'year\',now()) AND date_part(\'month\',in_date_time)=date_part(\'month\',now()) AND in_rec_abonent=kod_ab AND in_rec_delete<>\'delete\';


RETURN traf;



END;'

LANGUAGE 'plpgsql'






