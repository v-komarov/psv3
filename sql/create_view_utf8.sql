CREATE VIEW ps_show_abonent_list AS 
SELECT 
ps_abonent_list.ps_rec_id, 
ps_ul, 
ps_dom, 
ps_kv, 
to_char(ps_balans_total,'99990.99'), 
ps_tel, ps_fio, 
ps_tarif_plan_name.ps_tarif_plan_name, 
to_number(ps_kv,'9999') as ps_kv_order, 
ps_lsp as lsp, ps_p as p
FROM 
ps_abonent_list, 
ps_tarif_plan_name
WHERE 
ps_abonent_list.ps_rec_delete<>'delete' and 
ps_tarif_plan=ps_tarif_plan_name.ps_rec_id
ORDER BY ps_ul, ps_dom, ps_kv_order;


CREATE VIEW ps_show_tarif_plan_name AS 
SELECT 
ps_rec_id, 
ps_tarif_plan_name
FROM 
ps_tarif_plan_name
WHERE 
ps_rec_delete<>'delete'
ORDER BY ps_tarif_plan_name;


CREATE VIEW ps_show_tarif_plan AS 
SELECT 
ps_tarif_plan.ps_rec_id, 
ps_tarif_plan_name.ps_tarif_plan_name, 
ps_services.ps_services_name, 
to_char(ps_tarif_plan.ps_cost,'99990.99'), 
ps_showtypecount(ps_tarif_plan.ps_type_count)
FROM 
ps_tarif_plan, 
ps_tarif_plan_name, 
ps_services
WHERE 
ps_tarif_plan.ps_rec_delete<>'delete' and 
ps_tarif_plan_name.ps_rec_id=ps_tarif_plan.ps_tarif_plan_kod and 
ps_services.ps_rec_id=ps_tarif_plan.ps_service_kod
ORDER BY 2,3;


CREATE OR REPLACE VIEW ps_show_pay_in AS  
SELECT 
ps_pay_in.ps_rec_id, 
to_char(ps_pay_in.ps_data,'DD.MM.YYYY') as data, 
ps_pay_in.ps_abonent_kod, 
btrim(ps_tarif_plan_name.ps_tarif_plan_name) as tplan, 
btrim(ps_services.ps_services_name) as service, 
to_char(ps_pay_in.ps_service_sum,'99990.99') as sum, 
to_char(ps_pay_in.ps_balans_before,'99990.99') as before, 
to_char(ps_pay_in.ps_balans_after,'99990.99') as after, 
btrim(ps_pay_in.ps_info) as info, ps_pay_in.ps_data as data2,
ps_kassa_list.ps_kassa_name AS kassa
FROM 
ps_pay_in, 
ps_services, 
ps_tarif_plan_name,
ps_kassa_list
WHERE 
ps_pay_in.ps_tarif_plan_kod=ps_tarif_plan_name.ps_rec_id AND 
ps_pay_in.ps_service_kod=ps_services.ps_rec_id AND 
ps_pay_in.ps_rec_delete<>'delete' AND
ps_pay_in.ps_kassa_kod=ps_kassa_list.ps_rec_id
ORDER BY 10 DESC
;



CREATE VIEW ps_show_pay_out AS 
SELECT 
ps_pay_out.ps_rec_id, 
to_char(ps_pay_out.ps_data,'DD.MM.YYYY') as data, 
ps_pay_out.ps_abonent_kod, btrim(ps_tarif_plan_name.ps_tarif_plan_name) as tplan, 
btrim(ps_services.ps_services_name) as service, 
to_char(ps_pay_out.ps_service_cost,'99990.99') as sum, 
to_char(ps_pay_out.ps_balans_before,'99990.99') as before, 
to_char(ps_pay_out.ps_balans_after,'99990.99') as after, 
btrim(ps_pay_out.ps_info) as info, 
ps_pay_out.ps_data as data2
FROM 
ps_pay_out, ps_services, 
ps_tarif_plan_name
WHERE 
ps_pay_out.ps_tarif_plan_kod=ps_tarif_plan_name.ps_rec_id AND 
ps_pay_out.ps_service_kod=ps_services.ps_rec_id AND 
ps_pay_out.ps_rec_delete<>'delete'
ORDER BY 10 DESC;



CREATE VIEW ps_show_abonent_service AS 
SELECT 
ps_abonent_list.ps_rec_id, 
ps_abonent_list.ps_ul, 
ps_abonent_list.ps_dom, 
ps_abonent_list.ps_kv, 
ps_abonent_list.ps_balans_total,  
ps_tarif_plan_name.ps_tarif_plan_name, 
ps_abonent_list.ps_tarif_plan as kodtp, 
ps_services.ps_services_name, 
ps_tarif_plan.ps_service_kod as kodser,
ps_tarif_plan.ps_type_count,
ps_tarif_plan.ps_cost,
ps_ls.ps_ls_sum,
to_number(ps_kv,'9999') as ps_kv_order,
ps_abonent_list.ps_p as ps_p



FROM ps_abonent_list, ps_tarif_plan_name, ps_tarif_plan, ps_services, ps_ls

WHERE 
ps_abonent_list.ps_rec_delete<>'delete' AND 
ps_abonent_list.ps_tarif_plan=ps_tarif_plan_name.ps_rec_id AND 
ps_abonent_list.ps_tarif_plan=ps_tarif_plan.ps_tarif_plan_kod AND
ps_tarif_plan.ps_rec_delete<>'delete' AND
ps_tarif_plan.ps_service_kod=ps_services.ps_rec_id AND
ps_ls.ps_abonent_kod=ps_abonent_list.ps_rec_id AND
ps_ls.ps_service_kod=ps_tarif_plan.ps_service_kod
ORDER BY 2,3,ps_kv_order,8;




