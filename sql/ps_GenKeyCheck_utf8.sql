CREATE FUNCTION ps_GenKeyCheck(int4) 
        RETURNS varchar(24) 
        AS $BODY$

DECLARE

--- Получаемое значение уникального ключа ---
genk varchar(24);

--- Передаваемое значение - число индентификатор таблицы, в которой нужно проверять существование ключа ---
-- ps_abonent_list - 1
-- ps_tarif_plan - 2
-- ps_tarif_plan_name -3
-- ps_services - 4
-- ps_ls - 5
-- ps_pay_in - 6
-- ps_pay_out - 7
-- ps_messages - 8
-- ps_pay_in_other - 9

id_ ALIAS FOR $1;

-- Результат поиска существующего ключа в таблице ---
n int4;


BEGIN

-- Первоначально предполагаем, что такой же ключ уже существует
n:=1;


WHILE n<>0 LOOP
genk:=ps_GenKey24();

-- Для списка абонентов --
IF id_=1 THEN
SELECT INTO n count(*) FROM ps_abonent_list WHERE ps_rec_id=genk;
END IF;

-- Для наименований тарифных --
IF id_=2 THEN
SELECT INTO n count(*) FROM ps_tarif_plan WHERE ps_rec_id=genk;
END IF;

-- Для наименований тарифных планов ---
IF id_=3 THEN
SELECT INTO n count(*) FROM ps_tarif_plan_name WHERE ps_rec_id=genk;
END IF;

-- Для сервисов --
IF id_=4 THEN
SELECT INTO n count(*) FROM ps_services WHERE ps_rec_id=genk;
END IF;

-- Для лицевых счетов ---
IF id_=5 THEN
SELECT INTO n count(*) FROM ps_ls WHERE ps_rec_id=genk;
END IF;

-- Для платежей ---
IF id_=6 THEN
SELECT INTO n count(*) FROM ps_pay_in WHERE ps_rec_id=genk;
END IF;

-- Для удержаний ---
IF id_=7 THEN
SELECT INTO n count(*) FROM ps_pay_out WHERE ps_rec_id=genk;
END IF;

-- Для заметок ---
IF id_=8 THEN
SELECT INTO n count(*) FROM ps_messages WHERE ps_rec_id=genk;
END IF;

-- Для прочих платежей --
IF id_=9 THEN
SELECT INTO n count(*) FROM ps_pay_in_other WHERE ps_rec_id=genk;
END IF;

END LOOP;


RETURN genk;

END;$BODY$
LANGUAGE 'plpgsql';
