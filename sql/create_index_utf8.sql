
--- Таблица ps_abonent_list ---
CREATE UNIQUE INDEX ps_abonent_list_index ON ps_abonent_list USING btree (ps_ul,ps_dom,ps_kv);
CREATE INDEX ps_abonent_list_index1 ON ps_abonent_list USING btree (ps_rec_delete);
CREATE UNIQUE INDEX ps_abonent_list_index2 ON ps_abonent_list USING btree (ps_rec_id);
CREATE UNIQUE INDEX ps_abonent_list_index3 ON ps_abonent_list USING btree (ps_lsp);

--- Таблица ps_tarif_plan_name ---
CREATE UNIQUE INDEX ps_tarif_plan_name_index ON ps_tarif_plan_name USING btree (ps_tarif_plan_name);
CREATE INDEX ps_tarif_plan_name_index1 ON ps_tarif_plan_name USING btree (ps_rec_delete);
CREATE UNIQUE INDEX ps_tarif_plan_name_index2 ON ps_tarif_plan_name USING btree (ps_rec_id);
CREATE UNIQUE INDEX ps_tarif_plan_index ON ps_tarif_plan USING btree (ps_service_kod,ps_tarif_plan_kod);

--- Таблица ps_tarif_plan ---
CREATE INDEX ps_tarif_plan_index1 ON ps_tarif_plan USING btree (ps_rec_delete);
CREATE UNIQUE INDEX ps_tarif_plan_index2 ON ps_tarif_plan USING btree (ps_rec_id);

--- Таблица ps_services ---
CREATE UNIQUE INDEX ps_services_index ON ps_services USING btree (ps_services_name);
CREATE INDEX ps_services_index1 ON ps_services USING btree (ps_rec_delete);
CREATE UNIQUE INDEX ps_services_index2 ON ps_services USING btree (ps_rec_id);

--- Таблица ps_uls ---
CREATE UNIQUE INDEX ps_uls_index ON ps_uls USING btree (ps_ul_name);
CREATE UNIQUE INDEX ps_uls_index2 ON ps_uls USING btree (ps_rec_id);

--- Таблица ps_ls ---
CREATE INDEX ps_ls_index0 ON ps_ls USING btree (ps_abonent_kod);
CREATE INDEX ps_ls_index1 ON ps_ls USING btree (ps_service_kod);
CREATE UNIQUE INDEX ps_ls_index2 ON ps_ls USING btree (ps_rec_id);

--- Таблица ps_pay_in ---
CREATE INDEX ps_pay_in_index0 ON ps_pay_in USING btree (ps_abonent_kod);
CREATE INDEX ps_pay_in_index1 ON ps_pay_in USING btree (ps_rec_delete);
CREATE UNIQUE INDEX ps_pay_in_index2 ON ps_pay_in USING btree (ps_rec_id);
CREATE INDEX ps_pay_in_index3 ON ps_pay_in USING btree (ps_tarif_plan_kod);
CREATE INDEX ps_pay_in_index4 ON ps_pay_in USING btree (ps_kassa_kod);

--- Таблица ps_pay_out ---
CREATE INDEX ps_pay_out_index0 ON ps_pay_out USING btree (ps_abonent_kod);
CREATE INDEX ps_pay_out_index1 ON ps_pay_out USING btree (ps_rec_delete);
CREATE UNIQUE INDEX ps_pay_out_index2 ON ps_pay_out USING btree (ps_rec_id);
CREATE INDEX ps_pay_out_index3 ON ps_pay_out USING btree (ps_tarif_plan_kod);


--- Таблица ps_messages ---
CREATE INDEX ps_messages_index1 ON ps_messages USING btree (ps_rec_delete);
CREATE UNIQUE INDEX ps_messages_index2 ON ps_messages USING btree (ps_rec_id);


--- Таблица ps_pay_in_other ---
CREATE INDEX ps_pay_in_other_index1 ON ps_pay_in_other USING btree (ps_rec_delete);
CREATE UNIQUE INDEX ps_pay_in_other_index2 ON ps_pay_in_other USING btree (ps_rec_id);


--- Для таблицы ps_loadpay_log ---
CREATE INDEX ps_loadpay_log_i0 ON ps_loadpay_log USING btree (ps_date_pay,ps_abonent_kod,ps_service_kod,ps_sum);
CREATE INDEX ps_loadpay_log_i1 ON ps_loadpay_log USING btree (ps_date_load);
CREATE INDEX ps_loadpay_log_i2 ON ps_loadpay_log USING btree (ps_ok);
CREATE INDEX ps_loadpay_log_i3 ON ps_loadpay_log USING btree (ps_date_pay);
CREATE INDEX ps_loadpay_log_i4 ON ps_loadpay_log USING btree (ps_abonent_kod);
CREATE INDEX ps_loadpay_log_i5 ON ps_loadpay_log USING btree (ps_service_kod);