CREATE VIEW ps_show_service_list AS 
SELECT ps_services_name
FROM ps_services
WHERE ps_rec_delete<>'delete';


CREATE OR REPLACE VIEW ps_show_messages AS 
SELECT  
ps_rec_id, to_char(ps_data,'DD.MM.YYYY') as ps_data, 
ps_abonent_kod, ps_mess_txt, ps_data as data2
FROM ps_messages
WHERE  ps_rec_delete<>'delete'
ORDER BY data2 DESC;


CREATE OR REPLACE VIEW ps_show_pay_in_other AS 
SELECT  
ps_rec_id, to_char(ps_data,'DD.MM.YYYY') as ps_data, ps_abonent_kod, 
ps_about, to_char(ps_sum,'99990.99') as ps_sum, ps_info, ps_data as data2
FROM ps_pay_in_other
WHERE  ps_rec_delete<>'delete'
ORDER BY data2 DESC;


CREATE VIEW ps_show_status_service AS 
SELECT 
ps_ls.ps_rec_id,  
ps_ls.ps_abonent_kod as abonent_kod, 
ps_services.ps_services_name as service_name, 
ps_ls.ps_service_kod as service_kod, 
to_char(ps_ls.ps_ls_sum,'99990.99') as sum  
FROM ps_ls, ps_services
WHERE ps_ls.ps_service_kod=ps_services.ps_rec_id
ORDER BY 2,3;


CREATE VIEW ps_show_uldom_list AS 
SELECT DISTINCT 
ps_abonent_list.ps_ul, 
ps_abonent_list.ps_dom
FROM ps_abonent_list
WHERE 
ps_abonent_list.ps_rec_delete<>'delete' 
ORDER BY 1,2;




CREATE VIEW ps_show_abonent_off AS 
SELECT 
ps_abonent_list.ps_ul, 
ps_abonent_list.ps_dom, 
ps_abonent_list.ps_kv, 
ps_services.ps_services_name, 
ps_ls.ps_ls_sum as balans,
to_number(ps_kv,'9999') as ps_kv_order


FROM ps_abonent_list, ps_services, ps_ls

WHERE 
ps_abonent_list.ps_rec_delete<>'delete' AND 
ps_abonent_list.ps_rec_id=ps_ls.ps_abonent_kod AND 
ps_ls.ps_service_kod=ps_services.ps_rec_id AND
ps_abonent_list.ps_rec_id||ps_ls.ps_service_kod NOT IN
(SELECT ps_abonent_list.ps_rec_id||ps_tarif_plan.ps_service_kod FROM ps_abonent_list, ps_tarif_plan WHERE ps_abonent_list.ps_tarif_plan=ps_tarif_plan_kod AND ps_abonent_list.ps_rec_delete<>'delete' AND ps_tarif_plan.ps_rec_delete<>'delete')
ORDER BY 1,2,ps_kv_order,6;



CREATE OR REPLACE VIEW ps_show_check_in AS 
SELECT 
i.ps_abonent_kod,
s.ps_services_name,
t.ps_cost,
i.ps_service_sum,
i.ps_info

FROM 
ps_pay_in i, 
ps_services s, 
ps_tarif_plan t

WHERE 
i.ps_rec_delete<>'delete' AND 
date_trunc('day',i.ps_data)=date_trunc('day',now()) AND
i.ps_service_kod=s.ps_rec_id AND
i.ps_tarif_plan_kod=t.ps_tarif_plan_kod AND i.ps_service_kod=t.ps_service_kod
;



CREATE VIEW ps_show_check_in_other AS 
SELECT
ps_abonent_kod, 
ps_about,
ps_sum

FROM ps_pay_in_other 

WHERE 
ps_rec_delete<>'delete' AND 
date_trunc('day',ps_data)=date_trunc('day',now())
;



CREATE VIEW ps_show_task AS 
SELECT 
a.ps_rec_id AS abonent_id,
t.sc_rec_id AS task_id,
t.sc_plan_time AS sc_plan_time,
to_char(t.sc_plan_time,'DD.MM.YYYY') AS plan_date,
to_char(t.sc_plan_time,'HH24:MI') AS plan_time,
s.sc_status AS status,
t.sc_type_task AS type_task,
t.sc_text_task AS text_task,
t.sc_ul AS ul,
t.sc_dom AS dom,
t.sc_kv AS kv,
t.sc_p AS p,
t.sc_phone AS phone,
t.sc_task_note AS task_note
FROM 
sc_task t,
sc_status s,
ps_abonent_list a
WHERE
t.sc_rec_delete!='delete' AND
t.sc_status_task=s.sc_rec_id AND
btrim(a.ps_ul)=btrim(t.sc_ul) AND
btrim(a.ps_dom)=btrim(t.sc_dom) AND
btrim(a.ps_kv)=btrim(t.sc_kv)
ORDER BY t.sc_plan_time DESC;



