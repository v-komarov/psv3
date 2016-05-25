#coding:utf-8

import	psycopg
import	wx
import	RWCfg
import	string


class DBTools:
    def __init__(self):
	host_=RWCfg.ReadValue('ServerDb')
	port_=5432
#	port_=8000
	base_=RWCfg.ReadValue('NameDb')
	user_=RWCfg.ReadValue('UserDb')
	pass_=RWCfg.ReadValue('PassDb')


	self.cnx=psycopg.connect("host='%s' port='%s' dbname='%s' user='%s' password='%s'" % (host_,port_,base_,user_,pass_))



    def Destroy(self):
	self.cnx.close()
	

#### --- Проверка доступности сервера (отклика) ---
    def CheckConnectServer(self):
	cr=self.cnx.cursor()
	cr.execute("select ps_checklogin()")
        self.cnx.commit()
	result=cr.fetchone()
	cr.close()
	return result[0]
    

#### --- Вывод списка должников (перечень адресов без привязки к услуги) ---
    def ShowAbonentPart2(self,UlDom):
	qarray = string.split(UlDom,':')
	cr = self.cnx.cursor()
	cr.execute(
	    "SELECT DISTINCT 			\
	    ps_rec_id as kod_ab, 		\
	    ps_ul, 				\
	    ps_dom, 				\
	    ps_kv, 				\
	    ps_p, 				\
	    to_number(ps_kv, '9999') as ps_kv2, \
	    to_char(ps_balans_total,'99990.99') as balans, \
	    ps_ls_sum as ls_sum, 		\
	    ps_cost as cost 			\
	    FROM ps_show_abonent_service 	\
	    WHERE ps_ls_sum<0 AND 		\
	    btrim(ps_ul)=btrim('%s') AND 	\
	    btrim(ps_dom)=btrim('%s')		\
	    ORDER BY ps_kv2" % (qarray[0],qarray[1]))
	self.cnx.commit()
	result=cr.fetchall()
	cr.close()
	return result












#### --- Получение списка услуг (названий) ---
    def GetListServices(self):
	result=[]
    	cr=self.cnx.cursor()
	cr.execute("select ps_services_name from ps_show_service_list")
	self.cnx.commit()
	for row in cr.fetchall():
	    result.append(row[0])
	cr.close()
	return result











#### --- Получение данных по сервисам для интерфейса тарифных планов ---
    def GetTarifServiceData(self,tp): 
	cr = self.cnx.cursor()
	tp2=tp.encode('utf-8')
	cr.execute("select * from ps_show_tarif_plan where ps_tarif_plan_name='%s'" % (tp2))
	self.cnx.commit()
	result = cr.fetchall()
	cr.close()    
	return result









#### --- Получение номеров домов  ---
    def GetListDom(self): 
	cr = self.cnx.cursor()
	cr.execute("select distinct ps_dom from ps_show_uldom_list")
	self.cnx.commit()
	result = cr.fetchall()
	cr.close()    
	return result




















































#### --- Вывод списка Internet пользователей ---
    def GetListInternetUser(self):
	cr = self.cnx.cursor()
	cr.execute("select address_user from vabonents where holding='tspk'")
	self.cnx.commit()
	result=cr.fetchall()
	cr.close()
	return result










#### --- Добавление нового тарифа стоимости 1МБ Internet трафика ---
    def	AddIntTarif(self,name,cost):
	name2 = name.encode('utf-8')
	cost2 = cost.encode('utf-8')
	cr = self.cnx.cursor()
	cr.execute("select in_AddTarif('%s','%s')" % (name2,cost2))
	self.cnx.commit()
	result=cr.fetchone()[0]
	cr.close()
	return result




#### --- Список Internet тарифов ---
    def	GetIntTarif(self):
	cr = self.cnx.cursor()
	cr.execute("select cost_name from in_show_tarif")
	self.cnx.commit()
	result=cr.fetchall()
	cr.close()
	return result



