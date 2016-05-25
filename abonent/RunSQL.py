#coding:utf-8


import	DBTools
from	RWCfg	import	ReadValue


#### --- Сохранение данных нового вводимого абонента в базе ---
def SaveNewAbonent(ul,dom,kv,tel,fio,tp,p):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    ul2 = ul.encode('utf-8')
    dom2 = dom.encode('utf-8')
    kv2 = kv.encode('utf-8')
    tel2 = tel.encode('utf-8')
    fio2 = fio.encode('utf-8')
    tp2 = tp.encode('utf-8')
    p2 = p.encode('utf-8')

    cr.execute("select ps_addabonent('%s','%s','%s','%s','%s','%s','%s')" % (ul2,dom2,kv2,tel2,fio2,tp2,p2))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]
    
    



#### --- Сохранение данных абонента в базе после редактирования ---
def SaveEditAbonent(db,kod,ul,dom,kv,tel,fio,tp,np):
    cr=db.cnx.cursor()
    ul2=ul.encode('utf-8')
    dom2=dom.encode('utf-8')
    kv2=kv.encode('utf-8')
    tel2=tel.encode('utf-8')
    fio2=fio.encode('utf-8')
    tp2=tp.encode('utf-8')
    np2=np.encode('utf-8')
    cr.execute("select ps_editabonent('%s','%s','%s','%s','%s','%s','%s','%s')" % (kod,ul2,dom2,kv2,tel2,fio2,tp2,np2))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result[0]
    
    
    
def FindAbonentDB(ul,dom,kv):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    ul2=ul.encode('utf-8')
    dom2=dom.encode('utf-8')
    kv2=kv.encode('utf-8')
    cr.execute("select ps_checkabonent('%s','%s','%s')" % (ul2,dom2,kv2))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]
	


#### --- Поиск абонента по номеру его лицевого счета ---
def FindLsp(lsp):
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    lsp2 = str(lsp).encode('utf-8')
    cr.execute("select ps_findlsp('%s')" % (lsp2))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    db.Destroy()
    return result[0]



#### --- Получение списка улиц ---
def GetListUl(db):
    cr=db.cnx.cursor()
    cr.execute("select ps_ul_name from ps_uls ORDER BY ps_ul_name")
    db.cnx.commit()
    list = []
    for row in cr.fetchall():
	list.append(row[0])
    cr.close()
    return list


#### --- Получение списка тарифных планов (названий) ---
def GetListTarifPlan(db):
    cr=db.cnx.cursor()
    cr.execute("select ps_tarif_plan_name from ps_show_tarif_plan_name")
    db.cnx.commit()
    list = []
    for row in cr.fetchall():
	list.append(row[0])
    cr.close()
    return list



#### --- Получение данный учетной записи абонента для редактирования ---
def GetAbonentData(db): 
    kod_rec = ReadValue('FoundRecord')
    cr=db.cnx.cursor()
    cr.execute("select * from ps_show_abonent_list where ps_rec_id='%s'" % (kod_rec))
    db.cnx.commit()
    list = []
    for row in cr.fetchone():
	list.append(row)
    cr.close()
    return list



#### --- Получение данный учетной записи абонента для карточки абонента ---
def GetAbonentData2(kod_rec): 
    db = DBTools.DBTools()
    cr=db.cnx.cursor()
    cr.execute("select * from ps_show_abonent_list where ps_rec_id='%s'" % (kod_rec))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    db.Destroy()
    return result



#### --- Ввод нового мак адреса ---
def AddMac(db,kod,t,mac):
    cr=db.cnx.cursor()
    cr.execute("SELECT in_AddMac('%s',%s,'%s')" % (str(kod),t,str(mac)))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result[0]



#### --- Получение списка MAC адресов ---
def GetListMac(db,kod_ab): 
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM in_show_mac WHERE in_abonent_kod='%s'" % (kod_ab))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    return result



#### --- Удаление мак адреса ---
def DelMac(db,kod):
    cr=db.cnx.cursor()
    cr.execute("SELECT in_DelMac('%s')" % (kod))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result[0]