CREATE OR REPLACE VIEW ps_show_loadpay AS
SELECT
ps_date_pay AS date_pay,
ps_date_load AS date_load,
to_char(ps_date_pay,'DD.MM.YYYY') AS date_pay_str,
to_char(ps_date_load,'DD.MM.YYYY') AS date_load_str,
ps_lsp AS lsp,
CASE 
WHEN ps_service_kod='' THEN ''
ELSE (SELECT ps_services_name FROM ps_services WHERE ps_rec_id=ps_service_kod)
END AS service_name,
CASE WHEN ps_sum IS NULL THEN 0
ELSE ps_sum
END AS sum_pay,
btrim(to_char(ps_sum,'99999999.00')) AS sum_pay_str,
ps_error AS load_error,
ps_ok AS load_ok 
FROM
ps_loadpay_log
ORDER BY ps_date_pay,ps_lsp;


CREATE OR REPLACE VIEW ps_show_loadpay3 AS
SELECT
ps_date_pay AS date_pay,
ps_date_load AS date_load,
to_char(ps_date_pay,'DD.MM.YYYY') AS date_pay_str,
to_char(ps_date_load,'DD.MM.YYYY') AS date_load_str,
ps_lsp AS lsp,
CASE 
WHEN ps_service_kod='' THEN ''
ELSE (SELECT ps_services_name FROM ps_services WHERE ps_rec_id=ps_service_kod)
END AS service_name,
CASE WHEN ps_sum IS NULL THEN 0
ELSE ps_sum
END AS sum_pay,
btrim(to_char(ps_sum,'99999999.00')) AS sum_pay_str,
ps_error AS load_error,
ps_ok AS load_ok 
FROM
ps_loadpay3_log
ORDER BY ps_date_pay,ps_lsp;




CREATE OR REPLACE VIEW ps_show_loadpay4 AS
SELECT
ps_date_pay AS date_pay,
ps_date_load AS date_load,
to_char(ps_date_pay,'DD.MM.YYYY') AS date_pay_str,
to_char(ps_date_load,'DD.MM.YYYY') AS date_load_str,
ps_lsp AS lsp,
CASE 
WHEN ps_service_kod='' THEN ''
ELSE (SELECT ps_services_name FROM ps_services WHERE ps_rec_id=ps_service_kod)
END AS service_name,
CASE WHEN ps_sum IS NULL THEN 0
ELSE ps_sum
END AS sum_pay,
btrim(to_char(ps_sum,'99999999.00')) AS sum_pay_str,
ps_error AS load_error,
ps_ok AS load_ok 
FROM
ps_loadpay4_log
ORDER BY ps_date_pay,ps_lsp;




CREATE VIEW  in_show_tarif  AS 
SELECT  
in_rec_id, 
btrim(in_cost_name) as cost_name,  
btrim(to_char(in_cost_1mb,'9990.00')) as cost_1mb
FROM in_traf_cost
WHERE  in_rec_delete<>'delete' 
ORDER BY 2;


CREATE VIEW  in_show_login  AS 
SELECT  
in_account.in_rec_id,
ps_ul,ps_dom,ps_kv,
ps_tel,in_cost_name,
in_user_login,
in_ip_client, 
date_trunc('second',in_last_time)
FROM 
ps_abonent_list, 
in_account,
in_traf_cost
WHERE ps_abonent_list.ps_rec_id=in_account.in_rec_id AND
in_account.in_cost_kod=in_traf_cost.in_rec_id AND 
in_account.in_rec_delete<>'delete' 
ORDER BY 2,3,4;


CREATE VIEW  in_show_pay  AS 
SELECT  
in_rec_abonent,
in_date_time, 
to_char(in_date_time,'DD.MM.YYYY') as fdate, 
to_char(in_date_time,'HH24:MI') as ftime, 
in_sum, 
in_sum_before, 
in_sum_after, 
in_traf, 
in_cost_name
FROM 
in_pay_traf, 
in_traf_cost
WHERE 
in_pay_traf.in_traf_cost=in_traf_cost.in_rec_id AND 
in_pay_traf.in_rec_delete<>'delete' 
ORDER  BY 2 DESC;


CREATE VIEW  in_show_mac  AS 
SELECT 
in_rec_id, 
in_abonent_kod, 
in_type, in_mac 
FROM in_mac_list
WHERE in_rec_delete<>'delete' 
ORDER  BY 3 DESC;



CREATE VIEW sc_show_task AS 
SELECT 
t.sc_rec_id AS rec_id,
t.sc_plan_time AS sc_plan_time,
to_char(t.sc_plan_time,'DD.MM.YYYY') AS plan_date,
to_char(t.sc_plan_time,'HH24:MI') AS plan_time,
date_part('year',t.sc_plan_time) AS plan_year,
date_part('month',t.sc_plan_time) AS plan_month,
date_part('day',t.sc_plan_time) AS plan_day,
s.sc_status AS status,
t.sc_type_task AS type_task,
t.sc_text_task AS text_task,
t.sc_ul AS ul,
t.sc_dom AS dom,
t.sc_kv AS kv,
t.sc_p AS p,
t.sc_phone AS phone,
t.sc_plan_chch AS plan_chch,
t.sc_plan_workers AS plan_workers,
t.sc_fact_chch AS fact_chch,
t.sc_task_note AS task_note,
to_char(t.sc_create_time,'DD.MM.YYYY HH24.MI') AS create_time
FROM 
sc_task t,
sc_status s
WHERE
t.sc_rec_delete!='delete' AND
t.sc_status_task=s.sc_rec_id
ORDER BY t.sc_plan_time;




