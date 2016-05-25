CREATE FUNCTION ps_ShowTypeCount(varchar(30)) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

-- Значение поля ps_type_count таблицы ps_tarif_plan --
type_ ALIAS FOR $1;


BEGIN 


IF type_='month_before' THEN
RETURN 'Месяц, в начале месяца';
END IF;

IF type_='month_after' THEN
RETURN 'Месяц, в конце месяца';
END IF;

IF type_='day_before' THEN
RETURN 'День, в начале дня';
END IF;

IF type_='day_after' THEN
RETURN 'День, в конце дня';
END IF;


RETURN 'Прочее';


END;$BODY$


LANGUAGE 'plpgsql'



