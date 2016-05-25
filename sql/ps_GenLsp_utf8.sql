CREATE OR REPLACE FUNCTION ps_GenLsp() 
        RETURNS varchar(8) 
        AS $BODY$

DECLARE
-- объявления переменных 

-- Номер лицевого счета по платежке ---
lsp varchar(8);

-- Вспомогательная переменная ---
n int2;


BEGIN
-- начальная инициализация 
n := 1;


-- Проверка есть ли уже такой номер лицевого счета ---
WHILE n<>0 LOOP

	lsp := substr(btrim(to_char(trunc(random()*999999999999+1),'9999999999999')),1,8);
	SELECT INTO n count(*) FROM ps_abonent_list WHERE ps_lsp=lsp;

END LOOP;




RETURN lsp; 
             END;$BODY$ 
LANGUAGE 'plpgsql';
