CREATE OR REPLACE FUNCTION sc_NewTask(varchar(20),varchar(5),varchar(4),timestamp) RETURNS text

AS $BODY$

DECLARE


---- Переменные -----

---- Адрес ---
ul_ ALIAS FOR $1;
dom_ ALIAS FOR $2;
kv_ ALIAS FOR $3;

--- Дата и время заявки ---
task_time ALIAS FOR $4;

--- вспомогательная переменная ---
n int2;

--- Код абонента ---
kod_ab varchar(24);

--- Полное название улицы ---
ul_name varchar(20);

--- Номер подъезда ---
p varchar(3);

--- Номер телефона ---
phone varchar(16);

--- Код заявки ---
genk varchar(24);


BEGIN 


--- Проверка поступивших данных на корректность ---
IF length(ul_)=0 OR length(dom_)=0 OR length(kv_)=0 THEN
	RETURN 'ERRORDATA';
END IF;



---- Поиск адреса ---
SELECT INTO n count(*) FROM ps_abonent_list WHERE ps_ul like (ps_RusUpper(ul_)||'%') AND btrim(ps_dom)=ps_RusUpper(btrim(dom_)) AND btrim(ps_kv)=btrim(kv_) AND ps_rec_delete<>'delete';

---- Адреса нет ----
IF n!=1 THEN
	RETURN 'ERRORDATA';
END IF;


---- Если такой адрес найден - определяем код записи ---
SELECT INTO kod_ab ps_rec_id FROM ps_abonent_list WHERE ps_ul like (ps_RusUpper(ul_)||'%') AND btrim(ps_dom)=ps_RusUpper(btrim(dom_)) AND btrim(ps_kv)=btrim(kv_) AND ps_rec_delete<>'delete';


---- Определение полного названия улицы, номера подъезда, номер телефона ----
SELECT INTO ul_name,phone,p ps_ul,ps_tel,ps_p FROM ps_abonent_list WHERE ps_rec_id=kod_ab;



--- Первоначально такой ключ существует ---
n:=1;
--- Получение уникального ключа ---
WHILE n<>0 LOOP
	genk:=ps_GenKey24();
	SELECT INTO n count(*) FROM sc_task WHERE sc_rec_id=genk;
END LOOP;


--- Добавление новой заявки ----
INSERT INTO sc_task (
sc_rec_id,
sc_plan_time,
sc_text_task,
sc_abonent_kod,
sc_ul,
sc_dom,
sc_kv,
sc_p,
sc_phone
)

VALUES(
genk,
task_time,
'NEW',
kod_ab,
ul_name,
ps_RusUpper(dom_),
kv_,
p,
phone
);


--- Возврат кода добавленной заявки ---
RETURN genk;



END;$BODY$

LANGUAGE 'plpgsql'