--- Для таблицы ps_loadpay2_log ---
CREATE INDEX ps_loadpay2_log_i0 ON ps_loadpay2_log USING btree (ps_date_pay,ps_ul,ps_dom,ps_kv,ps_service_name,ps_sum);
CREATE INDEX ps_loadpay2_log_i1 ON ps_loadpay2_log USING btree (ps_date_load);
CREATE INDEX ps_loadpay2_log_i2 ON ps_loadpay2_log USING btree (ps_ok);
CREATE INDEX ps_loadpay2_log_i3 ON ps_loadpay2_log USING btree (ps_date_pay);
CREATE INDEX ps_loadpay2_log_i4 ON ps_loadpay2_log USING btree (ps_service_name);


--- Для таблицы ps_loadpay3_log ---
CREATE INDEX ps_loadpay3_log_i0 ON ps_loadpay3_log USING btree (ps_date_pay,ps_abonent_kod,ps_service_kod,ps_sum);
CREATE INDEX ps_loadpay3_log_i1 ON ps_loadpay3_log USING btree (ps_date_load);
CREATE INDEX ps_loadpay3_log_i2 ON ps_loadpay3_log USING btree (ps_ok);
CREATE INDEX ps_loadpay3_log_i3 ON ps_loadpay3_log USING btree (ps_date_pay);
CREATE INDEX ps_loadpay3_log_i4 ON ps_loadpay3_log USING btree (ps_abonent_kod);
CREATE INDEX ps_loadpay3_log_i5 ON ps_loadpay3_log USING btree (ps_service_kod);



--- Для таблицы ps_loadpay4_log ---
CREATE INDEX ps_loadpay4_log_i0 ON ps_loadpay4_log USING btree (ps_date_pay,ps_abonent_kod,ps_service_kod,ps_sum);
CREATE INDEX ps_loadpay4_log_i1 ON ps_loadpay4_log USING btree (ps_date_load);
CREATE INDEX ps_loadpay4_log_i2 ON ps_loadpay4_log USING btree (ps_ok);
CREATE INDEX ps_loadpay4_log_i3 ON ps_loadpay4_log USING btree (ps_date_pay);
CREATE INDEX ps_loadpay4_log_i4 ON ps_loadpay4_log USING btree (ps_abonent_kod);
CREATE INDEX ps_loadpay4_log_i5 ON ps_loadpay4_log USING btree (ps_service_kod);



--- Таблица ps_kassa_list ---
CREATE UNIQUE INDEX ps_kassa_i0 ON ps_kassa_list USING btree (ps_rec_id);
CREATE INDEX ps_kassa_i1 ON ps_kassa_list USING btree (ps_rec_delete);

--- Для таблицы in_account ---
CREATE UNIQUE INDEX in_account_index0 ON in_account USING btree (in_rec_id);
CREATE INDEX in_account_index1 ON in_account USING btree (in_rec_delete);
CREATE UNIQUE INDEX in_account_index2 ON in_account USING btree (in_user_login);
CREATE INDEX in_account_index3 ON in_account USING btree (in_cost_kod);


--- Для таблицы in_traf_cost ---
CREATE UNIQUE INDEX in_traf_cost_index0 ON in_traf_cost USING btree (in_rec_id);
CREATE INDEX in_traf_cost_index1 ON in_traf_cost USING btree (in_rec_delete);
CREATE UNIQUE INDEX in_traf_cost_index2 ON in_traf_cost USING btree (in_cost_name);

--- Для таблицы in_pay_traf ---
CREATE INDEX in_pay_traf_index0 ON in_pay_traf USING btree (in_rec_abonent);
CREATE INDEX in_pay_traf_index1 ON in_pay_traf USING btree (in_rec_delete);
CREATE INDEX in_pay_traf_index2 ON in_pay_traf USING btree (in_date_time);
CREATE INDEX in_pay_traf_index3 ON in_pay_traf USING btree (in_traf_cost);

--- Таблица in_mac_list ---
CREATE UNIQUE INDEX in_mac_list_index0 ON in_mac_list USING btree (in_rec_id);
CREATE UNIQUE INDEX in_mac_list_index2 ON in_mac_list USING btree (in_type,in_mac);
CREATE INDEX in_mac_list_index3 ON in_mac_list USING btree (in_rec_delete);


