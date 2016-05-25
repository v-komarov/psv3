CREATE OR REPLACE FUNCTION ps_EditAbonent(varchar(24),varchar(20),varchar(5),varchar(4),varchar(16),varchar(40),varchar(30),varchar(3)) RETURNS text

AS 
$BODY$

DECLARE

---- Переменные -----

--- Идентификатор стоки ---
kod_rec ALIAS FOR $1;

--- Улица ---
ul_ ALIAS FOR $2;

--- Дом ---
dom_ ALIAS FOR $3;

--- Квартира ---
kv_ ALIAS FOR $4;

--- Телефон ---
tel_ ALIAS FOR $5;

--- Контакт ---
fio_ ALIAS FOR $6;

--- Название тарифного плана ---
tp_  ALIAS FOR $7;

--- Номер подъезда ---
np ALIAS FOR $8;

--- Количество найденых совпадений ---
n int4;

--- Количество найденых совпадений ---
a int4;

--- current_user ---
usr varchar(20);


--- Код тарифного плана ---
kod_tp_new varchar(24);
kod_tp_old varchar(24);

--- Переменная для хранения промежуточных данных строк ---
row_data ps_tarif_plan%ROWTYPE;



BEGIN



--- Проверка переданных значений номера дома и квартиры ----
IF length(btrim(ul_))=0 OR length(btrim(dom_))=0 OR length(btrim(kv_))=0 OR length(btrim(tp_))=0 THEN
	RETURN 'ERROR IN DATA';
END IF;




--- Проверка есть ли такая уже запись в таблице - с тем же адресом ---
SELECT INTO n count(*) FROM ps_abonent_list WHERE ps_rec_id<>kod_rec AND btrim(ps_ul)=btrim(ul_) AND btrim(ps_dom)=btrim(ps_RusUpper(dom_)) AND btrim(ps_kv)=btrim(kv_);
IF n!=0 THEN
	RETURN 'CANT UPDATE THIS ABONENT';
END IF;



--- Пользователь ----
SELECT INTO usr current_user;


--- Изменение учетной записи абонента кроме тарифного плана --- 
IF usr='operatortspk' OR usr='operatortspk2' OR usr='operatortspk3' THEN
    UPDATE ps_abonent_list SET ps_tel=btrim(tel_), ps_fio=btrim(fio_), ps_p=btrim(np) WHERE ps_rec_id=kod_rec;
ELSE
    UPDATE ps_abonent_list SET ps_ul=btrim(ul_), ps_dom=btrim(ps_RusUpper(dom_)), ps_kv=btrim(kv_), ps_tel=btrim(tel_), ps_fio=btrim(fio_), ps_p=btrim(np) WHERE ps_rec_id=kod_rec;
END IF;

--- Определение кодов тарифных планов ---
SELECT INTO kod_tp_old ps_tarif_plan FROM ps_abonent_list WHERE ps_rec_id=kod_rec;
SELECT INTO kod_tp_new ps_rec_id FROM ps_tarif_plan_name WHERE btrim(ps_tarif_plan_name)=btrim(tp_);


--- Если тарифный план меняется в форме, то ...
IF kod_tp_old!=kod_tp_new THEN
	--- Изменение кода тарифного плана в учетной записи абонента ---
	UPDATE ps_abonent_list SET ps_tarif_plan=kod_tp_new WHERE ps_rec_id=kod_rec;
	--- Создание лицевых счетов по видам услуг на основании наполнения этими услугами тарифного плана ---
	FOR row_data IN SELECT * FROM ps_tarif_plan WHERE ps_tarif_plan_kod=kod_tp_new LOOP
		--- Проверка существует ли уже лицевой счет ---
		SELECT INTO a count(*) FROM ps_ls WHERE ps_abonent_kod=kod_rec AND ps_service_kod=row_data.ps_service_kod;
		--- Если необходимого лицевого счета нет - добавление --
		IF a=0 THEN
			--- Добавление лицевых счетов ---
			INSERT INTO ps_ls(ps_rec_id,ps_abonent_kod,ps_service_kod)   VALUES(ps_GenKeyCheck(5),kod_rec,row_data.ps_service_kod);
		END IF;
	END LOOP;
END IF;




--- Проверка INTERNET услуги абонента 7-11-2007 ---
---PERFORM in_CheckInternet(kod_rec);



--- Успешное завершение ---
RETURN 'OK';




END;$BODY$

LANGUAGE 'plpgsql';