#### --- Получение списка заявок ---
def GetListTask(db,kod_ab): 
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM ps_show_task WHERE abonent_id='%s'" % (kod_ab))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    return result



#### --- Получение списка материалов ---
def GetListMate(db,kod_ab): 
    cr=db.cnx.cursor()
    cr.execute("SELECT * FROM ps_show_mate WHERE abonent_kod='%s'" % (kod_ab))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    return result



#### --- Получение списка лицевых счетов абонента и определение статуса услуг ---
def ShowLSStatus(db, kod_ab):
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM ps_show_status_service WHERE abonent_kod=btrim('%s')" % (kod_ab))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    return result


#### --- Определение статуса услуги ---
def ShowLSStatus2(db, kod_ab, kod_ser):
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM ps_getstatusservice('%s','%s')" % (kod_ab,kod_ser))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result


#### --- Список заметок ---
def ListMess(db, kod_ab):
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM ps_show_messages WHERE ps_abonent_kod='%s'" % (kod_ab))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    return result


#### --- Получение списка прочих платежей ---
def GetMoneyOther(db, kod_ab):
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM ps_show_pay_in_other WHERE ps_abonent_kod='%s'" % (kod_ab))
    db.cnx.commit()
    result=cr.fetchall()
    cr.close()
    return result


#### --- Получение данных по платежам абонента ---
def GetMoneyInfoList(db,kod_ab): 
    cr = db.cnx.cursor()
    cr.execute("select * from ps_show_pay_in where ps_abonent_kod='%s'" % (kod_ab))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()    
    return result


#### --- Получение данных по удержаниям ---
def GetMoneyOutList(db,kod_ab): 
    cr = db.cnx.cursor()
    cr.execute("select * from ps_show_pay_out where ps_abonent_kod='%s' limit 200" % (kod_ab))
    db.cnx.commit()
    result = cr.fetchall()
    cr.close()    
    return result



#### --- Получение общего баланса абонента ---
def ShowBalans(db,kod):
    cr = db.cnx.cursor()
    cr.execute("select ps_ShowBalans('%s')" % (kod))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result[0]    



#### --- Удаление записи из ps_pay_in ---
def DelInto(db,kod):
    cr = db.cnx.cursor()
    cr.execute("select ps_del4payinto('%s')" % (kod))
    db.cnx.commit()
    cr.close()    



#### --- Добавление нового платежа ---
def AddMoneyInto(db,kod_ab,serv,pay_sum):
    cr = db.cnx.cursor()
    serv2=serv.encode('utf-8')
    pay_sum2=pay_sum.encode('utf-8')
    cr.execute("select ps_addmoneyinto('%s','%s','%s')" % (kod_ab, serv2, pay_sum2))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result[0]



#### --- Получение значения комментария из платежей для последующего редактирования  ---
def GetCommentPayIn(db,kod):
    cr = db.cnx.cursor()
    cr.execute("select info from ps_show_pay_in where ps_rec_id='%s'" % (kod))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    return result[0]    




#### --- Добавление коментария в таблицу ps_pay_in ---
def AddCommentInto(db,kod,comment):
    cr = db.cnx.cursor()
    comment2=comment.encode('utf-8')
    cr.execute("select ps_addcomment4payinto('%s','%s')" % (kod,comment2))
    db.cnx.commit()
    cr.close()    



#### --- Получение значения комментария из удержаний для последующего редактирования  ---
def GetCommentPayOut(db,kod):
    cr = db.cnx.cursor()
    cr.execute("select info from ps_show_pay_out where ps_rec_id='%s'" % (kod))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    return result[0]    




#### --- Добавление коментария в таблицу ps_pay_out ---
def AddCommentOut(db,kod,comment):
    cr = db.cnx.cursor()
    comment2=comment.encode('utf-8')
    cr.execute("select ps_addcomment4payout('%s','%s')" % (kod,comment2))
    db.cnx.commit()
    cr.close()    



