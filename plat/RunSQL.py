#coding:utf-8


import	DBTools
import	string





#### --- Вывод списка всех абонентов общим списком ---
def ShowAbonentTotal():
    db = DBTools.DBTools()
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM ps_show_abonent_list")
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    db.Destroy()
    return result




#### --- Загрузка внешних платежей в базу ---
def LoadPay(db,kod,ser,date,sum):
    cr = db.cnx.cursor()
    cr.execute("select ps_loadpay('%s','%s','%s','%s')" % (kod,ser,date,sum))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result[0]



#### --- Название файла из даты ---
def GetDateName(db):
    cr = db.cnx.cursor()
    cr.execute("SELECT to_char(current_date,'TSPK-YYYY-MM-DD.txt');")
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result[0]



#### --- Вывод списка абонентов бригантины ---
def ShowAbonentBrig(db,ul,dom):
    ul = ul.encode('utf-8')
    dom = dom.encode('utf-8')
    service = 'ДОМОФОН'
    cr = db.cnx.cursor()
    cr.execute("SELECT CASE WHEN ps_ls_sum<=(-60.0) THEN ps_ul||'#'||ps_dom||'#'||ps_kv||'#'||ps_services_name||'#-60.00' ELSE ps_ul||'#'||ps_dom||'#'||ps_kv||'#'||ps_services_name||'#'||btrim(to_char(ps_ls_sum,'9999990.00')) END AS row_str FROM ps_show_abonent_service WHERE ps_ul='%s' AND ps_dom='%s' AND ps_services_name='%s';" % (ul,dom,service))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    return result



#### --- Загрузка платежей Бригантины в базу ---
def LoadPay2(db,ul,dom,kv,service,datetime,sum):
    ul = ul.encode('utf-8')
    dom = dom.encode('utf-8')
    kv = kv.encode('utf-8')
    service = service.encode('utf-8')
    cr = db.cnx.cursor()
    cr.execute("SELECT ps_LoadPay2('%s','%s','%s','%s','%s', %s);" % (ul,dom,kv,service,datetime,sum))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result[0]



#### --- Загрузка внешних платежей в базу по КАСС ---
def LoadPay3(db,kod,ser,date,sum):
    cr = db.cnx.cursor()
    cr.execute("select ps_loadpay3('%s','%s','%s','%s')" % (kod,ser,date,sum))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result[0]




#### --- Загрузка внешних платежей в базу по CityPay ---
def LoadPay4(db,kod,ser,date,sum):
    cr = db.cnx.cursor()
    cr.execute("select ps_loadpay4('%s','%s','%s','%s')" % (kod,ser,date,sum))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result[0]
