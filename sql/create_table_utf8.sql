CREATE TABLE ps_abonent_list (
    ps_rec_id varchar(24) NOT NULL,
    ps_ul varchar(20) NOT NULL,
    ps_dom varchar(5) NOT NULL,
    ps_kv varchar(4) NOT NULL,
    ps_tel varchar(16) NOT NULL DEFAULT '',
    ps_fio varchar(40) NOT NULL DEFAULT '',
    ps_balans_total numeric(10,2) NOT NULL DEFAULT 0,
    ps_tarif_plan varchar(24) NOT NULL,
    ps_rec_delete varchar(6) NOT NULL DEFAULT '',
    ps_lsp varchar(8) NOT NULL DEFAULT '',
    ps_p varchar(3) NOT NULL DEFAULT ''
);

CREATE TABLE ps_tarif_plan_name (
    ps_rec_id varchar(24) NOT NULL,
    ps_tarif_plan_name varchar(30) NOT NULL,
    ps_rec_delete varchar(6) NOT NULL DEFAULT ''
);

CREATE TABLE ps_tarif_plan (
    ps_rec_id varchar(24) NOT NULL,
    ps_tarif_plan_kod varchar(24) NOT NULL,
    ps_type_count varchar(20) NOT NULL,
    ps_cost numeric(10,2) NOT NULL DEFAULT 0,
    ps_service_kod varchar(24) NOT NULL,
    ps_rec_delete varchar(6) NOT NULL DEFAULT ''
);

CREATE TABLE ps_services (
    ps_rec_id varchar(24) NOT NULL,
    ps_services_name varchar(30) NOT NULL,
    ps_rec_delete varchar(6) NOT NULL DEFAULT ''
);

CREATE TABLE ps_uls (
    ps_rec_id varchar(1) NOT NULL,
    ps_ul_name varchar(30) NOT NULL
);

CREATE TABLE ps_ls (
    ps_rec_id varchar(24) NOT NULL,
    ps_abonent_kod varchar(24) NOT NULL,
    ps_service_kod varchar(24) NOT NULL,
    ps_ls_sum numeric(10,2) NOT NULL DEFAULT 0
);

CREATE TABLE ps_pay_in (
    ps_rec_id varchar(24) NOT NULL,
    ps_data date NOT NULL DEFAULT current_date,
    ps_abonent_kod varchar(24) NOT NULL,
    ps_tarif_plan_kod varchar(24) NOT NULL,
    ps_service_kod varchar(24) NOT NULL,
    ps_service_sum numeric(10,2) NOT NULL DEFAULT 0,
    ps_balans_before numeric(10,2) NOT NULL,
    ps_balans_after numeric(10,2) NOT NULL,
    ps_info varchar(30) NOT NULL DEFAULT '',
    ps_rec_delete varchar(6) NOT NULL DEFAULT '',
    ps_kassa_kod int NOT NULL DEFAULT 0
);

CREATE TABLE ps_pay_out (
    ps_rec_id varchar(24) NOT NULL,
    ps_data date NOT NULL DEFAULT current_date,
    ps_abonent_kod varchar(24) NOT NULL,
    ps_tarif_plan_kod varchar(24) NOT NULL,
    ps_service_kod varchar(24) NOT NULL,
    ps_service_cost numeric(10,2) NOT NULL DEFAULT 0,
    ps_balans_before numeric(10,2) NOT NULL,
    ps_balans_after numeric(10,2) NOT NULL,
    ps_info varchar(30) NOT NULL DEFAULT '',
    ps_rec_delete varchar(6) NOT NULL DEFAULT ''
);


CREATE TABLE ps_messages (
    ps_rec_id varchar(24) NOT NULL,
    ps_data date NOT NULL DEFAULT current_date,
    ps_abonent_kod varchar(24) NOT NULL,
    ps_mess_txt varchar(70) NOT NULL,
    ps_rec_delete varchar(6) NOT NULL DEFAULT ''
);



