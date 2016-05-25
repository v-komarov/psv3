#coding:utf-8


from	DBTools	import	DBTools






#### --- Получение списка цен ---
def GetListCost(mate_kod):
    db = DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM mr_show_cost WHERE mate_kod=%s;" % (mate_kod))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()
    db.Destroy()
    return result






#### --- Добавление цены ---
def NewCostMate(db,mate_kod,date,cost):
    cost = cost.encode("utf-8")
    cr=db.cnx.cursor()
    cr.execute("SELECT mr_AddNewCost(%s,'%s',%s)" % (mate_kod,date,cost))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    return result[0]






#### --- Удаление цены ---
def DelCostMate(cost_kod):
    db = DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT mr_DelCost('%s')" % (cost_kod))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]