--- таблица sc_task ---
CREATE UNIQUE INDEX sc_task_index0 ON sc_task USING btree (sc_rec_id);
CREATE INDEX sc_task_index1 ON sc_task USING btree (sc_abonent_kod);
CREATE INDEX sc_task_index2 ON sc_task USING btree (sc_status_task);
CREATE INDEX sc_task_index3 ON sc_task USING btree (sc_type_task);
CREATE INDEX sc_task_index4 ON sc_task USING btree (sc_rec_delete);


--- Таблица sc_worker_list ---
CREATE UNIQUE INDEX sc_worker_list_index0 ON sc_worker_list USING btree (sc_rec_id);
CREATE UNIQUE INDEX sc_worker_list_index1 ON sc_worker_list USING btree (sc_name_1,sc_name_2,sc_name_3);
CREATE INDEX sc_worker_list_index2 ON sc_worker_list USING btree (sc_rec_delete);


--- Таблица sc_status ---
CREATE UNIQUE INDEX sc_status_index0 ON sc_status USING btree (sc_rec_id);
CREATE UNIQUE INDEX sc_status_index1 ON sc_status USING btree (sc_status);
CREATE INDEX sc_status_index2 ON sc_status USING btree (sc_rec_delete);

--- Таблица sc_worker ---
CREATE UNIQUE INDEX sc_worker_index0 ON sc_worker USING btree (sc_rec_id);
CREATE UNIQUE INDEX sc_worker_index1 ON sc_worker USING btree (sc_task_kod,sc_worker_kod);
CREATE INDEX sc_worker_index2 ON sc_worker USING btree (sc_worker_kod);
CREATE INDEX sc_worker_index3 ON sc_worker USING btree (sc_task_kod);
CREATE INDEX sc_worker_index4 ON sc_worker USING btree (sc_rec_delete);


--- Таблица mr_group_list ---
CREATE UNIQUE INDEX mr_group_list_i0 ON mr_group_list USING btree(mr_rec_id);
CREATE UNIQUE INDEX mr_group_list_i1 ON mr_group_list USING btree(mr_group_name);
CREATE INDEX mr_group_list_i2 ON mr_group_list USING btree(mr_rec_delete);



--- Таблица mr_eds_list ---
CREATE UNIQUE INDEX mr_eds_list_i0 ON mr_eds_list USING btree(mr_rec_id);
CREATE UNIQUE INDEX mr_eds_list_i1 ON mr_eds_list USING btree(mr_eds_name_shot);
CREATE UNIQUE INDEX mr_eds_list_i2 ON mr_eds_list USING btree(mr_eds_name);



--- Таблица mr_store_list ---
CREATE UNIQUE INDEX mr_store_list_i0 ON mr_store_list USING btree(mr_rec_id);
CREATE UNIQUE INDEX mr_store_list_i1 ON mr_store_list USING btree(mr_store_name);
CREATE INDEX mr_store_list_i2 ON mr_store_list USING btree(mr_store_man_kod);
CREATE INDEX mr_store_list_i3 ON mr_store_list USING btree(mr_store_man_login);
CREATE INDEX mr_store_list_i4 ON mr_store_list USING btree(mr_rec_delete);



--- Таблица mr_mate_list ---
CREATE UNIQUE INDEX mr_mate_list_i0 ON mr_mate_list USING btree(mr_rec_id);
CREATE UNIQUE INDEX mr_mate_list_i1 ON mr_mate_list USING btree(mr_mate_name);
CREATE INDEX mr_mate_list_i2 ON mr_mate_list USING btree(mr_eds_kod);
CREATE INDEX mr_mate_list_i3 ON mr_mate_list USING btree(mr_group_kod);
CREATE INDEX mr_mate_list_i4 ON mr_mate_list USING btree(mr_rec_delete);



--- Таблица mr_mate_in ---
CREATE UNIQUE INDEX mr_mate_in_i0 ON mr_mate_in USING btree(mr_rec_id);
CREATE INDEX mr_mate_in_i1 ON mr_mate_in USING btree(mr_mate_kod);
CREATE INDEX mr_mate_in_i2 ON mr_mate_in USING btree(mr_eds_kod);
CREATE INDEX mr_mate_in_i3 ON mr_mate_in USING btree(mr_store_kod);
CREATE INDEX mr_mate_in_i4 ON mr_mate_in USING btree(mr_rec_delete);



