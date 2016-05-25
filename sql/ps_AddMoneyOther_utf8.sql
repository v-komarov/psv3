CREATE FUNCTION ps_AddMoneyOther(varchar(24),varchar(40),varchar(10)) RETURNS text

AS 

$BODY$

DECLARE

---- Переменные -----

-- Код абонента - идентификатор строки ---
kod_ab ALIAS FOR $1;

-- Назначение платежа --
naz_ ALIAS FOR $2;

-- сумма как строка ---
sum_str ALIAS FOR $3;

-- Вносимая сумма тип numeric --
sum_num numeric(10,2);



BEGIN 

--- Проверка полученных значаний на не нулевые длинны строк ---
IF char_length(kod_ab)=0 OR char_length(naz_)=0 OR char_length(sum_str)=0 THEN
RETURN 'ERROR IN DATA';
END IF;


--- Перевод суммы денег строки в тип numeric ---
sum_num := to_number(sum_str,'9999990.00');

IF sum_num=0 THEN
RETURN 'ERROR IN DATA';
END IF;


--- Добавление платежа как такового ---
INSERT INTO ps_pay_in_other(ps_rec_id,ps_abonent_kod,ps_about,ps_sum) VALUES(ps_GenKeyCheck(9),kod_ab,naz_,sum_num);

RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql'






