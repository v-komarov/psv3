GRANT SELECT ON ps_abonent_list TO operatortspk2;
GRANT SELECT ON ps_ls TO operatortspk2;
GRANT SELECT ON ps_messages TO operatortspk2;
GRANT SELECT ON ps_pay_in TO operatortspk2;
GRANT SELECT ON ps_pay_out TO operatortspk2;
GRANT SELECT ON ps_pay_in_other TO operatortspk2;
GRANT SELECT ON ps_services TO operatortspk2;
GRANT SELECT ON ps_tarif_plan TO operatortspk2;
GRANT SELECT ON ps_tarif_plan_name TO operatortspk2;
GRANT SELECT ON ps_uls TO operatortspk2;

GRANT SELECT ON ps_show_abonent_list TO operatortspk2;
GRANT SELECT ON ps_show_abonent_off TO operatortspk2;
GRANT SELECT ON ps_show_abonent_service TO operatortspk2;
GRANT SELECT ON ps_show_check_in TO operatortspk2;
GRANT SELECT ON ps_show_check_in_other TO operatortspk2;
GRANT SELECT ON ps_show_messages TO operatortspk2;
GRANT SELECT ON ps_show_pay_in TO operatortspk2;
GRANT SELECT ON ps_show_pay_out TO operatortspk2;
GRANT SELECT ON ps_show_pay_in_other TO operatortspk2;
GRANT SELECT ON ps_show_service_list TO operatortspk2;
GRANT SELECT ON ps_show_status_service TO operatortspk2;
GRANT SELECT ON ps_show_tarif_plan TO operatortspk2;
GRANT SELECT ON ps_show_tarif_plan_name TO operatortspk2;
GRANT SELECT ON ps_show_uldom_list TO operatortspk2;
GRANT SELECT ON ps_show_task TO operatortspk2;

GRANT SELECT ON ps_kassa_list TO operatortspk2;


GRANT SELECT ON in_account TO operatortspk2;
GRANT SELECT ON in_mac_list TO operatortspk2;
GRANT SELECT ON in_pay_traf TO operatortspk2;
GRANT SELECT ON in_traf_cost TO operatortspk2;

GRANT SELECT ON in_show_login TO operatortspk;
GRANT SELECT ON in_show_mac TO operatortspk;
GRANT SELECT ON in_show_pay TO operatortspk;
GRANT SELECT ON in_show_tarif TO operatortspk;


GRANT SELECT ON sc_status TO operatortspk2;
GRANT SELECT,UPDATE,INSERT ON sc_task TO operatortspk2;
GRANT SELECT,UPDATE,INSERT ON sc_worker TO operatortspk2;
GRANT SELECT,UPDATE,INSERT ON sc_worker_list TO operatortspk2;

GRANT SELECT ON sc_show_status TO operatortspk2;
GRANT SELECT ON sc_show_task TO operatortspk2;
GRANT SELECT ON sc_show_task2 TO operatortspk2;
GRANT SELECT ON sc_show_task_noclose TO operatortspk2;
GRANT SELECT ON sc_show_worker TO operatortspk2;
GRANT SELECT ON sc_show_worker_list TO operatortspk2;
GRANT SELECT ON sc_show_worker_list2 TO operatortspk2;

GRANT SELECT ON sc_show_worker2 TO operatortspk2;
GRANT SELECT ON sc_show_mate TO operatortspk2;

GRANT SELECT ON sc_show_task_p TO operatortspk2;
GRANT SELECT ON ps_show_mate TO operatortspk2;


---
GRANT SELECT,UPDATE,INSERT ON mr_group_list TO operatortspk2;
GRANT SELECT ON mr_store_list TO operatortspk2;
GRANT SELECT,UPDATE,INSERT ON mr_mate_list TO operatortspk2;
GRANT SELECT ON mr_show_mate TO operatortspk2;


GRANT SELECT,UPDATE,INSERT ON mr_mate_in TO operatortspk2;
GRANT SELECT,UPDATE,INSERT ON mr_mate_in_party TO operatortspk2;
GRANT SELECT,UPDATE,INSERT ON mr_story_q TO operatortspk2;
GRANT SELECT,UPDATE,INSERT ON mr_mate_out TO operatortspk2;
GRANT SELECT,UPDATE,INSERT ON mr_mate_out_party TO operatortspk2;
GRANT SELECT,UPDATE,INSERT ON mr_mate_cost TO operatortspk2;

GRANT SELECT ON mr_show_cost TO operatortspk2;
GRANT SELECT ON mr_show_mate_in TO operatortspk2;
GRANT SELECT ON mr_show_store_q TO operatortspk2;

GRANT SELECT,INSERT,UPDATE ON mr_mate_set_store TO operatortspk2;

GRANT SELECT ON mr_show_mate_set_store TO operatortspk2;

GRANT SELECT ON sc_show_mate_store TO operatortspk2;
GRANT SELECT ON sc_show_mate TO operatortspk2;
GRANT SELECT ON mr_show_mate_page TO operatortspk2;

GRANT SELECT ON sc_show_task_p TO operatortspk2;
GRANT SELECT ON mr_show_mate_op TO operatortspk2;
GRANT SELECT ON mr_show_store_group_q TO operatortspk2;

GRANT SELECT ON mr_eds_list TO operatortspk2;
