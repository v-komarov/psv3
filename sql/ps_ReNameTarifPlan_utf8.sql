CREATE FUNCTION ps_ReNameTarifPlan(varchar(30), varchar(30)) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

-- Тарифный план (название) старый --
tp_ ALIAS FOR $1;


-- Тарифный план (название) новый --
tpnew_ ALIAS FOR $2;



--- Результат совпадения поиска тарифных планов по названию ----
n int4;


BEGIN 


--- Поиск тарифного плана по названию ---

SELECT INTO n count(*) FROM ps_tarif_plan_name WHERE btrim(ps_tarif_plan_name.ps_tarif_plan_name)=btrim(ps_RusUpper(tpnew_));


--- Если такого тарифного плана нет - меняем название ---
IF n=0 THEN


UPDATE ps_tarif_plan_name SET ps_tarif_plan_name=btrim(ps_RusUpper(tpnew_)) WHERE ps_tarif_plan_name=btrim(ps_RusUpper(tp_));


RETURN 'OK';

ELSE

RETURN 'CANT RENAME THIS TARIF PLAN';


END IF;

END;$BODY$

LANGUAGE 'plpgsql'



