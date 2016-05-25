#coding:utf-8


import	DBTools
import	string






#### --- Добавление нового исполнителя ---
def AddWorker(name_1,name_2,name_3):
    name_1 = name_1.encode('utf-8')
    name_2 = name_2.encode('utf-8')
    name_3 = name_3.encode('utf-8')
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT sc_AddWorker('%s','%s','%s')" % (name_1,name_2,name_3))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]




#### --- Получение списка ФИО исполнителей ---
def GetListWorker():
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM sc_show_worker_list2 ORDER BY sc_name_1;")
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()
    db.Destroy()
    return result




#### --- Получение списка исполнителей  для отображения в заявке ---
def GetListWorker2(task_id):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM sc_show_worker2 WHERE task_kod='%s';" % (task_id))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()
    db.Destroy()
    return result



#### --- Получение ФИО исполнителя ---
def GetWorker(kod_row):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM sc_show_worker_list2 WHERE sc_rec_id='%s'" % (kod_row))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result



#### --- изменение исполнителя ---
def EditWorker(kod_row,name_1,name_2,name_3):
    name_1 = name_1.encode('utf-8')
    name_2 = name_2.encode('utf-8')
    name_3 = name_3.encode('utf-8')
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT sc_EditWorker('%s','%s','%s','%s')" % (kod_row,name_1,name_2,name_3))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]




#### --- Удаление исполнителя ---
def DelWorker(kod_row):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT sc_DelWorker('%s')" % (kod_row))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]




#### --- Добавление новой заявки ---
def NewTask(ul,dom,kv,date0):
    ul = ul.encode('utf-8')
    dom = dom.encode('utf-8')
    kv = kv.encode('utf-8')
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT sc_NewTask('%s','%s','%s','%s')" % (ul,dom,kv,date0))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]




#### --- Добавление новой заявки (без указания квартиры) ---
def NewTask2(ul,dom,date0):
    ul = ul.encode('utf-8')
    dom = dom.encode('utf-8')
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT sc_NewTask2('%s','%s','%s')" % (ul,dom,date0))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]




#### --- Получение списка заявок ---
def GetListTask(date):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM sc_show_task WHERE date_trunc('day',sc_plan_time)='%s'" % (date))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()
    db.Destroy()
    return result




#### --- Получение списка всех заявок ---
def GetListTask2(date):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM sc_show_task2 WHERE date_trunc('day',sc_plan_time)='%s'" % (date))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()
    db.Destroy()
    return result





#### --- Получение списка названия заявок ---
def GetListNameTask():
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT DISTINCT sc_text_task FROM sc_task WHERE date_part('day',current_date-sc_date_task_close)<30 AND sc_text_task!='NEW' AND sc_rec_delete!='delete'")
    list = []
    db.cnx.commit()
    result = cr.fetchall()
    for row in result:
	list.append(row[0])
    cr.close()
    db.Destroy()
    return list




#### --- Получение списка статусов ---
def GetListStatus():
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT sc_status FROM sc_show_status")
    list = []
    db.cnx.commit()
    result = cr.fetchall()
    for row in result:
	list.append(row[0])
    cr.close()
    db.Destroy()
    return list



#### --- Получение одной заявки ---
def GetTask(kod):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM sc_show_task2 WHERE rec_id='%s'" % (kod))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result



#### --- Изменение заявки ---
def EditTask(kod_rec,date0,status,kod_type,name,p,phone,plan_ch,workers,fact_ch,note):
    kod_rec = kod_rec.encode("utf-8")
    date0 = date0.encode("utf-8")
    name = name.encode('utf-8')
    status = status.encode('utf-8')
    p = p.encode('utf-8')
    phone = phone.encode('utf-8')
    note = note.encode('utf-8')
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT sc_EditTask('%s','%s','%s',%s,'%s','%s','%s',%s,%s,%s,'%s')" % (kod_rec,date0,status,kod_type,name,p,phone,str(plan_ch),str(workers),str(fact_ch),note))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]





#### --- Удаление заявки ---
def DelTask(kod_rec):
    kod_rec = kod_rec.encode("utf-8")
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT sc_DelTask('%s')" % (kod_rec))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]




#### --- Получение списка фио исполнителей ---
def GetListFIO():
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM sc_show_worker_list")
    list = []
    db.cnx.commit()
    result = cr.fetchall()
    for row in result:
	list.append(row[1])
    cr.close()
    db.Destroy()
    return list




#### --- Добавление исполнителя заявки ---
def AddTaskWorker(kod_rec,kod_w):
    kod_rec = kod_rec.encode("utf-8")
    kod_w = kod_w.encode('utf-8')
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT sc_AddTaskWorker('%s','%s')" % (kod_rec,kod_w))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]



#### --- Получение списка фио исполнителей конкретной заявки ---
def GetListTaskWorker(kod_row):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM sc_show_worker WHERE task_kod='%s'" % (kod_row))
    list = []
    db.cnx.commit()
    result = cr.fetchall()
    for row in result:
	list.append(row[1])
    cr.close()
    db.Destroy()
    return list



#### --- Удаление исполнителя заявки ---
def DelTaskWorker(kod_task,kod_rec):
    kod_task = kod_task.encode("utf-8")
    kod_rec = kod_rec.encode('utf-8')
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT sc_DelTaskWorker('%s','%s')" % (kod_task,kod_rec))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]



#### --- Получение списка заявок на ремонт ---
def GetListTaskRem(date):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM sc_show_task WHERE type_task=1 AND date_trunc('day',sc_plan_time)='%s'" % (date))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()
    db.Destroy()
    return result




#### --- Получение списка заявок на монтаж ---
def GetListTaskMon(date):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM sc_show_task WHERE type_task=2 AND date_trunc('day',sc_plan_time)='%s'" % (date))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()
    db.Destroy()
    return result




#### --- Получение списка групп материалов ---
def GetListMateGroup():
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT mr_group_name FROM mr_group_list WHERE mr_rec_delete='' ORDER BY mr_group_name;")
    list = []
    db.cnx.commit()
    result = cr.fetchall()
    for row in result:
	list.append(row[0])
    cr.close()
    db.Destroy()
    return list




#### --- Получение списка выбора материала по группе ---
def GetListMateStore(group):
    group = group.encode("utf-8")
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM sc_show_mate_store WHERE group_name='%s' AND mate_cost IS NOT NULL" % (group))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()
    db.Destroy()
    return result




#### --- Получение списка использованных материалов по заявке ---
def GetListMate(task):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM sc_show_mate WHERE task_kod='%s'" % (task))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()
    db.Destroy()
    return result



#### --- Добавление материала заявки ---
def AddTaskMate(row_id,mate_kod,store_kod,q,task_kod):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT mr_AddMateOut('%s',%s,%s,%s,'%s')" % (row_id,mate_kod,store_kod,str(q),task_kod))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]



#### --- Добавление материала заявки ---
def DelTaskMate(row_id):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT mr_DelMateOut('%s')" % (row_id))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]


#### --- Получение списка заявок по дому ---
def GetListTaskDom(ul,dom,date):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM sc_show_task WHERE ul='%s' AND dom='%s' AND date_trunc('day',sc_plan_time)='%s'" % (ul,dom,date))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()
    db.Destroy()
    return result

