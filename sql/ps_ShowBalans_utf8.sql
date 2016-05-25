CREATE FUNCTION ps_ShowBalans(varchar(30)) RETURNS varchar(10)

AS $BODY$

DECLARE

---- Переменные -----

-- Идентификатор записи в таблице ps_abonent_list --
ps_rec_id_ ALIAS FOR $1;

--- Баланс как строка ---
balans varchar(10);



BEGIN 


SELECT INTO balans to_char(ps_balans_total,'99990.99') FROM ps_abonent_list WHERE ps_rec_id=ps_rec_id_;


RETURN balans;


END;$BODY$

LANGUAGE 'plpgsql'






