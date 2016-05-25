#coding:utf-8


import	DBTools




#### --- Определение количества строк в таблице (для резервирования) ---
def CountTable(table):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("select count(*) from %s" % (table))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]




#### --- Получение всех строк всех полей из таблицы, для резервирования данных ---
def GetTable(runsql):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute(runsql)
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()
    db.Destroy()
    return result




#### --- Выполнение команды sql, для загрузки данных из резервной копии ---
def RunSql(db,runsql):
    cr=db.cnx.cursor()
    cr.execute(runsql)
    db.cnx.commit()
    cr.close()

