CREATE FUNCTION in_GenPass() RETURNS text

AS '

DECLARE


Password varchar(24); 
i int2;
j int2;
tmp int2;
Symbol varchar(1);


BEGIN 
-- ��������� �������������
i:=1;
Password=\'\';
-- ���� ���������� ��������� �������� 
WHILE i <= 8 LOOP  
			
-- ������� ��������� ����� �� ���������� {48-57},{65-90},{97-122}
j:=trunc(random()*3+1);

if j=1 then
tmp:=trunc(random()*9+48);
else
if j=2 then
tmp:=trunc(random()*25+65);
else
tmp:=trunc(random()*25+97);
end if;
end if;

-- ��������� ���������� ������� �������� chr()
Symbol:=chr(tmp);
-- ���������� ���������� ������� � ������
Password:=Password||Symbol;
-- ���������� �������� ����� i
i := i + 1;
END LOOP;  
-- ������� ����������
RETURN Password; 




END;'

LANGUAGE 'plpgsql'






