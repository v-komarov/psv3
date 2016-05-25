CREATE FUNCTION in_GenLogin() RETURNS text

AS '

DECLARE

---- ���������� -----

-- ������������ ����� ������ ����� �������� --
max_login int4;

-- ����� ����� --
new_login text;



BEGIN 

-- ����������� ���� ������ INTERNET ---
SELECT INTO max_login max(to_number(substr(in_user_login,5,5),\'9999\')) FROM in_account WHERE substr(in_user_login,0,5)=\'tspk\';

SELECT INTO new_login \'tspk\'||btrim(to_char(max_login+1,\'0000\'));


RETURN new_login;



END;'

LANGUAGE 'plpgsql'






