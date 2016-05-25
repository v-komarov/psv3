#coding:utf-8


import	DBTools






#### --- Получение списка групп ---
def GetListGroup(db):
    cr=db.cnx.cursor()
    cr.execute("SELECT mr_group_name FROM mr_group_list WHERE mr_rec_delete='' ORDER BY mr_group_name;")
    db.cnx.commit()
    list = []
    result = cr.fetchall()
    cr.close()
    for item in result:
	list.append(item[0])
    return list




#### --- Получение списка единиц измерения ---
def GetListEds(db):
    cr=db.cnx.cursor()
    cr.execute("SELECT mr_eds_name FROM mr_eds_list ORDER BY mr_eds_name;")
    db.cnx.commit()
    list = []
    result = cr.fetchall()
    cr.close()
    for item in result:
	list.append(item[0])
    return list





#### --- Изменение материала ---
def EditMate(db,rec_id,name,eds,group):
    name = name.encode('utf-8')
    eds = eds.encode('utf-8')
    group = group.encode('utf-8')
    cr=db.cnx.cursor()
    cr.execute("SELECT mr_EditMate(%s,'%s','%s','%s')" % (rec_id,name,eds,group))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    return result[0]






#### --- Получение записи материала ---
def GetMate(db,rec):
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM mr_show_mate WHERE rec_id_str='%s';" % (rec))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    return result




