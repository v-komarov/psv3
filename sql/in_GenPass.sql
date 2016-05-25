CREATE FUNCTION in_GenPass() RETURNS text

AS '

DECLARE


Password varchar(24); 
i int2;
j int2;
tmp int2;
Symbol varchar(1);


BEGIN 
-- начальная инициализация
i:=1;
Password=\'\';
-- цикл добавления случайных символов 
WHILE i <= 8 LOOP  
			
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
-- добавление случайного символа к паролю
Password:=Password||Symbol;
-- нарастание счетчика цикла i
i := i + 1;
END LOOP;  
-- возврат результата
RETURN Password; 




END;'

LANGUAGE 'plpgsql'






