#coding:utf-8


"""
 --- Список и структура таблиц для резервирования ---
	
	Условыне типы данных (полей) для того чтобы определенным образом обрабатывать 
	
	numeric - число с точкой
	int - целое число
	text - строка или текст
	date - дата
	timestamp - дата и время
	time - время

"""



#### --- Структура таблиц ---
def Stru():
    
    table_data = (


	(    
	    'ps_abonent_list', (
	    ('ps_rec_id','text'),
	    ('ps_ul','text'),
	    ('ps_dom','text'),
	    ('ps_kv','text'),
	    ('ps_tel','text'),
	    ('ps_fio','text'),
	    ('ps_balans_total','numeric'),
	    ('ps_tarif_plan','text'),
	    ('ps_rec_delete','text'),
	    ('ps_lsp','text'),
	    ('ps_p','text'))
	),



	(    
	    'ps_ls', (
	    ('ps_rec_id','text'),
	    ('ps_abonent_kod','text'),
	    ('ps_service_kod','text'),
	    ('ps_ls_sum','numeric'))
	),



	(    
	    'ps_messages', (
	    ('ps_rec_id','text'),
	    ('ps_data','date'),
	    ('ps_abonent_kod','text'),
	    ('ps_mess_txt','text'),
	    ('ps_rec_delete','text'))
	),



	(    
	    'ps_pay_in', (
	    ('ps_rec_id','text'),
	    ('ps_data','date'),
	    ('ps_abonent_kod','text'),
	    ('ps_tarif_plan_kod','text'),
	    ('ps_service_kod','text'),
	    ('ps_service_sum','numeric'),
	    ('ps_balans_before','numeric'),
	    ('ps_balans_after','numeric'),
	    ('ps_info','text'),
	    ('ps_rec_delete','text'),
	    ('ps_kassa_kod','int'))
	),



	(    
	    'ps_pay_out', (
	    ('ps_rec_id','text'),
	    ('ps_data','date'),
	    ('ps_abonent_kod','text'),
	    ('ps_tarif_plan_kod','text'),
	    ('ps_service_kod','text'),
	    ('ps_service_cost','numeric'),
	    ('ps_balans_before','numeric'),
	    ('ps_balans_after','numeric'),
	    ('ps_info','text'),
	    ('ps_rec_delete','text'))
	),
	

	
	(    
	    'ps_pay_in_other', (
	    ('ps_rec_id','text'),
	    ('ps_data','date'),
	    ('ps_abonent_kod','text'),
	    ('ps_about','text'),
	    ('ps_sum','numeric'),
	    ('ps_info','text'),
	    ('ps_rec_delete','text'))
	),



	(    
	    'ps_services', (
	    ('ps_rec_id','text'),
	    ('ps_services_name','text'),
	    ('ps_rec_delete','text'))
	),



	(    
	    'ps_kassa_list', (
	    ('ps_rec_id','int'),
	    ('ps_kassa_name','text'),
	    ('ps_rec_delete','text'))
	),



	(    
	    'ps_tarif_plan', (
	    ('ps_rec_id','text'),
	    ('ps_tarif_plan_kod','text'),
	    ('ps_type_count','text'),
	    ('ps_cost','numeric'),
	    ('ps_service_kod','text'),
	    ('ps_rec_delete','text'))
	),



	(    
	    'ps_tarif_plan_name', (
	    ('ps_rec_id','text'),
	    ('ps_tarif_plan_name','text'),
	    ('ps_rec_delete','text'))
	),



	(    
	    'ps_uls', (
	    ('ps_rec_id','text'),
	    ('ps_ul_name','text'))
	),



	(    
	    'ps_loadpay_log', (
	    ('ps_date_pay','date'),
	    ('ps_abonent_kod','text'),
	    ('ps_service_kod','text'),
	    ('ps_sum','numeric'),
	    ('ps_lsp','text'),
	    ('ps_date_load','date'),
	    ('ps_error','text'),
	    ('ps_ok','int'))
	),




	(    
	    'ps_loadpay2_log', (
	    ('ps_date_pay','timestamp'),
	    ('ps_ul','text'),
	    ('ps_dom','text'),
	    ('ps_kv','text'),
	    ('ps_service_name','text'),
	    ('ps_sum','numeric'),
	    ('ps_lsp','text'),
	    ('ps_date_load','date'),
	    ('ps_error','text'),
	    ('ps_ok','int'))
	),




	(    
	    'ps_loadpay3_log', (
	    ('ps_date_pay','timestamp'),
	    ('ps_abonent_kod','text'),
	    ('ps_service_kod','text'),
	    ('ps_sum','numeric'),
	    ('ps_lsp','text'),
	    ('ps_date_load','timestamp'),
	    ('ps_error','text'),
	    ('ps_ok','int'))
	),




	(    
	    'in_account', (
	    ('in_rec_id','text'),
	    ('in_user_login','text'),
	    ('in_user_passwd','text'),
	    ('in_cost_kod','int'),
	    ('in_ip_client','text'),
	    ('in_last_time','timestamp'),
	    ('in_rec_delete','text'))
	),



	(    
	    'in_pay_traf', (
	    ('in_rec_abonent','text'),
	    ('in_date_time','timestamp'),
	    ('in_sum','numeric'),
	    ('in_sum_before','numeric'),
	    ('in_sum_after','numeric'),
	    ('in_traf','numeric'),
	    ('in_traf_cost','int'),
	    ('in_rec_delete','text'))
	),



	(    
	    'in_traf_cost', (
	    ('in_rec_id','int'),
	    ('in_cost_name','text'),
	    ('in_cost_1mb','numeric'),
	    ('in_rec_delete','text'))
	),




	(    
	    'in_mac_list', (
	    ('in_rec_id','text'),
	    ('in_abonent_kod','text'),
	    ('in_type','int'),
	    ('in_mac','text'),
	    ('in_create_time','timestamp'),
	    ('in_update_time','timestamp'),
	    ('in_create_author','text'),
	    ('in_update_author','text'),
	    ('in_rec_delete','text'))
	),




	(    
	    'sc_task', (
	    ('sc_rec_id','text'),
	    ('sc_date_task_open','timestamp'),
	    ('sc_date_task_close','timestamp'),
	    ('sc_plan_time','timestamp'),
	    ('sc_text_task','text'),
	    ('sc_status_task','int'),
	    ('sc_type_task','int'),
	    ('sc_abonent_kod','text'),
	    ('sc_ul','text'),
	    ('sc_dom','text'),
	    ('sc_kv','text'),
	    ('sc_p','text'),
	    ('sc_phone','text'),
	    ('sc_plan_chch','numeric'),
	    ('sc_plan_workers','int'),
	    ('sc_fact_chch','numeric'),
	    ('sc_task_note','text'),
	    ('sc_create_time','timestamp'),
	    ('sc_update_time','timestamp'),
	    ('sc_create_author','text'),
	    ('sc_update_author','text'),
	    ('sc_rec_delete','text'))
	),



	(    
	    'sc_worker', (
	    ('sc_rec_id','text'),
	    ('sc_worker_kod','text'),
	    ('sc_task_kod','text'),
	    ('sc_create_time','timestamp'),
	    ('sc_update_time','timestamp'),
	    ('sc_create_author','text'),
	    ('sc_update_author','text'),
	    ('sc_rec_delete','text'))
	),



	(    
	    'sc_status', (
	    ('sc_rec_id','int'),
	    ('sc_status','text'),
	    ('sc_rec_delete','text'))
	),



	(    
	    'sc_worker_list', (
	    ('sc_rec_id','text'),
	    ('sc_name_1','text'),
	    ('sc_name_2','text'),
	    ('sc_name_3','text'),
	    ('sc_create_time','timestamp'),
	    ('sc_update_time','timestamp'),
	    ('sc_create_author','text'),
	    ('sc_update_author','text'),
	    ('sc_rec_delete','text'))
	),




	(    
	    'mr_group_list', (
	    ('mr_rec_id','int'),
	    ('mr_group_name','text'),
	    ('mr_create_time','timestamp'),
	    ('mr_update_time','timestamp'),
	    ('mr_create_author','text'),
	    ('mr_update_author','text'),
	    ('mr_rec_delete','text'))
	),




	(    
	    'mr_eds_list', (
	    ('mr_rec_id','text'),
	    ('mr_eds_name_shot','text'),
	    ('mr_eds_name','text'))
	),




	(    
	    'mr_store_list', (
	    ('mr_rec_id','int'),
	    ('mr_store_name','text'),
	    ('mr_store_man_kod','text'),
	    ('mr_store_man_login','text'),
	    ('mr_create_time','timestamp'),
	    ('mr_update_time','timestamp'),
	    ('mr_create_author','text'),
	    ('mr_update_author','text'),
	    ('mr_rec_delete','text'))
	),




	(    
	    'mr_mate_list', (
	    ('mr_rec_id','int'),
	    ('mr_mate_name','text'),
	    ('mr_eds_kod','text'),
	    ('mr_group_kod','int'),
	    ('mr_create_time','timestamp'),
	    ('mr_update_time','timestamp'),
	    ('mr_create_author','text'),
	    ('mr_update_author','text'),
	    ('mr_rec_delete','text'))
	),




	(    
	    'mr_mate_in', (
	    ('mr_rec_id','text'),
	    ('mr_mate_kod','int'),
	    ('mr_eds_kod','text'),
	    ('mr_mate_cost','numeric'),
	    ('mr_mate_q','numeric'),
	    ('mr_store_kod','int'),
	    ('mr_create_time','timestamp'),
	    ('mr_update_time','timestamp'),
	    ('mr_create_author','text'),
	    ('mr_update_author','text'),
	    ('mr_rec_delete','text'))
	),




	(    
	    'mr_mate_in_party', (
	    ('mr_rec_id','text'),
	    ('mr_party_kod','text'),
	    ('mr_mate_kod','int'),
	    ('mr_eds_kod','text'),
	    ('mr_mate_cost','numeric'),
	    ('mr_mate_q','numeric'),
	    ('mr_store_kod','int'),
	    ('mr_create_time','timestamp'),
	    ('mr_update_time','timestamp'),
	    ('mr_create_author','text'),
	    ('mr_update_author','text'),
	    ('mr_rec_delete','text'))
	),




	(    
	    'mr_story_q', (
	    ('mr_rec_id','text'),
	    ('mr_operation_kod','int'),
	    ('mr_master_kod','text'),
	    ('mr_mate_kod','int'),
	    ('mr_eds_kod','text'),
	    ('mr_mate_q','numeric'),
	    ('mr_store_kod','int'),
	    ('mr_create_time','timestamp'),
	    ('mr_update_time','timestamp'),
	    ('mr_create_author','text'),
	    ('mr_update_author','text'),
	    ('mr_rec_delete','text'))
	),




	(    
	    'mr_mate_out', (
	    ('mr_rec_id','text'),
	    ('mr_task_kod','text'),
	    ('mr_mate_kod','int'),
	    ('mr_eds_kod','text'),
	    ('mr_abonent_cost','numeric'),
	    ('mr_mate_q','numeric'),
	    ('mr_store_kod','int'),
	    ('mr_create_time','timestamp'),
	    ('mr_update_time','timestamp'),
	    ('mr_create_author','text'),
	    ('mr_update_author','text'),
	    ('mr_rec_delete','text'))
	),




	(    
	    'mr_mate_out_party', (
	    ('mr_rec_id','text'),
	    ('mr_party_kod','text'),
	    ('mr_out_kod','text'),
	    ('mr_mate_kod','int'),
	    ('mr_eds_kod','text'),
	    ('mr_abonent_cost','numeric'),
	    ('mr_mate_q','numeric'),
	    ('mr_store_kod','int'),
	    ('mr_create_time','timestamp'),
	    ('mr_update_time','timestamp'),
	    ('mr_create_author','text'),
	    ('mr_update_author','text'),
	    ('mr_rec_delete','text'))
	),




	(    
	    'mr_mate_cost', (
	    ('mr_rec_id','text'),
	    ('mr_date_start','date'),
	    ('mr_mate_kod','int'),
	    ('mr_mate_cost','numeric'),
	    ('mr_create_time','timestamp'),
	    ('mr_update_time','timestamp'),
	    ('mr_create_author','text'),
	    ('mr_update_author','text'),
	    ('mr_rec_delete','text'))
	),




	(    
	    'mr_mate_set_store', (
	    ('mr_rec_id','text'),
	    ('mr_mate_kod','int'),
	    ('mr_eds_kod','text'),
	    ('mr_mate_cost','numeric'),
	    ('mr_mate_q','numeric'),
	    ('mr_store_kod','int'),
	    ('mr_create_time','timestamp'),
	    ('mr_update_time','timestamp'),
	    ('mr_create_author','text'),
	    ('mr_update_author','text'),
	    ('mr_rec_delete','text'))
	),




	(    
	    'mr_operation_list', (
	    ('mr_rec_id','int'),
	    ('mr_operation_name','text'))
	)


    
    )
    
    
    return table_data
    