CREATE TABLE ps_pay_in_other (
    ps_rec_id varchar(24) NOT NULL,
    ps_data date NOT NULL DEFAULT current_date,
    ps_abonent_kod varchar(24) NOT NULL,
    ps_about varchar(40) NOT NULL,
    ps_sum numeric(10,2) NOT NULL,
    ps_info varchar(30) NOT NULL DEFAULT '',
    ps_rec_delete varchar(6) NOT NULL DEFAULT ''
);




CREATE TABLE ps_loadpay_log (
    ps_date_pay date NOT NULL DEFAULT current_date,
    ps_abonent_kod varchar(24) NOT NULL,
    ps_service_kod varchar(24) NOT NULL,
    ps_sum numeric(10,2) NOT NULL,
    ps_lsp varchar(8) NOT NULL DEFAULT '',
    ps_date_load date NOT NULL DEFAULT current_date,
    ps_error varchar(100) NOT NULL DEFAULT '',
    ps_ok int NOT NULL DEFAULT 0
);




CREATE TABLE ps_loadpay2_log (
    ps_date_pay timestamp NOT NULL DEFAULT current_timestamp,
    ps_ul varchar(30) NOT NULL,
    ps_dom varchar(5) NOT NULL,
    ps_kv varchar(4) NOT NULL,
    ps_service_name varchar(30) NOT NULL DEFAULT '',
    ps_sum numeric(10,2) NOT NULL,
    ps_lsp varchar(8) NOT NULL DEFAULT '',
    ps_date_load date NOT NULL DEFAULT current_date,
    ps_error varchar(100) NOT NULL DEFAULT '',
    ps_ok int NOT NULL DEFAULT 0
);




CREATE TABLE ps_loadpay3_log (
    ps_date_pay timestamp NOT NULL DEFAULT current_timestamp,
    ps_abonent_kod varchar(24) NOT NULL,
    ps_service_kod varchar(24) NOT NULL,
    ps_sum numeric(10,2) NOT NULL,
    ps_lsp varchar(8) NOT NULL DEFAULT '',
    ps_date_load timestamp NOT NULL DEFAULT current_timestamp,
    ps_error varchar(100) NOT NULL DEFAULT '',
    ps_ok int NOT NULL DEFAULT 0
);



CREATE TABLE ps_loadpay4_log (
    ps_date_pay timestamp NOT NULL DEFAULT current_timestamp,
    ps_abonent_kod varchar(24) NOT NULL,
    ps_service_kod varchar(24) NOT NULL,
    ps_sum numeric(10,2) NOT NULL,
    ps_lsp varchar(8) NOT NULL DEFAULT '',
    ps_date_load timestamp NOT NULL DEFAULT current_timestamp,
    ps_error varchar(100) NOT NULL DEFAULT '',
    ps_ok int NOT NULL DEFAULT 0
);




CREATE TABLE ps_kassa_list (
    ps_rec_id int NOT NULL DEFAULT 0,
    ps_kassa_name varchar(50) NOT NULL DEFAULT '',
    ps_rec_delete varchar(6) NOT NULL DEFAULT ''
);

INSERT INTO ps_kassa_list(ps_rec_id,ps_kassa_name,ps_rec_delete) VALUES(0,'НЕТ','delete');
INSERT INTO ps_kassa_list(ps_rec_id,ps_kassa_name) VALUES(1,'КАССА');
INSERT INTO ps_kassa_list(ps_rec_id,ps_kassa_name) VALUES(2,'ПЛАТЁЖКА');
INSERT INTO ps_kassa_list(ps_rec_id,ps_kassa_name) VALUES(3,'БРИГАНТИНА');
INSERT INTO ps_kassa_list(ps_rec_id,ps_kassa_name) VALUES(4,'КАСС');


