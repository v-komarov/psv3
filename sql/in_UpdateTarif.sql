CREATE FUNCTION in_UpdateTarif(int4,varchar(30),varchar(10)) RETURNS text

AS '

DECLARE

---- Переменные -----

-- Идентификатор строки ---
rec_id ALIAS FOR $1;

-- Название тарифа --
tarif_ ALIAS FOR $2;

-- Цена за 1МБайт как строка--
cost_ ALIAS FOR $3;

-- Цена за 1МБайт как число ---
cost2_ numeric(8,2);


-- Вспомогательная переменная совпадения названий --
nn int2;



BEGIN 


-- Проверка на не пустые передаваемые значения ---
IF char_length(tarif_)=0 OR char_length(cost_)=0 THEN
RETURN \'ERROR IN DATA\';
END IF;



-- Если строки есть, проверка на совпадения названия нового тарифа с уже существующими --
SELECT INTO nn count(*) FROM in_traf_cost WHERE btrim(in_cost_name)=btrim(tarif_) AND in_rec_id<>rec_id;
IF nn!=0 THEN
RETURN \'ERROR IN DATA\';
END IF;


-- Перевод цены из строки в число ---
cost2_ := to_number(cost_,\'9990.00\');


-- Изменение тарифа ---
UPDATE in_traf_cost SET in_cost_name=btrim(tarif_) ,in_cost_1mb=cost2_ WHERE in_rec_id=rec_id;


RETURN \'OK\';



END;'

LANGUAGE 'plpgsql'






