CREATE FUNCTION in_AddTarif(varchar(30),varchar(10)) RETURNS text

AS '

DECLARE

---- Переменные -----

-- Название тарифа --
tarif_ ALIAS FOR $1;

-- Цена за 1МБайт как строка--
cost_ ALIAS FOR $2;

-- Цена за 1МБайт как число ---
cost2_ numeric(8,2);

-- Количество строк в тарифах на трафик ---
i int2;

-- Порядковый номер строки ---
n int2;

-- Вспомогательная переменная совпадения названий --
nn int2;



BEGIN 


-- Проверка на не пустые передаваемые значения ---
IF char_length(tarif_)=0 OR char_length(cost_)=0 THEN
RETURN \'ERROR IN DATA\';
END IF;



-- Определение количества строк ---
SELECT INTO i count(*) FROM in_traf_cost;

-- Если строк нет то следующая строка будет с идентификатором 1 --
IF i=0 THEN
n := 1;
ELSE
-- Если строки есть, проверка на совпадения названия нового тарифа с уже существующими --
SELECT INTO nn count(*) FROM in_traf_cost WHERE btrim(in_cost_name)=btrim(tarif_);
IF nn!=0 THEN
RETURN \'ERROR IN DATA\';
END IF;
-- Определение максимального значения идентификатора строки ---
SELECT INTO n max(in_rec_id) FROM in_traf_cost;
n := n+1;
END IF;


-- Перевод цены из строки в число ---
cost2_ := to_number(cost_,\'9990.00\');


-- Добавление нового тарифа ---
INSERT INTO in_traf_cost(in_rec_id,in_cost_name,in_cost_1mb) VALUES(n,btrim(tarif_),cost2_);


RETURN \'OK\';



END;'

LANGUAGE 'plpgsql'