CREATE TABLE in_account (
    in_rec_id varchar(24) NOT NULL,
    in_user_login varchar(8) NOT NULL,
    in_user_passwd varchar(8) NOT NULL,
    in_cost_kod int4 NOT NULL,
    in_ip_client varchar(15) NOT NULL DEFAULT '0.0.0.0',
    in_last_time timestamp NOT NULL DEFAULT current_timestamp,
    in_rec_delete varchar(6) NOT NULL DEFAULT ''
);


CREATE TABLE in_traf_cost (
    in_rec_id int4 NOT NULL,
    in_cost_name varchar(30) NOT NULL,
    in_cost_1mb numeric(8,2) NOT NULL DEFAULT 0,
    in_rec_delete varchar(6) NOT NULL DEFAULT ''
);


CREATE TABLE in_pay_traf (
    in_rec_abonent varchar(24) NOT NULL,
    in_date_time timestamp NOT NULL DEFAULT current_timestamp,
    in_sum numeric(8,2) NOT NULL DEFAULT 0,
    in_sum_before numeric(8,2) NOT NULL DEFAULT 0,
    in_sum_after numeric(8,2) NOT NULL DEFAULT 0,
    in_traf numeric(8,2) NOT NULL DEFAULT 0,
    in_traf_cost int4 NOT NULL,
    in_rec_delete varchar(6) NOT NULL DEFAULT ''
);


CREATE TABLE in_mac_list (
    in_rec_id varchar(24) NOT NULL,
    in_abonent_kod varchar(24) NOT NULL,
    in_type int2 NOT NULL,
    in_mac varchar(40) NOT NULL,
    in_create_time timestamp NOT NULL DEFAULT current_timestamp,
    in_update_time timestamp NOT NULL DEFAULT current_timestamp,
    in_create_author varchar(50) NOT NULL DEFAULT current_user,
    in_update_author varchar(50) NOT NULL DEFAULT current_user,
    in_rec_delete varchar(6) NOT NULL DEFAULT ''
);



CREATE TABLE sc_task (
    sc_rec_id varchar(24) NOT NULL,
    sc_date_task_open timestamp NOT NULL DEFAULT current_timestamp,
    sc_date_task_close timestamp NOT NULL DEFAULT current_timestamp,
    sc_plan_time timestamp NOT NULL DEFAULT current_timestamp,
    sc_text_task varchar(50) NOT NULL,
    sc_status_task int2 NOT NULL DEFAULT 0,
    sc_type_task int2 NOT NULL DEFAULT 0,
    sc_abonent_kod varchar(50) NOT NULL,
    sc_ul varchar(20) NOT NULL,
    sc_dom varchar(5) NOT NULL,
    sc_kv varchar(4) NOT NULL DEFAULT '',
    sc_p varchar(3) NOT NULL DEFAULT '',
    sc_phone varchar(100) NOT NULL DEFAULT '',
    sc_plan_chch numeric(10,2) NOT NULL DEFAULT 0,
    sc_plan_workers int NOT NULL DEFAULT 0,
    sc_fact_chch numeric(10,2) NOT NULL DEFAULT 0,
    sc_task_note text NOT NULL DEFAULT '',
    sc_create_time timestamp NOT NULL DEFAULT current_timestamp,
    sc_update_time timestamp NOT NULL DEFAULT current_timestamp,
    sc_create_author varchar(50) NOT NULL DEFAULT current_user,
    sc_update_author varchar(50) NOT NULL DEFAULT current_user,
    sc_rec_delete varchar(6) NOT NULL DEFAULT ''
);


CREATE TABLE sc_worker_list (
    sc_rec_id varchar(24) NOT NULL,
    sc_name_1 varchar(30) NOT NULL,
    sc_name_2 varchar(30) NOT NULL,
    sc_name_3 varchar(30) NOT NULL,
    sc_create_time timestamp NOT NULL DEFAULT current_timestamp,
    sc_update_time timestamp NOT NULL DEFAULT current_timestamp,
    sc_create_author varchar(50) NOT NULL DEFAULT current_user,
    sc_update_author varchar(50) NOT NULL DEFAULT current_user,
    sc_rec_delete varchar(6) NOT NULL DEFAULT ''
);