CREATE VIEW sc_show_task2 AS 
SELECT 
t.sc_rec_id AS rec_id,
t.sc_plan_time AS sc_plan_time,
to_char(t.sc_plan_time,'DD.MM.YYYY') AS plan_date,
to_char(t.sc_plan_time,'HH24:MI') AS plan_time,
date_part('year',t.sc_plan_time) AS plan_year,
date_part('month',t.sc_plan_time) AS plan_month,
date_part('day',t.sc_plan_time) AS plan_day,
s.sc_status AS status,
t.sc_type_task AS type_task,
t.sc_text_task AS text_task,
t.sc_ul AS ul,
t.sc_dom AS dom,
t.sc_kv AS kv,
t.sc_p AS p,
t.sc_phone AS phone,
t.sc_plan_chch AS plan_chch,
t.sc_plan_workers AS plan_workers,
t.sc_fact_chch AS fact_chch,
t.sc_task_note AS task_note,
to_char(t.sc_create_time,'DD.MM.YYYY HH24.MI') AS create_time,
t.sc_rec_delete AS rec_delete,
t.sc_status_task AS status_kod,
to_char(t.sc_date_task_close,'DD.MM.YYYY HH24.MI') AS close_time
FROM 
sc_task t,
sc_status s
WHERE
t.sc_status_task=s.sc_rec_id
ORDER BY t.sc_plan_time;






CREATE VIEW  sc_show_worker AS 
SELECT 
w.sc_task_kod AS task_kod,
l.sc_name_1||' '||l.sc_name_2||' '||l.sc_name_3 AS fio
FROM 
sc_worker w,
sc_worker_list l
WHERE 
w.sc_rec_delete!='delete' AND
w.sc_worker_kod=l.sc_rec_id;



CREATE VIEW  sc_show_worker_list AS 
SELECT  
sc_rec_id, 
btrim(sc_name_1)||' '||btrim(sc_name_2)||' '||btrim(sc_name_3) as worker_name 
FROM sc_worker_list 
WHERE  sc_rec_delete<>'delete' 
ORDER BY 2;


CREATE VIEW  sc_show_worker_list2 AS 
SELECT  
sc_rec_id, 
sc_name_1, 
sc_name_2, 
sc_name_3 
FROM sc_worker_list
WHERE  sc_rec_delete<>'delete' 
ORDER BY 2,3,4;


CREATE VIEW  sc_show_status AS 
SELECT  sc_rec_id,sc_status
FROM sc_status
WHERE  sc_rec_delete<>'delete' 
ORDER BY 2;



CREATE VIEW sc_show_task_noclose AS 
SELECT 
t.sc_rec_id AS rec_id,
t.sc_plan_time AS sc_plan_time,
to_char(t.sc_plan_time,'DD.MM.YYYY') AS plan_date,
to_char(t.sc_plan_time,'HH24:MI') AS plan_time,
date_part('year',t.sc_plan_time) AS plan_year,
date_part('month',t.sc_plan_time) AS plan_month,
date_part('day',t.sc_plan_time) AS plan_day,
s.sc_status AS status,
t.sc_type_task AS type_task,
t.sc_text_task AS text_task,
t.sc_ul AS ul,
t.sc_dom AS dom,
t.sc_kv AS kv,
t.sc_p AS p,
t.sc_phone AS phone,
t.sc_plan_chch AS plan_chch,
t.sc_plan_workers AS plan_workers,
t.sc_fact_chch AS fact_chch,
t.sc_task_note AS task_note
FROM 
sc_task t,
sc_status s
WHERE
t.sc_rec_delete!='delete' AND
t.sc_status_task=s.sc_rec_id AND
t.sc_status_task!=1
ORDER BY t.sc_plan_time DESC;




CREATE VIEW web_show_service_balans AS 
SELECT 
a.ps_ul AS ul,
a.ps_dom AS dom,
a.ps_kv AS kv,
a.ps_lsp AS lsp,
l.ps_service_kod AS service_kod,
s.ps_services_name AS service_name,
l.ps_ls_sum AS balans 
FROM 
ps_abonent_list a,
ps_ls l,
ps_services s,
ps_tarif_plan t
WHERE a.ps_rec_delete!='delete' AND
a.ps_rec_id=l.ps_abonent_kod AND
l.ps_service_kod=s.ps_rec_id AND
a.ps_tarif_plan=t.ps_tarif_plan_kod AND
t.ps_rec_delete!='delete' AND
l.ps_service_kod=t.ps_service_kod
ORDER BY 6;





CREATE VIEW web_show_pay_in AS 
SELECT 
a.ps_ul AS ul,
a.ps_dom AS dom,
a.ps_kv AS kv,
a.ps_lsp AS lsp,
i.ps_service_kod AS service_kod,
s.ps_services_name AS service_name,
i.ps_data AS ps_data,
to_char(i.ps_data,'DD.MM.YYYY') AS strdata,
i.ps_service_sum AS service_sum,
i.ps_balans_before AS balans_before,
i.ps_balans_after AS balans_after
FROM 
ps_abonent_list a,
ps_pay_in i,
ps_services s
WHERE a.ps_rec_delete!='delete' AND
a.ps_rec_id=i.ps_abonent_kod AND
i.ps_service_kod=s.ps_rec_id AND
i.ps_rec_delete!='delete' AND
date_part('year',i.ps_data)=date_part('year',now())
ORDER BY i.ps_data DESC;





