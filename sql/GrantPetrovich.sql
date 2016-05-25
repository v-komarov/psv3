GRANT SELECT,UPDATE,INSERT ON ps_abonent_list TO petrovich;
GRANT SELECT,UPDATE,INSERT ON ps_ls TO petrovich;
GRANT SELECT,UPDATE,INSERT ON ps_messages TO petrovich;
GRANT SELECT,UPDATE,INSERT ON ps_pay_in TO petrovich;
GRANT SELECT,UPDATE,INSERT ON ps_pay_out TO petrovich;
GRANT SELECT,UPDATE,INSERT ON ps_pay_in_other TO petrovich;
GRANT SELECT,UPDATE,INSERT ON ps_services TO petrovich;
GRANT SELECT,UPDATE,INSERT ON ps_tarif_plan TO petrovich;
GRANT SELECT,UPDATE,INSERT ON ps_tarif_plan_name TO petrovich;
GRANT SELECT,UPDATE,INSERT ON ps_uls TO petrovich;
GRANT SELECT,UPDATE,INSERT ON ps_loadpay_log TO petrovich;
GRANT SELECT,UPDATE,INSERT ON ps_loadpay3_log TO petrovich;


GRANT SELECT ON ps_show_abonent_list TO petrovich;
GRANT SELECT ON ps_show_abonent_off TO petrovich;
GRANT SELECT ON ps_show_abonent_service TO petrovich;
GRANT SELECT ON ps_show_check_in TO petrovich;
GRANT SELECT ON ps_show_check_in_other TO petrovich;
GRANT SELECT ON ps_show_messages TO petrovich;
GRANT SELECT ON ps_show_pay_in TO petrovich;
GRANT SELECT ON ps_show_pay_out TO petrovich;
GRANT SELECT ON ps_show_pay_in_other TO petrovich;
GRANT SELECT ON ps_show_service_list TO petrovich;
GRANT SELECT ON ps_show_status_service TO petrovich;
GRANT SELECT ON ps_show_tarif_plan TO petrovich;
GRANT SELECT ON ps_show_tarif_plan_name TO petrovich;
GRANT SELECT ON ps_show_uldom_list TO petrovich;
GRANT SELECT ON ps_show_task TO petrovich;
GRANT SELECT ON ps_show_loadpay TO petrovich;
GRANT SELECT ON ps_show_loadpay3 TO petrovich;
GRANT SELECT ON ps_show_report_pay_in TO petrovich;
GRANT SELECT ON ps_show_report_pay_in_other TO petrovich;
GRANT SELECT ON ps_show_report_abonent_service_dol_mes TO petrovich;



GRANT SELECT ON ps_kassa_list TO petrovich;

GRANT SELECT,UPDATE,INSERT ON in_account TO petrovich;
GRANT SELECT,UPDATE,INSERT ON in_mac_list TO petrovich;
GRANT SELECT,UPDATE,INSERT ON in_pay_traf TO petrovich;
GRANT SELECT,UPDATE,INSERT ON in_traf_cost TO petrovich;

GRANT SELECT ON in_show_login TO petrovich;
GRANT SELECT ON in_show_mac TO petrovich;
GRANT SELECT ON in_show_pay TO petrovich;
GRANT SELECT ON in_show_tarif TO petrovich;


GRANT SELECT ON sc_status TO petrovich;
GRANT SELECT,UPDATE,INSERT ON sc_task TO petrovich;
GRANT SELECT,UPDATE,INSERT ON sc_worker TO petrovich;
GRANT SELECT,UPDATE,INSERT ON sc_worker_list TO petrovich;

GRANT SELECT ON sc_show_status TO petrovich;
GRANT SELECT ON sc_show_task TO petrovich;
GRANT SELECT ON sc_show_task2 TO petrovich;
GRANT SELECT ON sc_show_task_noclose TO petrovich;
GRANT SELECT ON sc_show_worker TO petrovich;
GRANT SELECT ON sc_show_worker_list TO petrovich;
GRANT SELECT ON sc_show_worker_list2 TO petrovich;



GRANT SELECT,UPDATE,INSERT ON mr_group_list TO petrovich;
GRANT SELECT ON mr_store_list TO petrovich;
GRANT SELECT,UPDATE,INSERT ON mr_mate_list TO petrovich;
GRANT SELECT ON mr_show_mate TO petrovich;


GRANT SELECT,UPDATE,INSERT ON mr_mate_in TO petrovich;
GRANT SELECT,UPDATE,INSERT ON mr_mate_in_party TO petrovich;
GRANT SELECT,UPDATE,INSERT ON mr_story_q TO petrovich;
GRANT SELECT,UPDATE,INSERT ON mr_mate_out TO petrovich;
GRANT SELECT,UPDATE,INSERT ON mr_mate_out_party TO petrovich;
GRANT SELECT,UPDATE,INSERT ON mr_mate_cost TO petrovich;


GRANT SELECT ON mr_show_cost TO petrovich;
GRANT SELECT ON mr_show_mate_in TO petrovich;
GRANT SELECT ON mr_show_store_q TO petrovich;

GRANT SELECT,INSERT,UPDATE ON mr_mate_set_store TO petrovich;

GRANT SELECT ON mr_show_mate_set_store TO petrovich;

GRANT SELECT ON sc_show_worker2 TO petrovich;

GRANT SELECT ON sc_show_mate_store TO petrovich;
GRANT SELECT ON sc_show_mate TO petrovich;
GRANT SELECT ON mr_show_mate_page TO petrovich;

GRANT SELECT ON sc_show_task_p TO petrovich;
GRANT SELECT ON mr_show_mate_op TO petrovich;
GRANT SELECT ON mr_show_store_group_q TO petrovich;

GRANT SELECT ON mr_operation_list TO petrovich;
GRANT SELECT ON ps_show_mate TO petrovich;


GRANT SELECT,INSERT,UPDATE ON ps_loadpay2_log TO petrovich;

GRANT SELECT,INSERT,UPDATE,DELETE ON radcheck TO petrovich;
GRANT SELECT ON radacct TO petrovich;
GRANT ALL ON radcheck_id_seq TO petrovich;


GRANT SELECT ON mr_eds_list TO petrovich;