CREATE TABLE sc_status (
    sc_rec_id int2 NOT NULL,
    sc_status varchar(30) NOT NULL,
    sc_rec_delete varchar(6) NOT NULL DEFAULT ''
);

INSERT INTO sc_status(sc_rec_id,sc_status) VALUES(0,'Открыта');
INSERT INTO sc_status(sc_rec_id,sc_status) VALUES(1,'Закрыта');
INSERT INTO sc_status(sc_rec_id,sc_status) VALUES(2,'Отложена');
INSERT INTO sc_status(sc_rec_id,sc_status) VALUES(3,'Отменена');
INSERT INTO sc_status(sc_rec_id,sc_status) VALUES(4,'Выполняется');



CREATE TABLE sc_worker (
    sc_rec_id varchar(24) NOT NULL,
    sc_worker_kod varchar(24) NOT NULL,
    sc_task_kod varchar(24) NOT NULL,
    sc_create_time timestamp NOT NULL DEFAULT current_timestamp,
    sc_update_time timestamp NOT NULL DEFAULT current_timestamp,
    sc_create_author varchar(50) NOT NULL DEFAULT current_user,
    sc_update_author varchar(50) NOT NULL DEFAULT current_user,
    sc_rec_delete varchar(6) NOT NULL DEFAULT ''
);



CREATE TABLE web_log (
    web_datetime timestamp NOT NULL DEFAULT current_timestamp,
    web_ul varchar(250) NOT NULL DEFAULT '',
    web_dom varchar(250) NOT NULL DEFAULT '',
    web_kv varchar(250) NOT NULL DEFAULT '',
    web_ls varchar(250) NOT NULL DEFAULT ''
);



CREATE TABLE mr_group_list (
    mr_rec_id int NOT NULL,
    mr_group_name varchar(100) NOT NULL,
    mr_create_time timestamp NOT NULL DEFAULT current_timestamp,
    mr_update_time timestamp NOT NULL DEFAULT current_timestamp,
    mr_create_author varchar(50) NOT NULL DEFAULT current_user,
    mr_update_author varchar(50) NOT NULL DEFAULT current_user,
    mr_rec_delete varchar(6) NOT NULL DEFAULT ''
);




CREATE TABLE mr_eds_list
(
  mr_rec_id varchar(3) NOT NULL,
  mr_eds_name_shot varchar(12) NOT NULL,
  mr_eds_name varchar(90) NOT NULL
);

INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('112','л','Литр');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('163','г','Грамм');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('166','кг','Килограмм');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('168','т','Тонна');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('355','мин','Минута');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('356','ч','Час');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('359','сут','Сутки');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('360','нед','Неделя');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('361','дек','Декада');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('362','мес','Месяц');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('364','кварт','Квартал');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('365','полгода','Полугодие');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('616','боб','Бобина');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('625','л.','Лист');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('626','100 л.','Сто листов');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('736','рул','Рулон');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('778','упак','Упаковка');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('796','шт','Штука');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('797','100 шт','Сто штук');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('798','тыс.шт','Тысяча штук');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('018','пог.м','Погонный метр');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('449','т.км','Тонно-километр');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('539','чел.ч','Человеко-час');
INSERT INTO mr_eds_list (mr_rec_id,mr_eds_name_shot,mr_eds_name) VALUES('540','чел.дн','Человеко-день');