#### --- Удаление записи из ps_pay_out ---
def DelOut(db,kod):
    cr = db.cnx.cursor()
    cr.execute("select ps_del4payout('%s')" % (kod))
    db.cnx.commit()
    cr.close()    




#### --- Добавление нового удержания ---
def AddMoneyOut(db,kod_ab,serv,pay_sum):
    cr = db.cnx.cursor()
    serv2=serv.encode('utf-8')
    pay_sum2=pay_sum.encode('utf-8')
    cr.execute("select ps_addmoneyout('%s','%s','%s')" % (kod_ab, serv2, pay_sum2))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result[0]




#### --- Ввод нового прочего платежа ---
def EnterMoneyOther(db, kod_ab, naz, sum):
    naz2 = naz.encode('utf-8')
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM ps_addmoneyother('%s','%s','%s')" % (kod_ab,naz2,sum))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result



#### --- Удаление прочего платежа ---
def DelOther(db, kod):
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM ps_delpayintoother('%s')" % (kod))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result



#### --- Получение значения комментария из прочих платежей для последующего редактирования  ---
def GetCommentPayOther(db,kod):
    cr = db.cnx.cursor()
    cr.execute("select ps_info from ps_show_pay_in_other where ps_rec_id='%s'" % (kod))
    db.cnx.commit()
    result = cr.fetchone()
    cr.close()
    return result[0]    



#### --- Добавление коментария прочего платежа ---
def AddCommentOther(db, kod, mess):
    mess2 = mess.encode('utf-8')
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM ps_addcomment4payother('%s','%s')" % (kod,mess2))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result



#### --- Новая заметка ---
def NewMess(db, kod_ab, mess):
    mess2 = mess.encode('utf-8')
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM ps_addmessage('%s','%s')" % (kod_ab,mess2))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result


#### --- Удаление заметки ---
def DelMess(db, kod_mess):
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM ps_delmessage('%s')" % (kod_mess))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result



#### --- Ввод начального остатка по услуге ---
def Ostatok(db,kod_ab,serv,pay_sum):
    cr = db.cnx.cursor()
    serv2=serv.encode('utf-8')
    pay_sum2=pay_sum.encode('utf-8')
    cr.execute("select ps_enterostatok('%s','%s','%s')" % (kod_ab, serv2, pay_sum2))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result[0]



#### --- Ввод начального остатка по услуге несмотря на то что движения (платежи и удержания) уже были ---
def Ostatok2(db,kod_ab,serv,pay_sum):
    cr = db.cnx.cursor()
    serv2=serv.encode('utf-8')
    pay_sum2=pay_sum.encode('utf-8')
    cr.execute("select ps_enterostatok2('%s','%s','%s')" % (kod_ab, serv2, pay_sum2))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result[0]




#### --- Перемещение остатка ---
def MoveOstatok(db, kod_ls, name_ser):
    name_ser2 = name_ser.encode('utf-8')
    cr = db.cnx.cursor()
    cr.execute("SELECT * FROM ps_moveostatok('%s','%s')" % (kod_ls,name_ser2))
    db.cnx.commit()
    result=cr.fetchone()
    cr.close()
    return result




#### --- Получение списка доступных для абонента услуг, согласно его тарифного плана  ---
def GetAbonentService(db,kod_ab):
    result=[]
    cr=db.cnx.cursor()
    cr.execute("select ps_services_name from ps_show_abonent_service where ps_rec_id='%s'" % (kod_ab))
    db.cnx.commit()
    for row in cr.fetchall():
	result.append(row[0])
    cr.close()
    return result



#### --- Получение списка доступных для абонента услуг, согласно его тарифного плана  ---
def GetAbonentService2(db,kod_ab):
    result=['']
    cr=db.cnx.cursor()
    cr.execute("select ps_services_name from ps_show_abonent_service where ps_rec_id='%s'" % (kod_ab))
    db.cnx.commit()
    for row in cr.fetchall():
	result.append(row[0])
    cr.close()
    return result