#### --- Получение данных по Internet тарифу ---
    def GetDataTarif(self,name):
	name2 = name.encode(utf-8)
	cr = self.cnx.cursor()
	cr.execute("select * from in_show_tarif where btrim(cost_name)=btrim('%s')" % (name2))
	self.cnx.commit()
	result=cr.fetchone()
	cr.close()
	return result
	


#### --- Изменение тарифа стоимости 1МБ Internet трафика ---
    def	UpdateIntTarif(self,rec,name,cost):
	name2 = name.encode('utf-8')
	cost2 = cost.encode('utf-8')
	cr = self.cnx.cursor()
	cr.execute("select in_UpdateTarif('%s','%s','%s')" % (rec,name2,cost2))
	self.cnx.commit()
	result=cr.fetchone()[0]
	cr.close()
	return result



#### --- Список Internet логинов (учетных записей) ---
    def	GetIntLogin(self):
	cr = self.cnx.cursor()
	cr.execute("select * from in_show_login")
	self.cnx.commit()
	result=cr.fetchall()
	cr.close()
	return result






#### --- Получение логина и пароля учетной записи Internet (для Карточки абонента) ---
    def	GetIntLoginPasswd(self,rec):
	cr = self.cnx.cursor()
	cr.execute("select in_user_login,in_user_passwd from in_account where in_rec_id=('%s') and in_rec_delete<>'delete'" % (rec))
	self.cnx.commit()
	result=cr.fetchone()
	cr.close()    
	return result




#### --- Получение данных одной, конкретной учетной записи ---
    def	GetIntLogin2(self,reckod):
	cr = self.cnx.cursor()
	cr.execute("select * from in_show_login where in_rec_id=('%s')" % (reckod))
	self.cnx.commit()
	result=cr.fetchone()
	cr.close()
	return result



#### --- Получение значения лицевого счета по услуге INTERNET ---
    def	GetIntLs(self,reckod):
	cr = self.cnx.cursor()
	cr.execute("select in_GetLs('%s')" % (reckod))
	self.cnx.commit()
	result=cr.fetchone()
	cr.close()
	return result[0]



#### --- Получение значения по трафику в текущем месяце ---
    def	GetMonthTraf(self,reckod):
	cr = self.cnx.cursor()
	cr.execute("select in_GetMonthTraf('%s')" % (reckod))
	self.cnx.commit()
	result=cr.fetchone()
	cr.close()
	return result[0]



#### --- Список удержаний за Internet трафик ---
    def	GetIntPay(self,rec):
	cr = self.cnx.cursor()
	cr.execute("select * from in_show_pay where in_rec_abonent=('%s') limit 500" % (rec))
	self.cnx.commit()
	result=cr.fetchall()
	cr.close()
	return result


#### --- Изменение пароля учетной записи Internet ---
    def	UpdatePasswd(self,reckod):
	cr = self.cnx.cursor()
	cr.execute("select in_UpdatePasswd('%s')" % (reckod))
	self.cnx.commit()
	result=cr.fetchone()
	cr.close()
	return result[0]



#### --- Изменение тарифа учетной записи Internet ---
    def	UpdateTarifAccount(self,reckod,tarif):
	tarif2 = tarif.encode('utf-8')
	cr = self.cnx.cursor()
	cr.execute("select in_UpdateTarifAccount('%s','%s')" % (reckod,tarif2))
	self.cnx.commit()
	result=cr.fetchone()
	cr.close()
	return result[0]



#### --- Удаление конкретной выбранной сесии (Internet трафик) ---
    def	DelTrafSes(self,kod_abonent,datetimeses):
	cr = self.cnx.cursor()
	cr.execute("select in_DelTrafPay('%s','%s')" % (kod_abonent,datetimeses))
	self.cnx.commit()
	result=cr.fetchone()
	cr.close()
	return result[0]