--- Таблица mr_mate_in_party ---
CREATE UNIQUE INDEX mr_mate_in_party_i0 ON mr_mate_in_party USING btree(mr_rec_id);
CREATE INDEX mr_mate_in_party_i1 ON mr_mate_in_party USING btree(mr_party_kod);
CREATE INDEX mr_mate_in_party_i2 ON mr_mate_in_party USING btree(mr_mate_kod);
CREATE INDEX mr_mate_in_party_i3 ON mr_mate_in_party USING btree(mr_eds_kod);
CREATE INDEX mr_mate_in_party_i4 ON mr_mate_in_party USING btree(mr_store_kod);
CREATE INDEX mr_mate_in_party_i5 ON mr_mate_in_party USING btree(mr_rec_delete);



--- Таблица mr_story_q ---
CREATE UNIQUE INDEX mr_story_q_i0 ON mr_story_q USING btree(mr_rec_id);
CREATE INDEX mr_story_q_i1 ON mr_story_q USING btree(mr_operation_kod);
CREATE INDEX mr_story_q_i2 ON mr_story_q USING btree(mr_master_kod);
CREATE INDEX mr_story_q_i3 ON mr_story_q USING btree(mr_mate_kod);
CREATE INDEX mr_story_q_i4 ON mr_story_q USING btree(mr_eds_kod);
CREATE INDEX mr_story_q_i5 ON mr_story_q USING btree(mr_store_kod);
CREATE INDEX mr_story_q_i6 ON mr_story_q USING btree(mr_rec_delete);



--- Таблица mr_mate_out ---
CREATE UNIQUE INDEX mr_mate_out_i0 ON mr_mate_out USING btree(mr_rec_id);
CREATE INDEX mr_mate_out_i1 ON mr_mate_out USING btree(mr_task_kod);
CREATE INDEX mr_mate_out_i2 ON mr_mate_out USING btree(mr_mate_kod);
CREATE INDEX mr_mate_out_i3 ON mr_mate_out USING btree(mr_eds_kod);
CREATE INDEX mr_mate_out_i4 ON mr_mate_out USING btree(mr_store_kod);
CREATE INDEX mr_mate_out_i5 ON mr_mate_out USING btree(mr_rec_delete);



--- Таблица mr_mate_out_party ---
CREATE UNIQUE INDEX mr_mate_out_party_i0 ON mr_mate_out_party USING btree(mr_rec_id);
CREATE INDEX mr_mate_out_party_i1 ON mr_mate_out_party USING btree(mr_party_kod);
CREATE INDEX mr_mate_out_party_i2 ON mr_mate_out_party USING btree(mr_out_kod);
CREATE INDEX mr_mate_out_party_i3 ON mr_mate_out_party USING btree(mr_mate_kod);
CREATE INDEX mr_mate_out_party_i4 ON mr_mate_out_party USING btree(mr_eds_kod);
CREATE INDEX mr_mate_out_party_i5 ON mr_mate_out_party USING btree(mr_store_kod);
CREATE INDEX mr_mate_out_party_i6 ON mr_mate_out_party USING btree(mr_rec_delete);



--- Таблица mr_mate_cost ---
CREATE UNIQUE INDEX mr_mate_cost_i0 ON mr_mate_cost USING btree(mr_rec_id);
CREATE INDEX mr_mate_cost_i1 ON mr_mate_cost USING btree(mr_date_start);
CREATE INDEX mr_mate_cost_i2 ON mr_mate_cost USING btree(mr_mate_kod);
CREATE INDEX mr_mate_cost_i3 ON mr_mate_cost USING btree(mr_rec_delete);



--- Таблица mr_mate_set_store ---
CREATE UNIQUE INDEX mr_mate_set_store_i0 ON mr_mate_in USING btree(mr_rec_id);
CREATE INDEX mr_mate_set_store_i1 ON mr_mate_set_store USING btree(mr_mate_kod);
CREATE INDEX mr_mate_set_store_i2 ON mr_mate_set_store USING btree(mr_eds_kod);
CREATE INDEX mr_mate_set_store_i3 ON mr_mate_set_store USING btree(mr_store_kod);
CREATE INDEX mr_mate_set_store_i4 ON mr_mate_set_store USING btree(mr_rec_delete);



--- Таблица mr_operation_list ---
CREATE UNIQUE INDEX mr_operation_list_i0 ON mr_operation_list USING btree(mr_rec_id);
CREATE UNIQUE INDEX mr_operation_list_i1 ON mr_operation_list USING btree(mr_operation_name);
