#coding:utf-8


from	DBTools	import	DBTools








#### --- Получение списка складов ---
def GetListStore():
    db = DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT mr_store_name FROM mr_store_list WHERE mr_rec_delete='' ORDER BY mr_store_name;")
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()    
    db.Destroy()
    list = []
    for item in result:
	list.append(item[0]) 
    return list







#### --- Получение поступлений ---
def GetListMateIn(mate_kod):
    db = DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM mr_show_mate_in WHERE mate_kod=%s;" % (mate_kod))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()
    db.Destroy()
    return result






#### --- Добавление поступления ---
def AddMateIn(mate_kod,store_name,q,cost):
    db = DBTools()
    store_name = store_name.encode("utf-8")
    q = q.encode("utf-8")
    cost = cost.encode("utf-8")
    cr=db.cnx.cursor()
    cr.execute("SELECT mr_AddMateIn(%s,'%s',%s,%s)" % (mate_kod,store_name,q,cost))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]






#### --- Удаление записи поступления ---
def DelMateIn(rec_kod):
    db = DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT mr_DelMateIn('%s')" % (rec_kod))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]