CREATE VIEW web_show_pay_out AS 
SELECT 
a.ps_ul AS ul,
a.ps_dom AS dom,
a.ps_kv AS kv,
a.ps_lsp AS lsp,
o.ps_service_kod AS service_kod,
s.ps_services_name AS service_name,
o.ps_data AS ps_data,
to_char(o.ps_data,'DD.MM.YYYY') AS strdata,
o.ps_service_cost AS service_cost,
o.ps_balans_before AS balans_before,
o.ps_balans_after AS balans_after
FROM 
ps_abonent_list a,
ps_pay_out o,
ps_services s
WHERE a.ps_rec_delete!='delete' AND
a.ps_rec_id=o.ps_abonent_kod AND
o.ps_service_kod=s.ps_rec_id AND
o.ps_rec_delete!='delete' AND
date_part('year',o.ps_data)=date_part('year',now())
ORDER BY o.ps_data DESC;





CREATE VIEW web_show_pay_traf AS 
SELECT 
a.ps_ul AS ul,
a.ps_dom AS dom,
a.ps_kv AS kv,
a.ps_lsp AS lsp,
i.in_date_time AS in_date_time,
to_char(i.in_date_time,'DD.MM.YYYY') AS strdata,
to_char(i.in_date_time,'HH24.MI') AS strtime,
i.in_sum AS sum,
i.in_sum_before AS balans_before,
i.in_sum_after AS balans_after
FROM 
ps_abonent_list a,
in_pay_traf i
WHERE 
a.ps_rec_delete!='delete' AND
a.ps_rec_id=i.in_rec_abonent AND
i.in_rec_delete!='delete' AND
date_part('year',i.in_date_time)=date_part('year',now())
ORDER BY i.in_date_time DESC;




CREATE VIEW  upd_show_pay_traf AS 

SELECT  
upd_pay_traf.date_pay, 
 to_char(upd_pay_traf.date_pay,'DD.MM.YYYY') as date_char,
upd_pay_traf.sum_pay,
upd_pay_traf.traf_mb,
upd_user_list.address_user

FROM 
upd_user_list, 
upd_pay_traf

WHERE 
upd_pay_traf.id_user = upd_user_list.id_user_upd AND 
upd_user_list.abonent_del=0

ORDER BY 1 DESC;





CREATE OR REPLACE VIEW mac_internet AS
SELECT btrim(m.in_mac)
FROM
in_mac_list m,
ps_ls l,
ps_abonent_list a,
ps_tarif_plan t,
ps_services s
WHERE
m.in_rec_delete<>'delete' AND
m.in_type=1 AND
m.in_abonent_kod=a.ps_rec_id AND
a.ps_rec_delete<>'delete' AND
a.ps_tarif_plan=t.ps_tarif_plan_kod AND
t.ps_rec_delete<>'delete' AND
t.ps_service_kod=s.ps_rec_id AND
s.ps_rec_delete<>'delete' AND
btrim(s.ps_services_name)='INTERNET UNLIM' AND
l.ps_abonent_kod=a.ps_rec_id AND
l.ps_service_kod=t.ps_service_kod AND
l.ps_ls_sum>=0;




--- Для отчета поступлений ---
CREATE OR REPLACE VIEW ps_show_report_pay_in AS
SELECT 
substr(a.ps_ul,1,20) AS ul,
a.ps_dom AS dom,
a.ps_kv AS kv, 
i.ps_data AS date_pay,
to_char(i.ps_data,'DD.MM.YYYY') AS date_pay_str,
s.ps_services_name AS service_name,
k.ps_kassa_name AS kassa_name,
i.ps_service_sum AS sum_pay,
btrim(to_char(i.ps_service_sum,'99999990.00')) AS sum_pay_str
FROM 
ps_pay_in i,
ps_abonent_list a,
ps_services s,
ps_kassa_list k
WHERE
i.ps_rec_delete='' AND
i.ps_abonent_kod=a.ps_rec_id AND
i.ps_service_kod=s.ps_rec_id AND
i.ps_kassa_kod=k.ps_rec_id
ORDER BY i.ps_data,a.ps_ul,a.ps_dom,a.ps_kv;




--- Для отчета поступлений ---
CREATE OR REPLACE VIEW ps_show_report_pay_in_other AS
SELECT 
substr(a.ps_ul,1,20) AS ul,
a.ps_dom AS dom,
a.ps_kv AS kv,
i.ps_data AS date_pay,
to_char(i.ps_data,'DD.MM.YYYY') AS date_pay_str,
substr(i.ps_about,1,20) AS about,
i.ps_sum AS sum_pay,
btrim(to_char(i.ps_sum,'999999.00')) AS sum_pay_str
FROM 
ps_pay_in_other i,
ps_abonent_list a
WHERE
i.ps_rec_delete='' AND
i.ps_abonent_kod=a.ps_rec_id
ORDER BY i.ps_data,a.ps_ul,a.ps_dom,a.ps_kv;




