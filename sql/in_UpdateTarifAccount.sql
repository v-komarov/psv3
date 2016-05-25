CREATE FUNCTION in_UpdateTarifAccount(varchar(24),varchar(30)) RETURNS text

AS '

DECLARE

---- ���������� -----

-- ������������� ������ ---
rec_id ALIAS FOR $1;

-- �������� ������ --
tarif_ ALIAS FOR $2;

-- ��� ������ ---
tarif_kod int4;

-- ��������������� ���������� ---
n int2;


BEGIN 


-- �������� �� �� ������ ������������ �������� ---
IF char_length(tarif_)=0 OR char_length(rec_id)=0 THEN
RETURN \'ERROR IN DATA\';
END IF;

-- ����������� ���� ������ �� �������� ---
SELECT INTO n count(*) FROM in_traf_cost WHERE btrim(in_cost_name)=btrim(tarif_);
IF n<>1 THEN
RETURN \'CANT FIND TARIF\';
END IF;
SELECT INTO tarif_kod in_rec_id FROM in_traf_cost WHERE btrim(in_cost_name)=btrim(tarif_);


-- ��������� ������ � ������� ������ ---
UPDATE in_account SET in_cost_kod=tarif_kod WHERE in_rec_id=rec_id;


RETURN \'OK\';



END;'

LANGUAGE 'plpgsql'






