CREATE FUNCTION ps_AutoInsertAbonents(varchar(30),varchar(4),integer,varchar(30)) RETURNS text

AS 
$BODY$

DECLARE

---- Переменные -----

---- Передаваемые улица, номер дома, максимальное число квартир в доме ---
ul_ ALIAS FOR $1;
dom_ ALIAS FOR $2;
kv_ ALIAS FOR $3;
-- Тарифный план (название) --
tp_ ALIAS FOR $4;

--- счетчик ---
i int2 = 1;

--- Код тарифного плана ---
kod_tp varchar(24);

--- Результат совпадения поиска тарифных планов ----
n int4;


BEGIN 


--- Поиск тарифного плана по названию ---

SELECT INTO n count(*) FROM ps_tarif_plan_name WHERE btrim(ps_tarif_plan_name.ps_tarif_plan_name)=btrim(ps_RusUpper(tp_)) AND ps_rec_delete<>'delete';

IF n=1 THEN

SELECT INTO kod_tp ps_rec_id FROM ps_tarif_plan_name WHERE btrim(ps_tarif_plan_name)=btrim(ps_RusUpper(tp_));



WHILE i<=kv_ LOOP

INSERT INTO ps_abonent_list(ps_rec_id,ps_ul,ps_dom,ps_kv,ps_tarif_plan) VALUES(ps_GenKey24(),ps_RusUpper(ul_),dom_,btrim(to_char(i,'9999')),kod_tp);

i:=i+1;
END LOOP;


RETURN 'OK';

ELSE

RETURN 'CANT FIND THIS TARIF PLAN';


END IF;

END;$BODY$

LANGUAGE 'plpgsql'