--- Для отчетов по должникам и печати объявлений ---
CREATE OR REPLACE VIEW ps_show_report_abonent_service_dol_mes AS
SELECT 
a.ps_rec_id AS rec_id, 
a.ps_ul AS ul, 
a.ps_dom AS dom, 
a.ps_kv AS kv, 
a.ps_balans_total AS balans_total,
btrim(to_char(a.ps_balans_total,'999999990.00')) AS balans_total_str,
tn.ps_tarif_plan_name AS tarif_plan_name, 
s.ps_services_name AS service_name, 
t.ps_cost AS cost,
btrim(to_char(t.ps_cost,'9999990.00')) AS cost_str,
ls.ps_ls_sum AS ls_sum,
btrim(to_char(ls.ps_ls_sum,'9999990.00')) AS ls_sum_str,
btrim(to_char(abs(ls.ps_ls_sum),'9999990.00')) AS ls_sum_str_abs,
CASE WHEN t.ps_cost=0 THEN 0
ELSE floor(abs(ls.ps_ls_sum)/t.ps_cost)
END AS dol_mes,
CASE WHEN t.ps_cost=0 THEN '-'
ELSE btrim(to_char(floor(abs(ls.ps_ls_sum)/t.ps_cost),'990'))
END AS dol_mes_str,
a.ps_p AS p
FROM 
ps_abonent_list a, 
ps_tarif_plan_name tn, 
ps_tarif_plan t, 
ps_services s, 
ps_ls ls
WHERE 
a.ps_rec_delete<>'delete' AND 
a.ps_tarif_plan=tn.ps_rec_id AND 
a.ps_tarif_plan=t.ps_tarif_plan_kod AND
t.ps_rec_delete<>'delete' AND
t.ps_service_kod=s.ps_rec_id AND
ls.ps_abonent_kod=a.ps_rec_id AND
ls.ps_service_kod=t.ps_service_kod AND
ls.ps_ls_sum<0
ORDER BY a.ps_ul,a.ps_dom,to_number(a.ps_kv,'999')
;




--- Для справочника материалов ---
CREATE OR REPLACE VIEW mr_show_mate AS
SELECT
btrim(to_char(m.mr_rec_id,'99990')) AS rec_id_str,
m.mr_mate_name AS mate_name,
e.mr_eds_name AS eds_name,
e.mr_eds_name_shot AS eds_name_shot,
g.mr_group_name AS group_name
FROM
mr_mate_list m,
mr_group_list g,
mr_eds_list e
WHERE
m.mr_rec_delete='' AND
m.mr_eds_kod=e.mr_rec_id AND
m.mr_group_kod=g.mr_rec_id
ORDER BY m.mr_mate_name
;



--- Для отображение списка цен в закладке материала ---
CREATE OR REPLACE VIEW mr_show_cost AS
SELECT
c.mr_rec_id AS rec_id,
to_char(c.mr_date_start,'DD.MM.YYYY') AS date_start,
e.mr_eds_name AS eds_name,
btrim(to_char(c.mr_mate_cost,'99999990.00')) AS mate_cost,
c.mr_mate_kod AS mate_kod
FROM 
mr_mate_cost c,
mr_eds_list e,
mr_mate_list m
WHERE
c.mr_rec_delete='' AND
c.mr_mate_kod=m.mr_rec_id AND
m.mr_eds_kod=e.mr_rec_id
ORDER BY c.mr_date_start DESC;



--- Для отображение списка закладке поступлений ---
CREATE OR REPLACE VIEW mr_show_mate_in AS
SELECT
i.mr_rec_id AS rec_id,
to_char(i.mr_create_time,'DD.MM.YYYY') AS date_in,
s.mr_store_name AS store_name,
e.mr_eds_name AS eds_name,
btrim(to_char(i.mr_mate_q,'9999990.00')) AS mate_q,
btrim(to_char(i.mr_mate_cost,'9999990.00')) AS mate_cost,
btrim(to_char(i.mr_mate_q*i.mr_mate_cost,'99999990.00')) AS mate_sum,
i.mr_mate_kod AS mate_kod
FROM
mr_mate_in i,
mr_store_list s,
mr_eds_list e
WHERE
i.mr_rec_delete='' AND
i.mr_store_kod=s.mr_rec_id AND
i.mr_eds_kod=e.mr_rec_id
ORDER BY i.mr_create_time DESC;



--- Для отображение списка закладке наличие ---
CREATE OR REPLACE VIEW mr_show_store_q AS
SELECT
s.mr_store_name AS store_name,
e.mr_eds_name AS eds_name,
btrim(to_char(sum(p.mr_mate_q),'9999990.00')) AS mate_q,
p.mr_mate_kod AS mate_kod
FROM 
mr_mate_in_party p,
mr_store_list s,
mr_eds_list e
WHERE
p.mr_rec_delete='' AND
p.mr_store_kod=s.mr_rec_id AND
p.mr_eds_kod=e.mr_rec_id
GROUP BY s.mr_store_name,e.mr_eds_name,p.mr_mate_kod
ORDER BY s.mr_store_name,e.mr_eds_name,p.mr_mate_kod;



--- Для отображение списка закладке ввод остатков ---
CREATE OR REPLACE VIEW mr_show_mate_set_store AS
SELECT
i.mr_rec_id AS rec_id,
to_char(i.mr_create_time,'DD.MM.YYYY') AS date_in,
s.mr_store_name AS store_name,
e.mr_eds_name AS eds_name,
btrim(to_char(i.mr_mate_q,'9999990.00')) AS mate_q,
btrim(to_char(i.mr_mate_cost,'9999990.00')) AS mate_cost,
btrim(to_char(i.mr_mate_q*i.mr_mate_cost,'99999990.00')) AS mate_sum,
i.mr_mate_kod AS mate_kod
FROM
mr_mate_set_store i,
mr_store_list s,
mr_eds_list e
WHERE
i.mr_rec_delete='' AND
i.mr_store_kod=s.mr_rec_id AND
i.mr_eds_kod=e.mr_rec_id
ORDER BY i.mr_create_time DESC;




