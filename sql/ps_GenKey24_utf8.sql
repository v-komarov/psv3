CREATE OR REPLACE FUNCTION ps_GenKey24() 
        RETURNS varchar(24) 
        AS $BODY$
DECLARE
-- объявления переменных 
           	SessionKey varchar(24); 
		LengthOfKey integer;
		i integer;
j integer;
		tmp integer;
		Symbol varchar(1);
            BEGIN
-- начальная инициализация 
		i:=1;
		-- Создание численной части ключа функцией current_timestamp
SessionKey := to_char(current_timestamp,'MISSMSSSSSUS');
		LengthOfKey:=length(SessionKey);
		-- цикл добавления случайных символов
WHILE i <= (24-LengthOfKey) LOOP  
			-- выборка случайных чисел из интервалов {48-57},{65-90},{97-122}
j:=trunc(random()*3+1);
			if j=1 then
				tmp:=trunc(random()*9+48);
			else
				if j=2 then
					tmp:=trunc(random()*25+65);
				else
					tmp:=trunc(random()*25+97);
				end if;
			end if;
			-- получение случайного символа функцией chr()
Symbol:=chr(tmp);
-- добавление случайного символа
SessionKey:=SessionKey||Symbol;
			i := i + 1;
		END LOOP;  
			-- возврат результата
                RETURN SessionKey; 
             END;$BODY$ 
LANGUAGE 'plpgsql';
