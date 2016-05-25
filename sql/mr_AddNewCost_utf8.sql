CREATE OR REPLACE FUNCTION mr_AddNewCost(int,date,numeric(10,2)) RETURNS text

AS $BODY$

--- Добавление новой цены материала ---


DECLARE

---- Переменные -----

-- Код материала --
mate_kod ALIAS FOR $1;

--- Дата начала действия цены ---
start_date ALIAS FOR $2;

--- Значение цены ---
mate_cost ALIAS FOR $3;

--- Вспомогательная переменная ----
n int;

--- Идентификатор строки ---
genk varchar(24);





BEGIN 


--- Проверка поступивших данных ---
IF mate_kod IS NULL OR start_date IS NULL OR mate_cost IS NULL OR mate_cost<=0.00 THEN
	RETURN 'ERRORDATA';
END IF;




--- Устанавливаемая дата не должна быть в прошлом ---
IF current_date>start_date THEN
	RETURN 'NOTACCESS';
END IF;


--- Есть ли уже такая дата для этого материала ---
SELECT INTO n count(*) FROM mr_mate_cost WHERE mr_rec_delete='' AND mr_mate_kod=mate_kod AND mr_date_start=start_date;
IF n!=0 THEN
	RETURN 'NOTACCESS';
END IF;
	


--- Определение идентификатора строки ---
--- Первоначально такой ключ существует ---
n:=1;
--- Получение уникального ключа ---
WHILE n<>0 LOOP
	genk:=ps_GenKey24();
	SELECT INTO n count(*) FROM mr_mate_cost WHERE mr_rec_id=genk;
END LOOP;


--- Добавление записи ---
INSERT INTO mr_mate_cost(mr_rec_id,mr_date_start,mr_mate_kod,mr_mate_cost) VALUES(genk,start_date,mate_kod,mate_cost);

RETURN 'OK';


END;$BODY$

LANGUAGE 'plpgsql';