--- Для отображения исполнителей в заявке ---
CREATE VIEW  sc_show_worker2 AS 
SELECT 
w.sc_rec_id AS rec_id,
w.sc_task_kod AS task_kod,
l.sc_name_1 AS name_1,
l.sc_name_2 AS name_2,
l.sc_name_3 AS name_3
FROM 
sc_worker w,
sc_worker_list l
WHERE 
w.sc_rec_delete='' AND
w.sc_worker_kod=l.sc_rec_id
ORDER BY l.sc_name_1,l.sc_name_2
;




--- Для выбора материала в заявке ---
CREATE VIEW  sc_show_mate_store AS 
SELECT
btrim(to_char(p.mr_store_kod,'99990'))||'#'||btrim(to_char(p.mr_mate_kod,'99990')) AS rec_id,
m.mr_mate_name AS mate_name,
e.mr_eds_name_shot AS eds_name,
sum(p.mr_mate_q) AS mate_q,
btrim(to_char(sum(p.mr_mate_q),'99999990.00')) AS mate_q_str,
(SELECT
c.mr_mate_cost
FROM
mr_mate_cost c
WHERE
c.mr_date_start<=current_date AND c.mr_mate_kod=p.mr_mate_kod
ORDER BY c.mr_date_start DESC
LIMIT 1
) AS mate_cost,
btrim(to_char((SELECT
c.mr_mate_cost
FROM
mr_mate_cost c
WHERE
c.mr_date_start<=current_date AND c.mr_mate_kod=p.mr_mate_kod
ORDER BY c.mr_date_start DESC
LIMIT 1
),'999999.00')) AS mate_cost_str,
s.mr_store_name AS store_name,
g.mr_group_name AS group_name
FROM
mr_mate_in_party p,
mr_store_list s,
mr_mate_list m,
mr_group_list g,
mr_eds_list e
WHERE
p.mr_rec_delete='' AND
p.mr_store_kod=s.mr_rec_id AND
p.mr_mate_q!=0.00 AND
p.mr_mate_kod=m.mr_rec_id AND
m.mr_group_kod=g.mr_rec_id AND
p.mr_eds_kod=e.mr_rec_id
GROUP BY
btrim(to_char(p.mr_store_kod,'99990'))||'#'||btrim(to_char(p.mr_mate_kod,'99990')),
m.mr_mate_name,
e.mr_eds_name_shot,
s.mr_store_name,
g.mr_group_name,
(SELECT
c.mr_mate_cost
FROM
mr_mate_cost c
WHERE
c.mr_date_start<=current_date AND c.mr_mate_kod=p.mr_mate_kod
ORDER BY c.mr_date_start DESC
LIMIT 1
),
btrim(to_char((SELECT
c.mr_mate_cost
FROM
mr_mate_cost c
WHERE
c.mr_date_start<=current_date AND c.mr_mate_kod=p.mr_mate_kod
ORDER BY c.mr_date_start DESC
LIMIT 1
),'999999.00'))
ORDER BY
btrim(to_char(p.mr_store_kod,'99990'))||'#'||btrim(to_char(p.mr_mate_kod,'99990')),
m.mr_mate_name,
e.mr_eds_name_shot,
s.mr_store_name,
g.mr_group_name,
(SELECT
c.mr_mate_cost
FROM
mr_mate_cost c
WHERE
c.mr_date_start<=current_date AND c.mr_mate_kod=p.mr_mate_kod
ORDER BY c.mr_date_start DESC
LIMIT 1
),
btrim(to_char((SELECT
c.mr_mate_cost
FROM
mr_mate_cost c
WHERE
c.mr_date_start<=current_date AND c.mr_mate_kod=p.mr_mate_kod
ORDER BY c.mr_date_start DESC
LIMIT 1
),'999999.00'))
;




--- Для отображения расхода материала в заявке ---
CREATE VIEW  sc_show_mate AS 
SELECT 
o.mr_rec_id AS rec_id,
o.mr_task_kod AS task_kod,
m.mr_mate_name AS mate_name,
e.mr_eds_name_shot AS eds_name,
btrim(to_char(o.mr_mate_q,'99999990.00')) AS mate_q,
btrim(to_char(o.mr_abonent_cost,'99999990.00')) AS abonent_cost,
btrim(to_char(o.mr_mate_q*o.mr_abonent_cost,'9999999990.00')) AS mate_sum
FROM
mr_mate_out o,
mr_mate_list m,
mr_eds_list e
WHERE
o.mr_rec_delete='' AND
o.mr_mate_kod=m.mr_rec_id AND
o.mr_eds_kod=e.mr_rec_id
ORDER BY m.mr_mate_name;




--- Вид расхода по заявком для отображения в карточке материала ---
CREATE VIEW  mr_show_mate_page AS 
SELECT
o.mr_mate_kod AS mate_kod,
to_char(t.sc_plan_time,'DD.MM.YYYY HH24:MI'),
t.sc_text_task AS text_task,
e.mr_eds_name_shot AS eds_name,
btrim(to_char(o.mr_mate_q,'9999990.00')) AS mate_q,
btrim(to_char(o.mr_abonent_cost,'9999990.00')) AS abonent_cost,
btrim(to_char(o.mr_mate_q*o.mr_abonent_cost,'9999990.00')) AS mate_sum,
t.sc_ul AS ul,
t.sc_dom AS dom,
t.sc_p AS p,
t.sc_kv AS kv
FROM
sc_task t,
mr_mate_out o,
mr_eds_list e
WHERE
t.sc_rec_delete='' AND
t.sc_rec_id=o.mr_task_kod AND
o.mr_rec_delete='' AND
o.mr_eds_kod=e.mr_rec_id
ORDER BY sc_date_task_open DESC;




