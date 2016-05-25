CREATE FUNCTION ps_SetCostServiceOfTPlan(varchar(24),varchar(10)) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

-- Код строки --
kod_ ALIAS FOR $1;


-- Передаваемая строка стоимости --
cost_str_ ALIAS FOR $2;


-- Передаваемое число стоимости ---
cost_ numeric(10,2);


BEGIN 


--- Проверка полученных значаний на не нулевые длинны строк ---
IF char_length(kod_)=0 OR char_length(cost_str_)=0 THEN
RETURN 'ERROR IN DATA';
END IF;


--- Перевод суммы денег строки в тип numeric ---
cost_ := to_number(cost_str_,'9999990.00');



UPDATE ps_tarif_plan SET ps_cost=cost_ WHERE ps_rec_id=kod_;



RETURN 'OK';



END;$BODY$

LANGUAGE 'plpgsql'






