CREATE FUNCTION sc_GenKeyCheckSC(int4) 
        RETURNS varchar(24) 
        AS $BODY$

DECLARE

--- Получаемое значение уникального ключа ---
genk varchar(24);

--- Передаваемое значение - число индентификатор таблицы, в которой нужно проверять существование ключа ---
-- sc_list - 1
-- sc_spec - 2
-- sc_worker -3

id_ ALIAS FOR $1;

-- Результат поиска существующего ключа в таблице ---
n int4;


BEGIN

-- Первоначально предполагаем, что такой же ключ уже существует
n:=1;


WHILE n<>0 LOOP
genk:=ps_GenKey24();

-- Для списка заявок --
IF id_=1 THEN
SELECT INTO n count(*) FROM sc_list WHERE sc_rec_id=genk;
END IF;

-- Для специализации --
IF id_=2 THEN
SELECT INTO n count(*) FROM sc_spec WHERE sc_rec_id=genk;
END IF;

-- Для бригад ---
IF id_=3 THEN
SELECT INTO n count(*) FROM sc_worker WHERE sc_rec_id=genk;
END IF;


END LOOP;


RETURN genk;

END;$BODY$ 
LANGUAGE 'plpgsql';
