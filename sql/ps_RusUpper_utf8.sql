CREATE FUNCTION ps_RusUpper(text) RETURNS text

AS $BODY$

DECLARE

---- Переменные -----

--- last_key ---
word_ ALIAS FOR $1;


BEGIN 


RETURN translate(word_,'абвгдеёжзийклмнопрстуфхцчшщьыъэюя','АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ');

END;$BODY$

LANGUAGE 'plpgsql'



