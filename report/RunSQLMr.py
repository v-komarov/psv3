#coding:utf-8


import	DBTools
import	string







#### --- Получение складских остатков ---
def GetStoreGroup(store,group): 
    store = store.encode("utf-8")
    group = group.encode("utf-8")
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM mr_show_store_group_q WHERE store_name='%s' AND group_name='%s' ORDER BY mate_name;" % (store,group))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()    
    db.Destroy()
    return result



#### --- Получение движения материала ---
def GetMateInfo(db,mate_kod,date0,date1): 
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM mr_show_mate_op WHERE mate_kod='%s' AND create_time>='%s' AND create_time<='%s';" % (mate_kod,date0,date1))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()    
    return result



#### --- Получение записи одного материала ---
def GetMate(db,mate_kod): 
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM mr_show_mate WHERE rec_id_str='%s';" % (mate_kod))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()    
    return result



#### --- Получение списка заявок по подъезду ---
def GetTaskP(db,date0,date1,ul,dom,p):
#    ul = ul.encode("utf-8") 
#    dom = dom.encode("utf-8") 
#    p = p.encode("utf-8") 
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM sc_show_task2 WHERE date_trunc('day',sc_plan_time)>='%s' AND date_trunc('day',sc_plan_time)<='%s' AND btrim(ul)=btrim('%s') AND btrim(dom)=btrim('%s') AND btrim(p)=btrim('%s') AND kv='' AND rec_delete='';" % (date0,date1,ul,dom,p))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()    
    return result



#### --- Получение списка исполнителей по заявке ---
def GetTaskWorker(db,task_kod):
    cr = db.cnx.cursor()
    cr.execute("SELECT name_1 FROM sc_show_worker2 WHERE task_kod='%s';" % (task_kod))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()    
    return result



#### --- Получение списка материалов по заявке ---
def GetTaskMate(db,task_kod):
    cr = db.cnx.cursor()
    cr.execute("SELECT substr(mate_name,1,35),eds_name,mate_q,mate_sum FROM sc_show_mate WHERE task_kod='%s';" % (task_kod))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()    
    return result
