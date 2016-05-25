CREATE FUNCTION sc_GenPinkod() RETURNS varchar(12)

AS $BODY$

DECLARE

pinkod varchar(12);

BEGIN 

pinkod:=substr(btrim(to_char(trunc(random()*99999999999999)+1, '99999999999999')),1,12);


RETURN pinkod;

END;$BODY$

LANGUAGE 'plpgsql'



