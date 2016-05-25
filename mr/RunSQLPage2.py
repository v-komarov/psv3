#coding:utf-8


from	DBTools	import	DBTools






#### --- Получение списка расхода по заявкам ---
def GetListMateTask(mate_kod):
    db = DBTools()
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM mr_show_mate_page WHERE mate_kod=%s;" % (mate_kod))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()
    db.Destroy()
    return result






