CREATE FUNCTION ps_CheckAbonent(varchar(20),varchar(5),varchar(4)) RETURNS varchar(10)

AS 
$BODY$

DECLARE


---- Переменные -----

---- Передаваемые улица, номер дома, максимальное число квартир в доме ---
ul_ ALIAS FOR $1;
dom_ ALIAS FOR $2;
kv_ ALIAS FOR $3;

--- Количество найденых записей ---
co int4;

--- Код учетной записи ---
kod varchar(24);

BEGIN 


---- Сколько записей нашел поиск ---
SELECT INTO co count(*) FROM ps_abonent_list WHERE ps_ul like (ps_RusUpper(ul_)||'%') AND btrim(ps_dom)=ps_RusUpper(btrim(dom_)) AND btrim(ps_kv)=btrim(kv_) AND ps_rec_delete<>'delete';

---- Если запись единственная ----
IF co=1 THEN

---- Определение кода учетной записи ---
SELECT INTO kod ps_rec_id FROM ps_abonent_list WHERE ps_ul like (ps_RusUpper(ul_)||'%') AND btrim(ps_dom)=ps_RusUpper(btrim(dom_)) AND btrim(ps_kv)=btrim(kv_) AND ps_rec_delete<>'delete';


RETURN kod;

ELSE
---- Если запись не единственная либо вообще записей нет - то... ----
RETURN 'NORESULT';

END IF;

END;$BODY$

LANGUAGE 'plpgsql'



