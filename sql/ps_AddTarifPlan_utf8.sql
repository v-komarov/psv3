CREATE FUNCTION ps_AddTarifPlan(varchar(30)) RETURNS text

AS 
$BODY$

DECLARE

---- Переменные -----

-- Тарифный план (название) --
tp_ ALIAS FOR $1;

--- Код тарифного плана ---
kod_tp varchar(24);

--- Результат совпадения поиска тарифных планов по названию ----
n int4;


BEGIN 


--- Поиск тарифного плана по названию ---

SELECT INTO n count(*) FROM ps_tarif_plan_name WHERE btrim(ps_tarif_plan_name.ps_tarif_plan_name)=btrim(ps_RusUpper(tp_));


--- Если такого тарифного плана нет - добавляем ---
IF n=0 THEN


INSERT INTO ps_tarif_plan_name(ps_rec_id,ps_tarif_plan_name) VALUES(ps_GenKeyCheck(3),btrim(ps_RusUpper(tp_)));


RETURN 'OK';

ELSE

RETURN 'CANT ADD THIS TARIF PLAN';


END IF;

END;$BODY$

LANGUAGE 'plpgsql'



