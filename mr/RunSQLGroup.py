#coding:utf-8


import	DBTools






#### --- Получение списка групп ---
def GetListGroup():
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT btrim(to_char(mr_rec_id,'990')),mr_group_name FROM mr_group_list WHERE mr_rec_delete='' ORDER BY mr_group_name;")
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()
    db.Destroy()
    return result






#### --- Добавление новой группы ---
def AddGroup(name):
    name = name.encode('utf-8')
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT mr_AddGroup('%s')" % (name))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]





#### --- Изменение группы ---
def EditGroup(rec,name):
    name = name.encode('utf-8')
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT mr_EditGroup(%s,'%s')" % (rec,name))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]




#### --- Получение записи группы ---
def GetGroup(rec):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT mr_group_name FROM mr_group_list WHERE mr_rec_id=%s;" % (rec))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]




