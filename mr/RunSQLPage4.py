#coding:utf-8


from	DBTools	import	DBTools









#### --- Получение списка ввода остатков ---
def GetListMateSetStore(mate_kod):
    db = DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM mr_show_mate_set_store WHERE mate_kod=%s;" % (mate_kod))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()
    db.Destroy()
    return result






#### --- Ввод нового остатка ---
def SetMateStore(mate_kod,store_name,q,cost):
    db = DBTools()
    store_name = store_name.encode("utf-8")
    q = q.encode("utf-8")
    cost = cost.encode("utf-8")
    cr=db.cnx.cursor()
    cr.execute("SELECT mr_SetMateStore(%s,'%s',%s,%s)" % (mate_kod,store_name,q,cost))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]






