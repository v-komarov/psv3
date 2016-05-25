CREATE FUNCTION in_UpdateTarifAccount(varchar(24),varchar(30)) RETURNS text

AS '

DECLARE

---- Переменные -----

-- Идентификатор строки ---
rec_id ALIAS FOR $1;

-- Название тарифа --
tarif_ ALIAS FOR $2;

-- Код тарифа ---
tarif_kod int4;

-- Вспомогательная переменная ---
n int2;


BEGIN 


-- Проверка на не пустые передаваемые значения ---
IF char_length(tarif_)=0 OR char_length(rec_id)=0 THEN
RETURN \'ERROR IN DATA\';
END IF;

-- Определение кода тарифа по названию ---
SELECT INTO n count(*) FROM in_traf_cost WHERE btrim(in_cost_name)=btrim(tarif_);
IF n<>1 THEN
RETURN \'CANT FIND TARIF\';
END IF;
SELECT INTO tarif_kod in_rec_id FROM in_traf_cost WHERE btrim(in_cost_name)=btrim(tarif_);


-- Изменение тарифа в учетной записи ---
UPDATE in_account SET in_cost_kod=tarif_kod WHERE in_rec_id=rec_id;


RETURN \'OK\';



END;'

LANGUAGE 'plpgsql'






