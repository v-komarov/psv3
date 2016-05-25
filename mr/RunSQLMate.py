#coding:utf-8


import	DBTools






#### --- Получение списка групп ---
def GetListGroup():
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT mr_group_name FROM mr_group_list WHERE mr_rec_delete='' ORDER BY mr_group_name;")
    db.cnx.commit()
    list = []
    result = cr.fetchall()
    cr.close()
    db.Destroy()
    for item in result:
	list.append(item[0])
    return list




#### --- Получение списка единиц измерения ---
def GetListEds():
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT mr_eds_name FROM mr_eds_list ORDER BY mr_eds_name;")
    db.cnx.commit()
    list = []
    result = cr.fetchall()
    cr.close()
    db.Destroy()
    for item in result:
	list.append(item[0])
    return list





#### --- Добавление нового материала ---
def AddMate(name,eds,group):
    name = name.encode('utf-8')
    eds = eds.encode('utf-8')
    group = group.encode('utf-8')
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT mr_AddMate('%s','%s','%s')" % (name,eds,group))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]




#### --- Поиск материала ---
def FindMate(name):
    name = '%' + name.encode('utf-8') + '%'
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT count(*) FROM mr_show_mate WHERE ps_RusUpper(mate_name) LIKE ps_RusUpper('%s')" % (name))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    if result[0] == 0:
	res = 'NOT'
    elif result[0] == 1:
	cr=db.cnx.cursor()
	cr.execute("SELECT rec_id_str FROM mr_show_mate WHERE ps_RusUpper(mate_name) LIKE ps_RusUpper('%s')" % (name))
	db.cnx.commit()
	result = cr.fetchone()
	cr.close()
	res = 'ONE#'+result[0]
    else:
	cr=db.cnx.cursor()
	cr.execute("SELECT * FROM mr_show_mate WHERE ps_RusUpper(mate_name) LIKE ps_RusUpper('%s')" % (name))
	db.cnx.commit()
	result = cr.fetchall()
	cr.close()
	res = result
    db.Destroy()
    return res






#### --- Получение спсика материала группы  ---
def GetMateGroupList(group):
    group = group.encode('utf-8')
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM mr_show_mate WHERE btrim(group_name)=btrim('%s')" % (group))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()
    db.Destroy()
    return result







