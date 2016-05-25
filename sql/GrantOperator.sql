GRANT SELECT,UPDATE,INSERT ON ps_abonent_list TO operatortspk;
GRANT SELECT,UPDATE,INSERT ON ps_ls TO operatortspk;
GRANT SELECT,UPDATE,INSERT ON ps_messages TO operatortspk;
GRANT SELECT,UPDATE,INSERT ON ps_pay_in TO operatortspk;
GRANT SELECT,UPDATE,INSERT ON ps_pay_out TO operatortspk;
GRANT SELECT,UPDATE,INSERT ON ps_pay_in_other TO operatortspk;
GRANT SELECT,UPDATE,INSERT ON ps_services TO operatortspk;
GRANT SELECT,UPDATE,INSERT ON ps_tarif_plan TO operatortspk;
GRANT SELECT,UPDATE,INSERT ON ps_tarif_plan_name TO operatortspk;
GRANT SELECT,UPDATE,INSERT ON ps_uls TO operatortspk;
GRANT SELECT,UPDATE,INSERT ON ps_loadpay_log TO operatortspk;


GRANT SELECT ON ps_show_abonent_list TO operatortspk;
GRANT SELECT ON ps_show_abonent_off TO operatortspk;
GRANT SELECT ON ps_show_abonent_service TO operatortspk;
GRANT SELECT ON ps_show_check_in TO operatortspk;
GRANT SELECT ON ps_show_check_in_other TO operatortspk;
GRANT SELECT ON ps_show_messages TO operatortspk;
GRANT SELECT ON ps_show_pay_in TO operatortspk;
GRANT SELECT ON ps_show_pay_out TO operatortspk;
GRANT SELECT ON ps_show_pay_in_other TO operatortspk;
GRANT SELECT ON ps_show_service_list TO operatortspk;
GRANT SELECT ON ps_show_status_service TO operatortspk;
GRANT SELECT ON ps_show_tarif_plan TO operatortspk;
GRANT SELECT ON ps_show_tarif_plan_name TO operatortspk;
GRANT SELECT ON ps_show_uldom_list TO operatortspk;
GRANT SELECT ON ps_show_task TO operatortspk;
GRANT SELECT ON ps_show_loadpay TO operatortspk;
GRANT SELECT ON ps_show_report_pay_in TO operatortspk;
GRANT SELECT ON ps_show_report_pay_in_other TO operatortspk;
GRANT SELECT ON ps_show_report_abonent_service_dol_mes TO operatortspk;



GRANT SELECT ON ps_kassa_list TO operatortspk;

GRANT SELECT,UPDATE,INSERT ON in_account TO operatortspk;
GRANT SELECT,UPDATE,INSERT ON in_mac_list TO operatortspk;
GRANT SELECT,UPDATE,INSERT ON in_pay_traf TO operatortspk;
GRANT SELECT,UPDATE,INSERT ON in_traf_cost TO operatortspk;

GRANT SELECT ON in_show_login TO operatortspk;
GRANT SELECT ON in_show_mac TO operatortspk;
GRANT SELECT ON in_show_pay TO operatortspk;
GRANT SELECT ON in_show_tarif TO operatortspk;


GRANT SELECT ON sc_status TO operatortspk;
GRANT SELECT,UPDATE,INSERT ON sc_task TO operatortspk;
GRANT SELECT,UPDATE,INSERT ON sc_worker TO operatortspk;
GRANT SELECT,UPDATE,INSERT ON sc_worker_list TO operatortspk;

GRANT SELECT ON sc_show_status TO operatortspk;
GRANT SELECT ON sc_show_task TO operatortspk;
GRANT SELECT ON sc_show_task2 TO operatortspk;
GRANT SELECT ON sc_show_task_noclose TO operatortspk;
GRANT SELECT ON sc_show_worker TO operatortspk;
GRANT SELECT ON sc_show_worker_list TO operatortspk;
GRANT SELECT ON sc_show_worker_list2 TO operatortspk;

GRANT SELECT ON sc_show_worker2 TO operatortspk;
GRANT SELECT ON sc_show_mate TO operatortspk;

GRANT SELECT ON sc_show_task_p TO operatortspk;
GRANT SELECT ON ps_show_mate TO operatortspk;


GRANT SELECT,INSERT,UPDATE ON ps_loadpay2_log TO operatortspk;


GRANT SELECT,INSERT,UPDATE,DELETE ON radcheck TO operatortspk;
GRANT SELECT ON radacct TO operatortspk;
GRANT ALL ON radcheck_id_seq TO operatortspk;
