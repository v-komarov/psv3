CREATE OR REPLACE FUNCTION ps_AddAbonent(varchar(20),varchar(5),varchar(4),varchar(16),varchar(40),varchar(30),varchar(3)) RETURNS text

AS 
$BODY$

DECLARE

---- Переменные -----

--- Улица ---
ul_ ALIAS FOR $1;

--- Дом ---
dom_ ALIAS FOR $2;

--- Квартира ---
kv_ ALIAS FOR $3;

--- Телефон ---
tel_ ALIAS FOR $4;

--- Контакт ---
fio_ ALIAS FOR $5;

--- Название тарифного плана ---
tp_  ALIAS FOR $6;

--- Номер подъезда ---
np ALIAS FOR $7;

--- Количество найденых совпадений ---
n int4;

--- Код тарифного плана ---
kod_tp varchar(24);

--- Сгенерированный ключ записи абонента ---
gen_key varchar(24);

--- Сгенерированный ключ записи лицевого счета ---
gen_key2 varchar(24);

--- Переменная для хранения промежуточных данных строк ---
row_data ps_tarif_plan%ROWTYPE;

--- Вспомогательные - длинна передаваемых строк номера дома и квартиры ---
nstrul int4;
nstrdom int4;
nstrkv int4;
nstrtp int4;


BEGIN

--- Проверка переданных значений номера дома и квартиры ----
nstrul:=char_length(btrim(ul_));
nstrdom:=char_length(btrim(dom_));
nstrkv:=char_length(btrim(kv_));
nstrtp:=char_length(btrim(tp_));


IF (nstrul>0 AND nstrdom>0 AND nstrkv>0 AND nstrtp>0) THEN

--- Проверка есть ли такая уже запись в таблице ---

SELECT INTO n count(*) FROM ps_abonent_list WHERE btrim(ps_ul)=btrim(ps_RusUpper(ul_)) AND btrim(ps_dom)=btrim(ps_RusUpper(dom_)) AND btrim(ps_kv)=btrim(kv_);


--- Если такого абонента нет - добавляем ---
IF n=0 THEN

--- Вычисление кода тарифного плана по названию ---
SELECT INTO kod_tp ps_rec_id FROM ps_tarif_plan_name WHERE btrim(ps_tarif_plan_name)=btrim(tp_);

--- Кенерация ключа записи абонента ---
gen_key:=ps_GenKeyCheck(1);

--- Добавление учетной записи абонента --- 
INSERT INTO ps_abonent_list(ps_rec_id,ps_ul,ps_dom,ps_kv,ps_tel,ps_fio,ps_tarif_plan,ps_lsp,ps_p) VALUES(gen_key,btrim(ps_RusUpper(ul_)),btrim(ps_RusUpper(dom_)),btrim(kv_),btrim(tel_),btrim(fio_),kod_tp, ps_GenLsp(),btrim(np));

--- Создание лицевых счетов по видам услуг на основании наполнения этими услугами тарифного плана ---
FOR row_data IN SELECT * FROM ps_tarif_plan WHERE ps_tarif_plan_kod=kod_tp LOOP

--- Кенерация ключа лицевого счета абонента ---
gen_key2:=ps_GenKeyCheck(5);
--- Добавление лицевых счетов ---
INSERT INTO ps_ls(ps_rec_id,ps_abonent_kod,ps_service_kod) VALUES(gen_key2,gen_key,row_data.ps_service_kod);

END LOOP;



--- Проверка INTERNET услуги абонента 7-11-2007 ---
---PERFORM in_CheckInternet(gen_key);




RETURN 'OK'||gen_key;

ELSE

RETURN 'CANT ADD THIS ABONENT';


END IF;

--- если значение дома или квартиры - строка нулейвой длинны ---
ELSE
RETURN 'ERROR IN DATA';
END IF;

END;$BODY$

LANGUAGE 'plpgsql'