CREATE OR REPLACE VIEW  sc_show_task_p AS 
SELECT DISTINCT
sc_ul||'#'||sc_dom||'#'||sc_p AS rec_id,
sc_ul AS ul,
sc_dom AS dom,
sc_p AS p,
to_number(sc_dom,'999') AS dom_n
FROM sc_task 
WHERE
sc_abonent_kod=repeat('0',24) AND
btrim(sc_p) != ''
ORDER BY sc_ul,to_number(sc_dom,'999'),sc_p
;



--- Движение материала по операциям ---
CREATE OR REPLACE VIEW  mr_show_mate_op AS 
SELECT
to_char(q.mr_create_time,'DD.MM.YYYY') AS create_time_str,
o.mr_operation_name AS operation_name,
e.mr_eds_name_shot AS eds_name,
btrim(to_char(q.mr_mate_q,'999999990.00')) AS mate_q,
q.mr_mate_kod AS mate_kod,
s.mr_store_name AS store_name,
date_trunc('day',q.mr_create_time) AS create_time,
CASE WHEN q.mr_operation_kod=4 OR q.mr_operation_kod=4 THEN
substr((SELECT t.sc_text_task FROM sc_task t, mr_mate_out m WHERE q.mr_master_kod=m.mr_rec_id AND m.mr_task_kod=t.sc_rec_id),1,20)
ELSE ''
END AS task_name,
CASE WHEN q.mr_operation_kod=4 OR q.mr_operation_kod=4 THEN
substr((SELECT t.sc_ul FROM sc_task t, mr_mate_out m WHERE q.mr_master_kod=m.mr_rec_id AND m.mr_task_kod=t.sc_rec_id),1,20)
ELSE ''
END AS task_ul,
CASE WHEN q.mr_operation_kod=4 OR q.mr_operation_kod=4 THEN
substr((SELECT t.sc_dom FROM sc_task t, mr_mate_out m WHERE q.mr_master_kod=m.mr_rec_id AND m.mr_task_kod=t.sc_rec_id),1,20)
ELSE ''
END AS task_dom,
CASE WHEN q.mr_operation_kod=4 OR q.mr_operation_kod=4 THEN
substr((SELECT t.sc_kv FROM sc_task t, mr_mate_out m WHERE q.mr_master_kod=m.mr_rec_id AND m.mr_task_kod=t.sc_rec_id),1,20)
ELSE ''
END AS task_kv,
CASE WHEN q.mr_operation_kod=4 OR q.mr_operation_kod=4 THEN
substr((SELECT t.sc_p FROM sc_task t, mr_mate_out m WHERE q.mr_master_kod=m.mr_rec_id AND m.mr_task_kod=t.sc_rec_id),1,20)
ELSE ''
END AS task_p
FROM 
mr_story_q q,
mr_store_list s,
mr_operation_list o,
mr_eds_list e
WHERE
q.mr_rec_delete='' AND
q.mr_operation_kod=o.mr_rec_id AND
q.mr_eds_kod=e.mr_rec_id AND
q.mr_store_kod=s.mr_rec_id
ORDER BY q.mr_create_time
;




--- Остатки материалов на складе (по группам) ---
CREATE VIEW  mr_show_store_group_q AS 
SELECT 
m.mr_mate_name AS mate_name,
e.mr_eds_name_shot AS eds_name,
sum(p.mr_mate_q) AS mate_q,
btrim(to_char(sum(p.mr_mate_q),'999999990.00')) AS mate_q_str,
g.mr_group_name AS group_name,
s.mr_store_name AS store_name
FROM
mr_mate_in_party p,
mr_mate_list m,
mr_group_list g,
mr_eds_list e,
mr_store_list s
WHERE
p.mr_rec_delete='' AND
p.mr_mate_kod=m.mr_rec_id AND
p.mr_eds_kod=e.mr_rec_id AND
m.mr_group_kod=g.mr_rec_id AND
p.mr_store_kod=s.mr_rec_id AND
p.mr_mate_q!=0.00
GROUP BY m.mr_mate_name,e.mr_eds_name_shot,g.mr_group_name,s.mr_store_name
ORDER BY m.mr_mate_name,e.mr_eds_name_shot,g.mr_group_name,s.mr_store_name
;





--- Для отображения расхода материала в карточке абонентов ---
CREATE VIEW  ps_show_mate AS 
SELECT 
t.sc_abonent_kod AS abonent_kod,
to_char(t.sc_date_task_open,'DD.MM.YYYY') AS date_open,
m.mr_mate_name AS mate_name,
e.mr_eds_name_shot AS eds_name,
btrim(to_char(o.mr_mate_q,'99999990.00')) AS mate_q,
btrim(to_char(o.mr_abonent_cost,'99999990.00')) AS abonent_cost,
btrim(to_char(o.mr_mate_q*o.mr_abonent_cost,'9999999990.00')) AS mate_sum
FROM
mr_mate_out o,
mr_mate_list m,
mr_eds_list e,
sc_task t
WHERE
o.mr_rec_delete='' AND
o.mr_mate_kod=m.mr_rec_id AND
o.mr_eds_kod=e.mr_rec_id AND
o.mr_task_kod=t.sc_rec_id AND
t.sc_abonent_kod!=repeat('0',24)
ORDER BY t.sc_date_task_open DESC;