CREATE TABLE mr_store_list (
    mr_rec_id int NOT NULL,
    mr_store_name varchar(100) NOT NULL,
    mr_store_man_kod varchar(24) NOT NULL,
    mr_store_man_login varchar(50) NOT NULL,
    mr_create_time timestamp NOT NULL DEFAULT current_timestamp,
    mr_update_time timestamp NOT NULL DEFAULT current_timestamp,
    mr_create_author varchar(50) NOT NULL DEFAULT current_user,
    mr_update_author varchar(50) NOT NULL DEFAULT current_user,
    mr_rec_delete varchar(6) NOT NULL DEFAULT ''
);
INSERT INTO mr_store_list (mr_rec_id,mr_store_name,mr_store_man_kod,mr_store_man_login) VALUES('1','БАТУРИНА 10','152450644124505822htab00','semenov');



CREATE TABLE mr_mate_list (
    mr_rec_id int NOT NULL,
    mr_mate_name varchar(200) NOT NULL,
    mr_eds_kod varchar(3) NOT NULL,
    mr_group_kod int NOT NULL,
    mr_create_time timestamp NOT NULL DEFAULT current_timestamp,
    mr_update_time timestamp NOT NULL DEFAULT current_timestamp,
    mr_create_author varchar(50) NOT NULL DEFAULT current_user,
    mr_update_author varchar(50) NOT NULL DEFAULT current_user,
    mr_rec_delete varchar(6) NOT NULL DEFAULT ''
);



CREATE TABLE mr_mate_in (
    mr_rec_id varchar(24) NOT NULL,
    mr_mate_kod int NOT NULL,
    mr_eds_kod varchar(3) NOT NULL,
    mr_mate_cost numeric(10,2) NOT NULL DEFAULT 0.00,
    mr_mate_q numeric(10,2) NOT NULL DEFAULT 0.00,
    mr_store_kod int NOT NULL,
    mr_create_time timestamp NOT NULL DEFAULT current_timestamp,
    mr_update_time timestamp NOT NULL DEFAULT current_timestamp,
    mr_create_author varchar(50) NOT NULL DEFAULT current_user,
    mr_update_author varchar(50) NOT NULL DEFAULT current_user,
    mr_rec_delete varchar(6) NOT NULL DEFAULT ''
);



CREATE TABLE mr_mate_in_party (
    mr_rec_id varchar(24) NOT NULL,
    mr_party_kod varchar(24) NOT NULL,
    mr_mate_kod int NOT NULL,
    mr_eds_kod varchar(3) NOT NULL,
    mr_mate_cost numeric(10,2) NOT NULL DEFAULT 0.00,
    mr_mate_q numeric(10,2) NOT NULL DEFAULT 0.00,
    mr_store_kod int NOT NULL,
    mr_create_time timestamp NOT NULL DEFAULT current_timestamp,
    mr_update_time timestamp NOT NULL DEFAULT current_timestamp,
    mr_create_author varchar(50) NOT NULL DEFAULT current_user,
    mr_update_author varchar(50) NOT NULL DEFAULT current_user,
    mr_rec_delete varchar(6) NOT NULL DEFAULT ''
);



CREATE TABLE mr_story_q (
    mr_rec_id varchar(24) NOT NULL,
    mr_operation_kod int NOT NULL,
    mr_master_kod varchar(24) NOT NULL,
    mr_mate_kod int NOT NULL,
    mr_eds_kod varchar(3) NOT NULL,
    mr_mate_q numeric(10,2) NOT NULL DEFAULT 0.00,
    mr_store_kod int NOT NULL,
    mr_create_time timestamp NOT NULL DEFAULT current_timestamp,
    mr_update_time timestamp NOT NULL DEFAULT current_timestamp,
    mr_create_author varchar(50) NOT NULL DEFAULT current_user,
    mr_update_author varchar(50) NOT NULL DEFAULT current_user,
    mr_rec_delete varchar(6) NOT NULL DEFAULT ''
);



