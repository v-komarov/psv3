CREATE FUNCTION in_UpdateTarif(int4,varchar(30),varchar(10)) RETURNS text

AS '

DECLARE

---- ���������� -----

-- ������������� ������ ---
rec_id ALIAS FOR $1;

-- �������� ������ --
tarif_ ALIAS FOR $2;

-- ���� �� 1����� ��� ������--
cost_ ALIAS FOR $3;

-- ���� �� 1����� ��� ����� ---
cost2_ numeric(8,2);


-- ��������������� ���������� ���������� �������� --
nn int2;



BEGIN 


-- �������� �� �� ������ ������������ �������� ---
IF char_length(tarif_)=0 OR char_length(cost_)=0 THEN
RETURN \'ERROR IN DATA\';
END IF;



-- ���� ������ ����, �������� �� ���������� �������� ������ ������ � ��� ������������� --
SELECT INTO nn count(*) FROM in_traf_cost WHERE btrim(in_cost_name)=btrim(tarif_) AND in_rec_id<>rec_id;
IF nn!=0 THEN
RETURN \'ERROR IN DATA\';
END IF;


-- ������� ���� �� ������ � ����� ---
cost2_ := to_number(cost_,\'9990.00\');


-- ��������� ������ ---
UPDATE in_traf_cost SET in_cost_name=btrim(tarif_) ,in_cost_1mb=cost2_ WHERE in_rec_id=rec_id;


RETURN \'OK\';



END;'

LANGUAGE 'plpgsql'






