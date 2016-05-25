CREATE FUNCTION in_LoadUserVPN(varchar(30),varchar(5),varchar(4),varchar(8)) RETURNS text


---- �������� ������ �� VPNBilling ������� Zope � VPNBilling ������� wxPython ---
---- �������� �� ����������� ������ ������������ � �������� ����� ����                     ---


AS '

DECLARE

---- ���������� -----

--- ����� � ����� �������� ---
ul ALIAS FOR $1;
--- ����� ���� � ����� �������� ---
dom ALIAS FOR $2;
--- ����� �������� � ����� �������� ---
kv ALIAS FOR $3;
--- ����� ������������ ---
login ALIAS FOR $4;

--- ��������� ������ �� ������ ---
n int2;

--- ��� �������� ---
kod_ps varchar(24);
kod_upd int4;

--- ������ � Internet ---
loginrad varchar(16);
passwd varchar(8);
tp_kod int4;


--- ���������� ��� �������� ������������� ����������� ���������� ������� ---
row_data upd_pay_1mes%ROWTYPE;
row_data2 upd_pay_traf%ROWTYPE;
row_data3 upd_pay_user%ROWTYPE;

--- ��� ������ Internet ---
kod_ser varchar(24);


--- ��� ������� ��������� ����� ---
kod_ptp varchar(24);


--- ��������������� ��� ����������� ������� �������� ����� ---
ls_ok int2;


--- ������� ����� �� ������� ����� ---
internet_ost numeric(8,2);


--- ����� ������ ---
balans numeric(10,2);


--- ������� �������� ---
tel varchar(30);


BEGIN


--- ����� � ����������� ���� ������� ��������� ����� ---
SELECT INTO n count(*) FROM ps_tarif_plan_name WHERE btrim(ps_tarif_plan_name)=\'������\';

IF n!=1 THEN
RETURN \'CANT FIND ������ �������� ����\';
ELSE
--- ����������� ���� ��������� ����� ---
SELECT INTO kod_ptp ps_rec_id FROM ps_tarif_plan_name WHERE btrim(ps_tarif_plan_name)=\'������\';
END IF;



--- ����� ������ INTERNET ---
SELECT INTO n count(*) FROM ps_services WHERE btrim(ps_services_name)=\'INTERNET\';

IF n!=1 THEN
RETURN \'CANT FIND INTERNET SERVICE\';
ELSE
--- ����������� ���� ������ ---
SELECT INTO kod_ser ps_rec_id FROM ps_services WHERE btrim(ps_services_name)=\'INTERNET\';
END IF;


--- ����� ������ �� ������ ---
SELECT INTO n count(*) FROM ps_abonent_list WHERE btrim(ps_ul)=btrim(ul) AND btrim(ps_dom)=btrim(dom) AND btrim(ps_kv)=btrim(kv);

IF n!=1 THEN
RETURN \'CANT FIND ABONENT ADDRESS\';
END IF;

SELECT INTO n count(*) FROM upd_user_list WHERE btrim(rad_login)=btrim(login);

IF n!=1 THEN
RETURN \'CANT FIND ABONENT LOGIN\';
END IF;


--- ����������� ���� �������� ---
SELECT INTO kod_ps ps_rec_id FROM ps_abonent_list WHERE btrim(ps_ul)=btrim(ul) AND btrim(ps_dom)=btrim(dom) AND btrim(ps_kv)=btrim(kv);
SELECT INTO kod_upd id_user_upd FROM upd_user_list WHERE btrim(rad_login)=btrim(login);


--- ������� ����������� ����������� ����� ---
FOR row_data IN SELECT * FROM upd_pay_1mes WHERE id_user_upd=kod_upd LOOP
	INSERT INTO ps_pay_out(ps_rec_id,ps_data,ps_abonent_kod,ps_tarif_plan_kod,ps_service_kod,ps_service_cost,ps_balans_before,ps_balans_after,ps_info) VALUES(ps_GenKeyCheck(7),row_data.date_opl,kod_ps,kod_ptp,kod_ser,row_data.pay_1mes,0,0,\'�������\');
END LOOP;


--- ������� ��������� �� ������ ---
FOR row_data2 IN SELECT * FROM upd_pay_traf WHERE id_user=kod_upd LOOP
	INSERT INTO in_pay_traf(in_rec_abonent,in_date_time,in_sum,in_sum_before,in_sum_after,in_traf,in_traf_cost) VALUES(kod_ps,row_data2.date_pay,row_data2.sum_pay,0,0,row_data2.traf_mb,row_data2.t_plan);
END LOOP;


--- ������� �������� �������� ---
FOR row_data3 IN SELECT * FROM upd_pay_user WHERE id_user_upd=kod_upd LOOP
	INSERT INTO ps_pay_in(ps_rec_id,ps_data,ps_abonent_kod,ps_tarif_plan_kod,ps_service_kod,ps_service_sum,ps_balans_before,ps_balans_after,ps_info) VALUES(ps_GenKeyCheck(6),row_data3.date_op,kod_ps,kod_ptp,kod_ser,row_data3.pay_rub,0,0,\'�������\');
END LOOP;


--- ����������� ������� ������ � ������ ---
SELECT INTO loginrad btrim(rad_login) FROM upd_user_list WHERE id_user_upd=kod_upd;
SELECT INTO passwd btrim(rad_pass) FROM upd_user_list WHERE id_user_upd=kod_upd;
--- ����������� �������� ������ �� ������ ---
SELECT INTO tp_kod tplan FROM upd_user_list WHERE id_user_upd=kod_upd;


--- ������� ������� � ������� ������� � ���� Internet ---
INSERT INTO in_account(in_rec_id,in_user_login,in_user_passwd,in_cost_kod,in_rec_delete) VALUES(kod_ps,loginrad,passwd,tp_kod,\'delete\');


--- �������� ���� �� ������� ���� INTERNET ��� �������� ---
SELECT INTO ls_ok count(*) FROM ps_ls WHERE ps_abonent_kod=kod_ps AND ps_service_kod=kod_ser;
--- ���������� ������������ �������� ����� ---
IF ls_ok=0 THEN
INSERT INTO ps_ls(ps_rec_id,ps_abonent_kod,ps_service_kod) VALUES(ps_GenKeyCheck(5),kod_ps,kod_ser);
END IF;


--- ������� ������� �� ������� ����� �� ������ INTERNET ---
SELECT INTO internet_ost ls_user FROM upd_user_list WHERE id_user_upd=kod_upd;
UPDATE ps_ls SET ps_ls_sum=internet_ost WHERE ps_abonent_kod=kod_ps AND ps_service_kod=kod_ser;
--- ���������� ������ ������� ---
SELECT INTO balans sum(ps_ls_sum) FROM ps_ls WHERE ps_abonent_kod=kod_ps;
UPDATE ps_abonent_list SET ps_balans_total=balans WHERE ps_rec_id=kod_ps;
--- ������� ��������� �������� ---
SELECT INTO tel kt_user FROM upd_user_list WHERE id_user_upd=kod_upd;
UPDATE ps_abonent_list SET ps_tel=substr(btrim(tel),0,17) WHERE ps_rec_id=kod_ps;



RETURN \'OK\';

END;'

LANGUAGE 'plpgsql'






