CREATE FUNCTION in_LoadUserVPN(varchar(30),varchar(5),varchar(4),varchar(8)) RETURNS text


---- Загрузка данных из VPNBilling вариант Zope в VPNBilling вариант wxPython ---
---- работает по перемещению данных пользователя в пределах одной базы                     ---


AS '

DECLARE

---- Переменные -----

--- Улиуа в новой редакции ---
ul ALIAS FOR $1;
--- Номер дома в новой редакции ---
dom ALIAS FOR $2;
--- Номер квартиры в новой редакции ---
kv ALIAS FOR $3;
--- Логин пользователя ---
login ALIAS FOR $4;

--- Результат поиска по адресу ---
n int2;

--- Код абонента ---
kod_ps varchar(24);
kod_upd int4;

--- Доступ к Internet ---
loginrad varchar(16);
passwd varchar(8);
tp_kod int4;


--- Переменные для хранения промежуточных результатов построчной выборки ---
row_data upd_pay_1mes%ROWTYPE;
row_data2 upd_pay_traf%ROWTYPE;
row_data3 upd_pay_user%ROWTYPE;

--- Код услуги Internet ---
kod_ser varchar(24);


--- Код пустого тарифного плана ---
kod_ptp varchar(24);


--- Вспомогательная для определения наличия лицевого счета ---
ls_ok int2;


--- Остаток суммы на лицевом счете ---
internet_ost numeric(8,2);


--- Общий баланс ---
balans numeric(10,2);


--- Телефон абонента ---
tel varchar(30);


BEGIN


--- Поиск и определение кода ПУСТОГО тарифного плана ---
SELECT INTO n count(*) FROM ps_tarif_plan_name WHERE btrim(ps_tarif_plan_name)=\'ПУСТОЙ\';

IF n!=1 THEN
RETURN \'CANT FIND ПУСТОЙ ТАРИФНЫЙ ПЛАН\';
ELSE
--- Определение кода тарифного плана ---
SELECT INTO kod_ptp ps_rec_id FROM ps_tarif_plan_name WHERE btrim(ps_tarif_plan_name)=\'ПУСТОЙ\';
END IF;



--- Поиск услуги INTERNET ---
SELECT INTO n count(*) FROM ps_services WHERE btrim(ps_services_name)=\'INTERNET\';

IF n!=1 THEN
RETURN \'CANT FIND INTERNET SERVICE\';
ELSE
--- Определение кода услуги ---
SELECT INTO kod_ser ps_rec_id FROM ps_services WHERE btrim(ps_services_name)=\'INTERNET\';
END IF;


--- Поиск записи по адресу ---
SELECT INTO n count(*) FROM ps_abonent_list WHERE btrim(ps_ul)=btrim(ul) AND btrim(ps_dom)=btrim(dom) AND btrim(ps_kv)=btrim(kv);

IF n!=1 THEN
RETURN \'CANT FIND ABONENT ADDRESS\';
END IF;

SELECT INTO n count(*) FROM upd_user_list WHERE btrim(rad_login)=btrim(login);

IF n!=1 THEN
RETURN \'CANT FIND ABONENT LOGIN\';
END IF;


--- Определение кода абонента ---
SELECT INTO kod_ps ps_rec_id FROM ps_abonent_list WHERE btrim(ps_ul)=btrim(ul) AND btrim(ps_dom)=btrim(dom) AND btrim(ps_kv)=btrim(kv);
SELECT INTO kod_upd id_user_upd FROM upd_user_list WHERE btrim(rad_login)=btrim(login);


--- Перенос ежемесячной абонентской платы ---
FOR row_data IN SELECT * FROM upd_pay_1mes WHERE id_user_upd=kod_upd LOOP
	INSERT INTO ps_pay_out(ps_rec_id,ps_data,ps_abonent_kod,ps_tarif_plan_kod,ps_service_kod,ps_service_cost,ps_balans_before,ps_balans_after,ps_info) VALUES(ps_GenKeyCheck(7),row_data.date_opl,kod_ps,kod_ptp,kod_ser,row_data.pay_1mes,0,0,\'ПЕРЕНОС\');
END LOOP;


--- Перенос удержаний за трафик ---
FOR row_data2 IN SELECT * FROM upd_pay_traf WHERE id_user=kod_upd LOOP
	INSERT INTO in_pay_traf(in_rec_abonent,in_date_time,in_sum,in_sum_before,in_sum_after,in_traf,in_traf_cost) VALUES(kod_ps,row_data2.date_pay,row_data2.sum_pay,0,0,row_data2.traf_mb,row_data2.t_plan);
END LOOP;


--- Перенос платежей абонента ---
FOR row_data3 IN SELECT * FROM upd_pay_user WHERE id_user_upd=kod_upd LOOP
	INSERT INTO ps_pay_in(ps_rec_id,ps_data,ps_abonent_kod,ps_tarif_plan_kod,ps_service_kod,ps_service_sum,ps_balans_before,ps_balans_after,ps_info) VALUES(ps_GenKeyCheck(6),row_data3.date_op,kod_ps,kod_ptp,kod_ser,row_data3.pay_rub,0,0,\'ПЕРЕНОС\');
END LOOP;


--- Определение текущих логина и пароля ---
SELECT INTO loginrad btrim(rad_login) FROM upd_user_list WHERE id_user_upd=kod_upd;
SELECT INTO passwd btrim(rad_pass) FROM upd_user_list WHERE id_user_upd=kod_upd;
--- Определение текущего тарифа за трафик ---
SELECT INTO tp_kod tplan FROM upd_user_list WHERE id_user_upd=kod_upd;


--- Перенос логинов и паролей доступа к сети Internet ---
INSERT INTO in_account(in_rec_id,in_user_login,in_user_passwd,in_cost_kod,in_rec_delete) VALUES(kod_ps,loginrad,passwd,tp_kod,\'delete\');


--- Проверка есть ли лицевой счет INTERNET для абонента ---
SELECT INTO ls_ok count(*) FROM ps_ls WHERE ps_abonent_kod=kod_ps AND ps_service_kod=kod_ser;
--- Добавление необходимого лицевого счета ---
IF ls_ok=0 THEN
INSERT INTO ps_ls(ps_rec_id,ps_abonent_kod,ps_service_kod) VALUES(ps_GenKeyCheck(5),kod_ps,kod_ser);
END IF;


--- Перенос остатка на лицевом счете по услуге INTERNET ---
SELECT INTO internet_ost ls_user FROM upd_user_list WHERE id_user_upd=kod_upd;
UPDATE ps_ls SET ps_ls_sum=internet_ost WHERE ps_abonent_kod=kod_ps AND ps_service_kod=kod_ser;
--- Перерасчет общего баланса ---
SELECT INTO balans sum(ps_ls_sum) FROM ps_ls WHERE ps_abonent_kod=kod_ps;
UPDATE ps_abonent_list SET ps_balans_total=balans WHERE ps_rec_id=kod_ps;
--- Перенос телефонов абонента ---
SELECT INTO tel kt_user FROM upd_user_list WHERE id_user_upd=kod_upd;
UPDATE ps_abonent_list SET ps_tel=substr(btrim(tel),0,17) WHERE ps_rec_id=kod_ps;



RETURN \'OK\';

END;'

LANGUAGE 'plpgsql'






