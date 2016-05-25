#coding:utf-8


import	DBTools
import	string




#### --- Получение данных по улицам и номерам домов для выбора при формировании отчетов ---
def GetUlDom(): 
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("select * from ps_show_uldom_list")
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()    
    db.Destroy()
    return result



#### --- Вывод списка всех абонентов ---
def ShowAbonentAll(UlDom):
    db = DBTools.DBTools()
    qarray = string.split(UlDom,':')
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM ps_show_abonent_list WHERE btrim(ps_ul)=btrim('%s') AND btrim(ps_dom)=btrim('%s')" % (qarray[0],qarray[1]))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    db.Destroy()
    return result



#### --- Вывод списка абонентов для отчета "Остатки по услугам" ---
def ShowAbonentContact(db,UlDom):
    qarray = string.split(UlDom,':')
    cr = db.cnx.cursor()
    cr.execute("SELECT ps_rec_id,ps_kv,ps_fio FROM ps_show_abonent_list WHERE btrim(ps_ul)=btrim('%s') AND btrim(ps_dom)=btrim('%s')" % (qarray[0],qarray[1]))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    return result




#### --- Вывод списка услуг для отчета "Остатки по услугам" ---
def ShowServiceBalans(db,abonent_kod):
    cr = db.cnx.cursor()
    cr.execute("SELECT service_name,btrim(sum) FROM ps_show_status_service WHERE btrim(abonent_kod)=btrim('%s');" % (abonent_kod))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    return result





#### --- Вывод списка должников ---
def ShowAbonentPart(UlDom):
    db = DBTools.DBTools()
    qarray = string.split(UlDom,':')
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM ps_show_report_abonent_service_dol_mes WHERE btrim(ul)=btrim('%s') AND btrim(dom)=btrim('%s')" % (qarray[0],qarray[1]))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    db.Destroy()
    return result




#### --- Вывод списка должников для объявлений ---
def ShowAbonentPartOb(db,UlDom):
    qarray = string.split(UlDom,':')
    cr = db.cnx.cursor()
    cr.execute("SELECT DISTINCT rec_id,ul,dom,kv,balans_total_str,p,to_number(kv,'9990') FROM ps_show_report_abonent_service_dol_mes WHERE dol_mes>2 AND btrim(ul)=btrim('%s') AND btrim(dom)=btrim('%s') ORDER BY to_number(kv,'9990');" % (qarray[0],qarray[1]))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    return result




#### --- Вывод для объявлений ---
def ShowAbonentPartObService(db,UlDom,ser,month,min_sum):
    qarray = string.split(UlDom,':')
    ser = ser.encode("utf-8")
    month = month.encode("utf-8")
    min_sum = min_sum.encode("utf-8")
    cr = db.cnx.cursor()
    cr.execute("SELECT ul,dom,kv,p,service_name,to_char((ls_sum+cost),'9999990.00') AS dolg,to_number(kv,'9990') FROM ps_show_report_abonent_service_dol_mes WHERE btrim(ul)=btrim('%s') AND btrim(dom)=btrim('%s') AND btrim(service_name)=btrim('%s') AND dol_mes>%s AND abs(ls_sum+cost)>=%s ORDER BY to_number(kv,'9990');" % (qarray[0],qarray[1],ser,month,min_sum))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    return result




#### --- Вывод для объявлений - список должников ---
def ShowAbonentPartObU(db,UlDom):
    qarray = string.split(UlDom,':')
    cr = db.cnx.cursor()
    cr.execute("SELECT DISTINCT rec_id,ul,dom,kv,p,to_number(kv,'9990') FROM ps_show_report_abonent_service_dol_mes WHERE btrim(ul)=btrim('%s') AND btrim(dom)=btrim('%s') ORDER BY to_number(kv,'9990');" % (qarray[0],qarray[1]))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    return result



#### --- Вывод для объявлений - Получение данных по конкретной услуги для конкретного абонента ---
def ShowAbonentPartObServiceData(db,rec_id,ser,month,min_sum):
    ser = ser.encode("utf-8")
    month = month.encode("utf-8")
    min_sum = min_sum.encode("utf-8")

    cr = db.cnx.cursor()
    cr.execute("SELECT count(*) FROM ps_show_report_abonent_service_dol_mes WHERE btrim(rec_id)=btrim('%s') AND btrim(service_name)=btrim('%s') AND dol_mes>%s AND abs(ls_sum+cost)>=%s;" % (rec_id,ser,month,min_sum))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()

    if result[0] == 0:
	return 'None'

    cr = db.cnx.cursor()
    cr.execute("SELECT service_name,to_char((ls_sum+cost),'9999990.00') AS dolg FROM ps_show_report_abonent_service_dol_mes WHERE btrim(rec_id)=btrim('%s') AND btrim(service_name)=btrim('%s') AND dol_mes>%s AND abs(ls_sum+cost)>=%s;" % (rec_id,ser,month,min_sum))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()

    return result




