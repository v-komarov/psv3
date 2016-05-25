GRANT SELECT ON sc_status TO semenov;
GRANT SELECT,UPDATE ON sc_task TO semenov;
GRANT SELECT,UPDATE,INSERT ON sc_worker TO semenov;
GRANT SELECT ON sc_worker_list TO semenov;
GRANT SELECT ON sc_show_status TO semenov;
GRANT SELECT ON sc_show_task TO semenov;
GRANT SELECT ON sc_show_task2 TO semenov;
GRANT SELECT ON sc_show_task_noclose TO semenov;
GRANT SELECT ON sc_show_worker TO semenov;
GRANT SELECT ON sc_show_worker_list TO semenov;
GRANT SELECT ON sc_show_worker_list2 TO semenov;



GRANT SELECT,UPDATE,INSERT ON mr_group_list TO semenov;
GRANT SELECT ON mr_store_list TO semenov;
GRANT SELECT,UPDATE,INSERT ON mr_mate_list TO semenov;
GRANT SELECT ON mr_show_mate TO semenov;


GRANT SELECT,UPDATE,INSERT ON mr_mate_in TO semenov;
GRANT SELECT,UPDATE,INSERT ON mr_mate_in_party TO semenov;
GRANT SELECT,UPDATE,INSERT ON mr_story_q TO semenov;
GRANT SELECT,UPDATE,INSERT ON mr_mate_out TO semenov;
GRANT SELECT,UPDATE,INSERT ON mr_mate_out_party TO semenov;
GRANT SELECT,UPDATE,INSERT ON mr_mate_cost TO semenov;

GRANT SELECT ON mr_show_cost TO semenov;
GRANT SELECT ON mr_show_mate_in TO semenov;
GRANT SELECT ON mr_show_store_q TO semenov;

GRANT SELECT,INSERT,UPDATE ON mr_mate_set_store TO semenov;

GRANT SELECT ON mr_show_mate_set_store TO semenov;

GRANT SELECT ON sc_show_worker2 TO semenov;

GRANT SELECT ON sc_show_mate_store TO semenov;
GRANT SELECT ON sc_show_mate TO semenov;
GRANT SELECT ON mr_show_mate_page TO semenov;

GRANT SELECT ON sc_show_task_p TO semenov;
GRANT SELECT ON mr_show_mate_op TO semenov;
GRANT SELECT ON mr_show_store_group_q TO semenov;

GRANT SELECT ON mr_eds_list TO semenov;
