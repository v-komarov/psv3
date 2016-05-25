CREATE OR REPLACE FUNCTION in_changeuserlock()
  RETURNS "trigger" AS
$BODY$


/*

	Функция создает или удаляет учетную запись в таблице Radius сервера
	в зависимости от значения полей учетной записи Internet в ps
	Выполняется при каждом обновлении (UPDATE) строки таблицы in_account

*/



DECLARE

---- Переменные -----




BEGIN 



-- Проверка по полю in_rec_delete ---            
IF NEW.in_rec_delete = 'delete' THEN
--- Абонент аблокирован поэтому удалется его учетная запись из radcheck ---
    DELETE FROM radcheck WHERE btrim(username)=btrim(NEW.in_user_login);


ELSE
--- Абонент разблокирован, либо поменялись данные, например пароль ---
    DELETE FROM radcheck WHERE btrim(username)=btrim(NEW.in_user_login);
    INSERT INTO radcheck(username,attribute,value) VALUES(btrim(NEW.in_user_login),'Password',btrim(NEW.in_user_passwd)); 
END IF;



RETURN NEW;

END;$BODY$
  LANGUAGE 'plpgsql' VOLATILE;