#### --- Вывод списка должников с выбором услуги ---
def ShowAbonentPartService(UlDom,service):
    db = DBTools.DBTools()
    qarray = string.split(UlDom,':')
    service = service.encode('utf-8')
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM ps_show_report_abonent_service_dol_mes WHERE btrim(ul)=btrim('%s') AND btrim(dom)=btrim('%s') AND btrim(service_name)=btrim('%s')" % (qarray[0],qarray[1],service))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    db.Destroy()
    return result






#### --- Вывод суммарного долга по услугам ---
def ShowAbonentPartServiceSum(UlDom):
    db = DBTools.DBTools()
    qarray = string.split(UlDom,':')
    cr = db.cnx.cursor()
    cr.execute("SELECT services_name,sum(abs(ls_sum)) FROM ps_show_report_abonent_service_dol_mes WHERE btrim(ul)=btrim('%s') AND btrim(dom)=btrim('%s') GROUP BY services_name ORDER BY services_name;" % (qarray[0],qarray[1]))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    db.Destroy()
    return result




#### --- Вывод долга по домам и по услугам ---
def ShowDomServiceSum():
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("SELECT ul,dom,service_name,sum(abs(ls_sum)) FROM ps_show_report_abonent_service_dol_mes GROUP BY ul,dom,service_name ORDER BY ul,dom,service_name;")
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    db.Destroy()
    return result




#### --- Вывод долга по услугам ---
def ShowServiceSum():
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("SELECT service_name,sum(abs(ls_sum)) FROM ps_show_report_abonent_service_dol_mes GROUP BY service_name ORDER BY service_name;")
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    db.Destroy()
    return result




#### --- Получение данных по всем сервисам и всем тарифным планам ---
def GetTarifServiceData2(): 
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("select * from ps_show_tarif_plan")
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()    
    db.Destroy()
    return result



#### --- Вывод всего списка заявок ---
def GetListAllTask(UlDom):
    db = DBTools.DBTools()
    qarray = string.split(UlDom,':')
    cr = db.cnx.cursor()
    cr.execute("SELECT *  FROM sc_show_task WHERE btrim(ul)=btrim('%s') AND btrim(dom)=btrim('%s')" % (qarray[0],qarray[1]))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    db.Destroy()
    return result



#### --- Вывод списка незавершенных заявок ---
def GetListNoCloseTask():
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("SELECT *  FROM sc_show_task_noclose")
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    db.Destroy()
    return result



#### --- Вывод списка отключенных абонентов (должников) ---
def ShowAbonentOff():
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("select * from ps_show_abonent_off")
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    db.Destroy()
    return result





#### --- Данные для отчета "Поступления"  ---
def RepPayAll(db,date_start,date_stop):
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM ps_show_report_pay_in WHERE date_pay>='%s' AND date_pay<='%s';" % (date_start,date_stop))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    return result



#### --- Данные для отчета "Поступления"  ---
def RepPayAllService(db,date_start,date_stop):
    cr = db.cnx.cursor()
    cr.execute("SELECT service_name,btrim(to_char(sum(sum_pay),'999999.00')) FROM ps_show_report_pay_in WHERE date_pay>='%s' AND date_pay<='%s' GROUP BY service_name ORDER BY service_name;" % (date_start,date_stop))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    return result




#### --- Данные для отчета "Поступления"  ---
def RepPayAllSum(db,date_start,date_stop):
    cr = db.cnx.cursor()
    cr.execute("SELECT btrim(to_char(sum(sum_pay),'999999.00')) FROM ps_show_report_pay_in WHERE date_pay>='%s' AND date_pay<='%s';" % (date_start,date_stop))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result[0]



#### --- Данные для отчета "Поступления"  ---
def RepPayOtherAll(db,date_start,date_stop):
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM ps_show_report_pay_in_other WHERE date_pay>='%s' AND date_pay<='%s';" % (date_start,date_stop))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    return result




#### --- Данные для отчета "Поступления"  ---
def RepPayOtherAllSum(db,date_start,date_stop):
    cr = db.cnx.cursor()
    cr.execute("SELECT btrim(to_char(sum(sum_pay),'999999.00')) FROM ps_show_report_pay_in_other WHERE date_pay>='%s' AND date_pay<='%s';" % (date_start,date_stop))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result[0]



