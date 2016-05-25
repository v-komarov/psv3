CREATE FUNCTION in_AddTarif(varchar(30),varchar(10)) RETURNS text

AS '

DECLARE

---- ���������� -----

-- �������� ������ --
tarif_ ALIAS FOR $1;

-- ���� �� 1����� ��� ������--
cost_ ALIAS FOR $2;

-- ���� �� 1����� ��� ����� ---
cost2_ numeric(8,2);

-- ���������� ����� � ������� �� ������ ---
i int2;

-- ���������� ����� ������ ---
n int2;

-- ��������������� ���������� ���������� �������� --
nn int2;



BEGIN 


-- �������� �� �� ������ ������������ �������� ---
IF char_length(tarif_)=0 OR char_length(cost_)=0 THEN
RETURN \'ERROR IN DATA\';
END IF;



-- ����������� ���������� ����� ---
SELECT INTO i count(*) FROM in_traf_cost;

-- ���� ����� ��� �� ��������� ������ ����� � ��������������� 1 --
IF i=0 THEN
n := 1;
ELSE
-- ���� ������ ����, �������� �� ���������� �������� ������ ������ � ��� ������������� --
SELECT INTO nn count(*) FROM in_traf_cost WHERE btrim(in_cost_name)=btrim(tarif_);
IF nn!=0 THEN
RETURN \'ERROR IN DATA\';
END IF;
-- ����������� ������������� �������� �������������� ������ ---
SELECT INTO n max(in_rec_id) FROM in_traf_cost;
n := n+1;
END IF;


-- ������� ���� �� ������ � ����� ---
cost2_ := to_number(cost_,\'9990.00\');


-- ���������� ������ ������ ---
INSERT INTO in_traf_cost(in_rec_id,in_cost_name,in_cost_1mb) VALUES(n,btrim(tarif_),cost2_);


RETURN \'OK\';



END;'

LANGUAGE 'plpgsql'






