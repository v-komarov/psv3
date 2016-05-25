CREATE FUNCTION ps_FindAbonent(varchar(20),varchar(5),varchar(4)) RETURNS text

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
--- Строка с результатом ---
re text;

BEGIN 


---- Сколько записей нашел поиск ---
SELECT INTO co count(*) FROM ps_abonent_list WHERE ps_ul like (ps_RusUpper(ul_)||'%') AND btrim(ps_dom)=btrim(dom_) AND btrim(ps_kv)=btrim(kv_) AND ps_rec_delete<>'delete';

---- Если запись единственная - делаем выборку данных ----
IF co=1 THEN

SELECT INTO re '<re><abonent><kod>'||ps_rec_id||'</kod><ul>'||ps_ul||'</ul><dom>'||ps_dom||'</dom><kv>'||ps_kv||'</kv><tel>'||ps_tel||'</tel><kon>'||ps_fio||'</kon><balans>'||ps_balans_total||'</balans><tplan>'||ps_tarif_plan||'</tplan></abonent></re>' FROM ps_abonent_list WHERE ps_ul like (ps_RusUpper(ul_)||'%') AND btrim(ps_dom)=btrim(dom_) AND btrim(ps_kv)=btrim(kv_) AND ps_rec_delete<>'delete';

RETURN re;

ELSE
---- Если запись не единственная либо вообще записей нет - то... ----
RETURN 'NORESULT';

END IF;

END;$BODY$

LANGUAGE 'plpgsql'