#### --- Данные для отчета "Поступления"  ---
def RepPayKassa(db,date_start,date_stop,kassa):
    kassa = kassa.encode("utf-8")
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM ps_show_report_pay_in WHERE date_pay>='%s' AND date_pay<='%s' AND kassa_name='%s';" % (date_start,date_stop,kassa))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    return result



#### --- Данные для отчета "Поступления"  ---
def RepPayKassaService(db,date_start,date_stop,kassa):
    kassa = kassa.encode("utf-8")
    cr = db.cnx.cursor()
    cr.execute("SELECT service_name,btrim(to_char(sum(sum_pay),'999999.00')) FROM ps_show_report_pay_in WHERE date_pay>='%s' AND date_pay<='%s' AND kassa_name='%s' GROUP BY service_name ORDER BY service_name;" % (date_start,date_stop,kassa))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    return result




#### --- Данные для отчета "Поступления"  ---
def RepPayKassaSum(db,date_start,date_stop,kassa):
    kassa = kassa.encode("utf-8")
    cr = db.cnx.cursor()
    cr.execute("SELECT btrim(to_char(sum(sum_pay),'999999.00')) FROM ps_show_report_pay_in WHERE date_pay>='%s' AND date_pay<='%s' AND kassa_name='%s';" % (date_start,date_stop,kassa))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result[0]



#### --- Сегодняшняя дата как строка ---
def GetNow():
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("SELECT to_char(current_date,'DD.MM.YYYY')")
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]






#### --- Получение данных по услугам платежей сегодня (для печатной формы копии чека) ---
def GetData4Check1(kod_ab):
    db = DBTools.DBTools()
    vn = (u'ВНЕШНИЙ').encode('utf-8')
    cr=db.cnx.cursor()
    cr.execute("select * from ps_show_check_in where ps_abonent_kod='%s' AND btrim(ps_info)!='%s'" % (kod_ab,vn))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()
    db.Destroy()
    return result




#### --- Получение данных прочих платежей сегодня (для печатной формы копии чека) ---
def GetData4Check2(kod_ab):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("select * from ps_show_check_in_other where ps_abonent_kod='%s'" % (kod_ab))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()
    db.Destroy()
    return result




#### --- Получение списка касс ---
def GetListKassa():
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("SELECT ps_kassa_name FROM ps_kassa_list WHERE ps_rec_delete!='delete' ORDER BY ps_kassa_name;")
    db.cnx.commit()
    list = []
    result=cr.fetchall()
    for row in result:
	list.append(row[0])
    cr.close()
    db.Destroy()
    return list




#### --- Проверка Internet учетной записи (имеет ли абонент доступ к Inetnet) : для Карточки абонента ---
def CheckIntLogin(rec):
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("select count(*) from in_account where in_rec_id=('%s') and in_rec_delete<>'delete'" % (rec))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()    
    db.Destroy()
    return result[0]


#### --- Получение списка лицевых счетов абонента со значениями, согласно его действующего тарифного плана (для печатной формы Карточки абонента) ---
def ServiceBalans(kod_ab):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("select * from ps_show_abonent_service where ps_rec_id='%s'" % (kod_ab))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()
    db.Destroy()
    return result



#### --- Вывод списка MAC адресов ---
def GetListMac():
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("SELECT a.ps_ul||' '||a.ps_dom||'-'||a.ps_kv,m.in_type,m.in_mac FROM ps_abonent_list a, in_mac_list m WHERE a.ps_rec_id=m.in_abonent_kod AND a.ps_rec_delete!='delete' AND m.in_rec_delete!='delete' ORDER BY 1,2")
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    db.Destroy()
    return result



#### --- Вывод списка незавершенных заявок за период для печатной формы ---
def GetListNoCloseTask2(date0,date1):
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("SELECT *  FROM sc_show_task_noclose WHERE date_trunc('day',sc_plan_time)>='%s' AND date_trunc('day',sc_plan_time)<='%s'" % (date0,date1))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    db.Destroy()
    return result




#### --- Вывод балансов по домам ---
def GetListBalans():
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("SELECT ps_ul,ps_dom,sum(ps_balans_total)  FROM ps_abonent_list WHERE ps_rec_delete='' GROUP BY ps_ul,ps_dom ORDER BY ps_ul,ps_dom;")
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    db.Destroy()
    return result



#### --- Журнал загрузок из платежки ---
def GetListPaySystem(date0,date1):
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("SELECT *  FROM ps_show_loadpay WHERE date_trunc('day',date_pay)>='%s' AND date_trunc('day',date_pay)<='%s'" % (date0,date1))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    db.Destroy()
    return result




