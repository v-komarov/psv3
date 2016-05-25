CREATE OR REPLACE FUNCTION ps_FindLsp(varchar(8)) RETURNS text

AS 
$BODY$

/*

	Осуществляет поиск абонента по номеру лицевого счета по системе "Платежка"

*/

DECLARE


---- Переменные -----

---- Передаваемый номер лицевого счета ---
lsp ALIAS FOR $1;

--- Количество найденых записей ---
n int4;

--- Строка с результатом ---
re text;

BEGIN 


---- Сколько записей нашел поиск ---
SELECT INTO n count(*) FROM ps_abonent_list WHERE ps_lsp=lsp AND ps_rec_delete<>'delete';

---- Если запись единственная - делаем выборку данных ----
IF n=1 THEN

SELECT INTO re ps_rec_id FROM ps_abonent_list WHERE ps_lsp=lsp AND ps_rec_delete<>'delete';

RETURN re;

ELSE
---- Если запись не единственная либо вообще записей нет - то... ----
RETURN 'NORESULT';

END IF;

END;$BODY$

LANGUAGE 'plpgsql'



