#coding:utf-8


import	DBTools
from	RWCfg	import	ReadValue



#### --- Получение списка тарифных планов (названий) ---
def GetListTarifPlan():
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("select ps_tarif_plan_name from ps_show_tarif_plan_name")
    db.cnx.commit()
    list = []
    for row in cr.fetchall():
	list.append(row[0])
    cr.close()
    db.Destroy()
    return list



#### --- Добавление нового тарифного плана ---
def NewTarifPlan(NamePlan):
    db = DBTools.DBTools()
    name = NamePlan.encode('utf-8')
    cr=db.cnx.cursor()
    cr.execute("select ps_addtarifplan('%s')" % (name))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]



#### --- Переименование тарифного плана ---
def ReNameTarifPlan(NamePlanOld, NamePlanNew):
    db = DBTools.DBTools()
    NameOld = NamePlanOld.encode('utf-8')
    NameNew = NamePlanNew.encode('utf-8')
    cr=db.cnx.cursor()
    cr.execute("select ps_renametarifplan('%s','%s')" % (NameOld, NameNew))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]


#### --- Добавление услуги к тарифному плану ---
def AddService(NameService, NamePlan):	
    db = DBTools.DBTools()
    NameS = NameService.encode('utf-8')
    NameP = NamePlan.encode('utf-8')
    cr=db.cnx.cursor()
    cr.execute("select ps_addser2tplan('%s','%s',0)" % (NameS, NameP))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]



#### --- Установка стоимости услуги в тарифном плане ---
def SetCostService(rec_kod, cost_ser):	
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("select ps_setcostserviceoftplan('%s','%s')" % (rec_kod, cost_ser))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]



#### --- Удаление услуги из тарифного плана ---
def DelSerFromTP(kod):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("select ps_delserfromtplan('%s')" % (kod))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]