#### --- Журнал загрузок из платежки (сумма) ---
def GetListPaySystemSum(date0,date1):
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("SELECT btrim(to_char(sum(sum_pay),'99999990.00'))  FROM ps_show_loadpay WHERE date_trunc('day',date_pay)>='%s' AND date_trunc('day',date_pay)<='%s' AND load_ok=1;" % (date0,date1))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]



#### --- Журнал загрузок из Бригантины ---
def GetListPaySystem2(date0,date1):
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("SELECT to_char(ps_date_pay,'DD.MM.YYYY'),to_char(ps_date_load,'DD.MM.YYYY'),ps_ul||' '||ps_dom||'-'||ps_kv,ps_sum,ps_error,ps_ok  FROM ps_loadpay2_log WHERE date_trunc('day',ps_date_pay)>='%s' AND date_trunc('day',ps_date_pay)<='%s'" % (date0,date1))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    db.Destroy()
    return result



#### --- Журнал загрузок из Бригантины (сумма) ---
def GetListPaySystemSum2(date0,date1):
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("SELECT btrim(to_char(sum(ps_sum),'99999990.00'))  FROM ps_loadpay2_log WHERE date_trunc('day',ps_date_pay)>='%s' AND date_trunc('day',ps_date_pay)<='%s' AND ps_ok=1;" % (date0,date1))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]




#### --- Журнал загрузок из КАСС ---
def GetListPaySystem3(date0,date1):
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("SELECT *  FROM ps_show_loadpay3 WHERE date_trunc('day',date_pay)>='%s' AND date_trunc('day',date_pay)<='%s'" % (date0,date1))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    db.Destroy()
    return result




#### --- Журнал загрузок из КАСС (сумма) ---
def GetListPaySystemSum3(date0,date1):
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("SELECT btrim(to_char(sum(sum_pay),'99999990.00'))  FROM ps_show_loadpay3 WHERE date_trunc('day',date_pay)>='%s' AND date_trunc('day',date_pay)<='%s' AND load_ok=1;" % (date0,date1))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]





#### --- Журнал загрузок из CityPay ---
def GetListPaySystem4(date0,date1):
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("SELECT *  FROM ps_show_loadpay4 WHERE date(date_pay)>=date('%s') AND date(date_pay)<=date('%s')" % (date0,date1))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    db.Destroy()
    return result




#### --- Журнал загрузок из CityPay (сумма) ---
def GetListPaySystemSum4(date0,date1):
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("SELECT btrim(to_char(sum(sum_pay),'99999990.00'))  FROM ps_show_loadpay4 WHERE date(date_pay)>=date('%s') AND date(date_pay)<=date('%s') AND load_ok=1;" % (date0,date1))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]




#### --- Получение списка услуг ---
def GetListService():
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("SELECT *  FROM ps_show_service_list;")
    db.cnx.commit()
    result=cr.fetchall()
    list = []
    for row in result:
	list.append(row[0])
    cr.close()
    db.Destroy()
    return list



#### --- Вывод списка услуг должников ---
def ShowAbonentPart3(db,rec_id):
    cr = db.cnx.cursor()
    cr.execute("SELECT service_name,ls_sum_str FROM ps_show_report_abonent_service_dol_mes WHERE rec_id='%s'" % (rec_id))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    return result




#### --- Получение данных по улицам , номерам домов и подъездам ---
def GetUlDomP(): 
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("select * from sc_show_task_p;")
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()    
    db.Destroy()
    return result




#### --- Получение списка складов ---
def GetListStore():
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("SELECT mr_store_name FROM mr_store_list WHERE mr_rec_delete='';")
    db.cnx.commit()
    list = []
    result=cr.fetchall()
    for row in result:
	list.append(row[0])
    cr.close()
    db.Destroy()
    return list




#### --- Получение списка групп материалов ---
def GetListGroup():
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("SELECT mr_group_name FROM mr_group_list WHERE mr_rec_delete='' ORDER BY mr_group_name;")
    db.cnx.commit()
    list = []
    result=cr.fetchall()
    for row in result:
	list.append(row[0])
    cr.close()
    db.Destroy()
    return list




#### --- Получение данных для акта сверки ---
def GetDataAct(abonent_id,date_start,date_stop,service):
    db = DBTools.DBTools()
    service = service.encode("utf-8")
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM ps_Act('%s','%s','%s','%s') AS ( \
	ps_rec_id int, \
	ps_oper_name varchar(50), \
	ps_oper_kod int, \
	ps_date date, \
	ps_date_str varchar(10), \
	ps_service varchar(30), \
	ps_sum numeric(10,2), \
	ps_kassa varchar(50), \
	ps_balans numeric(10,2))" % (abonent_id,date_start,date_stop,service))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    db.Destroy()
    return result
