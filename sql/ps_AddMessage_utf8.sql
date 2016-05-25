CREATE FUNCTION ps_AddMessage(varchar(24),varchar(70)) RETURNS text

AS 

$BODY$

DECLARE

---- Переменные -----

-- Код абонента - идентификатор строки ---
kod_ab ALIAS FOR $1;

-- Заметка --
mess_ ALIAS FOR $2;

-- Обрезано в заметке лишнее ---
mess_cut varchar(70);



BEGIN 


-- Усечение стоки, удаление лишних пробелов ---
mess_cut := substr(btrim(mess_),1,69);

-- Добавление заметки ---
INSERT INTO ps_messages(ps_rec_id,ps_abonent_kod,ps_mess_txt) VALUES(ps_GenKeyCheck(8),kod_ab,mess_cut);


RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql'