CREATE TABLE mr_mate_out (
    mr_rec_id varchar(24) NOT NULL,
    mr_task_kod varchar(24) NOT NULL,
    mr_mate_kod int NOT NULL,
    mr_eds_kod varchar(3) NOT NULL,
    mr_abonent_cost numeric(10,2) NOT NULL DEFAULT 0.00,
    mr_mate_q numeric(10,2) NOT NULL DEFAULT 0.00,
    mr_store_kod int NOT NULL,
    mr_create_time timestamp NOT NULL DEFAULT current_timestamp,
    mr_update_time timestamp NOT NULL DEFAULT current_timestamp,
    mr_create_author varchar(50) NOT NULL DEFAULT current_user,
    mr_update_author varchar(50) NOT NULL DEFAULT current_user,
    mr_rec_delete varchar(6) NOT NULL DEFAULT ''
);



CREATE TABLE mr_mate_out_party (
    mr_rec_id varchar(24) NOT NULL,
    mr_party_kod varchar(24) NOT NULL,
    mr_out_kod varchar(24) NOT NULL,
    mr_mate_kod int NOT NULL,
    mr_eds_kod varchar(3) NOT NULL,
    mr_abonent_cost numeric(10,2) NOT NULL DEFAULT 0.00,
    mr_mate_q numeric(10,2) NOT NULL DEFAULT 0.00,
    mr_store_kod int NOT NULL,
    mr_create_time timestamp NOT NULL DEFAULT current_timestamp,
    mr_update_time timestamp NOT NULL DEFAULT current_timestamp,
    mr_create_author varchar(50) NOT NULL DEFAULT current_user,
    mr_update_author varchar(50) NOT NULL DEFAULT current_user,
    mr_rec_delete varchar(6) NOT NULL DEFAULT ''
);



CREATE TABLE mr_mate_cost (
    mr_rec_id varchar(24) NOT NULL,
    mr_date_start date NOT NULL,
    mr_mate_kod int NOT NULL,
    mr_mate_cost numeric(10,2) NOT NULL DEFAULT 0.00,
    mr_create_time timestamp NOT NULL DEFAULT current_timestamp,
    mr_update_time timestamp NOT NULL DEFAULT current_timestamp,
    mr_create_author varchar(50) NOT NULL DEFAULT current_user,
    mr_update_author varchar(50) NOT NULL DEFAULT current_user,
    mr_rec_delete varchar(6) NOT NULL DEFAULT ''
);



CREATE TABLE mr_mate_set_store (
    mr_rec_id varchar(24) NOT NULL,
    mr_mate_kod int NOT NULL,
    mr_eds_kod varchar(3) NOT NULL,
    mr_mate_cost numeric(10,2) NOT NULL DEFAULT 0.00,
    mr_mate_q numeric(10,2) NOT NULL DEFAULT 0.00,
    mr_store_kod int NOT NULL,
    mr_create_time timestamp NOT NULL DEFAULT current_timestamp,
    mr_update_time timestamp NOT NULL DEFAULT current_timestamp,
    mr_create_author varchar(50) NOT NULL DEFAULT current_user,
    mr_update_author varchar(50) NOT NULL DEFAULT current_user,
    mr_rec_delete varchar(6) NOT NULL DEFAULT ''
);





CREATE TABLE mr_operation_list
(
  mr_rec_id int NOT NULL,
  mr_operation_name varchar(200) NOT NULL
);

INSERT INTO mr_operation_list (mr_rec_id,mr_operation_name) VALUES(0,'НЕТ');
INSERT INTO mr_operation_list (mr_rec_id,mr_operation_name) VALUES(1,'Ввод остатка');
INSERT INTO mr_operation_list (mr_rec_id,mr_operation_name) VALUES(2,'Поступление на склад');
INSERT INTO mr_operation_list (mr_rec_id,mr_operation_name) VALUES(3,'Удаление поступления на склад');
INSERT INTO mr_operation_list (mr_rec_id,mr_operation_name) VALUES(4,'Расход со склада');
INSERT INTO mr_operation_list (mr_rec_id,mr_operation_name) VALUES(5,'Удаление расхода со склада');


