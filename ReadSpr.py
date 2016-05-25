#coding:utf-8

""" Читаем справочники """


import	DBTools
import	RWCfg
import	wx
import	sys



### --- Справочник улиц для формы редактирования данных абонента ---
def ReadUl(Value):
    db = DBTools.DBTools()
    list = [Value]
    for p in db.GetListUl():
	if Value != p:
	    list.append(p)
    
    db.Destroy()
    return list



### --- Справочник тарифных планов для формы редактирования данных абонента ---    
def ReadTp(Value):
    db = DBTools.DBTools()
    list = [Value]
    for p in db.GetListTarifPlan():
	if Value != p:
	    list.append(p)

    db.Destroy()
    return list




### --- Получение данных для формы учетной записи ----
def GetAccount(rec):
    db = DBTools.DBTools()
    re = db.GetIntLogin2(rec)
    db.Destroy()
    return re





### --- Список сервисов (названия всех услуг) ---    
def ReadAllServices():
    db = DBTools.DBTools()
    list = []
    for p in db.GetListServices():
	    list.append(p)

    db.Destroy()
    return list





### --- Список Internet пользователей ---    
def ReadListInternetUser():
    db = DBTools.DBTools()
    list = []
    for p in db.GetListInternetUser():
	list.append(p[0])
    db.Destroy()
    return list


### --- Список Internet тарифов ---
def ReadIntTarif():
    db = DBTools.DBTools()
    list = []
    for p in db.GetIntTarif():
	list.append(p[0])
    db.Destroy()
    return list




### --- Получение логина и пароля учетной записи Internet для Карточки абонента ---
def GetIntLoginPasswd(rec):
    db = DBTools.DBTools()
    lp = db.GetIntLoginPasswd(rec)
    db.Destroy()
    return lp



##### ---- Форма списка Internet логинов ---- ####
class IntListLogin(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0),
                 size=(550,350), style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)


        self.InsertColumn(0, "Улица")
	self.InsertColumn(1, "Дом")
	self.InsertColumn(2, "Квартира")
	self.InsertColumn(3, "Логин")
	self.InsertColumn(4, "Телефон")
	self.InsertColumn(5, "Тариф")
	self.InsertColumn(6, "IP адрес")
	self.InsertColumn(7, "Дата и время")
	
	

    	self.SetColumnWidth(0, 150)
    	self.SetColumnWidth(1, 70)
    	self.SetColumnWidth(2, 70)
    	self.SetColumnWidth(3, 100)
    	self.SetColumnWidth(4, 100)
    	self.SetColumnWidth(5, 150)
    	self.SetColumnWidth(6, 150)
    	self.SetColumnWidth(7, 150)
	

    def Populate(self):

	self.DeleteAllItems()

#### --- Получение списка ---	
	db=DBTools.DBTools()


#### --- Отображение данных в форме ---
	self.kod_record=[] # массив идентификаторов записей
	for row in db.GetIntLogin():
	    str0=row[0]
	    str1=row[1]
	    str2=row[2]
	    str3=row[3]
	    str4=row[6]
	    str5=row[4]
	    str6=row[5]
	    str7=row[7]
	    str8=str(row[8])

	    index=self.InsertStringItem(sys.maxint, str0)
	    self.SetStringItem( index, 0, str1)
	    self.SetStringItem( index, 1, str2)
	    self.SetStringItem( index, 2, str3)
	    self.SetStringItem( index, 3, str4)
	    self.SetStringItem( index, 4, str5)
	    self.SetStringItem( index, 5, str6)
	    self.SetStringItem( index, 6, str7)
	    self.SetStringItem( index, 7, str8)

	# -- Заполнение массива идентификаторов записей ---
	    self.kod_record.append(row[0])    
	    
	db.Destroy()
	
	self.currentItem=0




##### ---- Форма учета Internet трафика ---- ####
class IntListTrafik(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0),
                 size=(200,350), style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)


        self.InsertColumn(0, "Дата")
	self.InsertColumn(1, "Время")
	self.InsertColumn(2, "Сумма")
	self.InsertColumn(3, "Счет до...")
	self.InsertColumn(4, "Счет после...")
	self.InsertColumn(5, "Трафик")
	self.InsertColumn(6, "Тариф")
	
	

    	self.SetColumnWidth(0, 100)
    	self.SetColumnWidth(1, 70)
    	self.SetColumnWidth(2, 100)
    	self.SetColumnWidth(3, 100)
    	self.SetColumnWidth(4, 100)
    	self.SetColumnWidth(5, 100)
    	self.SetColumnWidth(6, 200)
	

    def Populate(self,rec):

	self.DeleteAllItems()

#### --- Получение списка ---	
	db=DBTools.DBTools()


#### --- Отображение данных в форме ---
	self.kod_record=[] # массив идентификаторов записей
	for row in db.GetIntPay(rec):
	    str0=str(row[1])
	    str1=row[2]
	    str2=row[3]
	    str3=str(row[4])
	    str4=str(row[5])
	    str5=str(row[6])
	    str6=str(row[7])
	    str7=row[8]
	    
	    index=self.InsertStringItem(sys.maxint, str0)
	    self.SetStringItem( index, 0, str1)
	    self.SetStringItem( index, 1, str2)
	    self.SetStringItem( index, 2, str3)
	    self.SetStringItem( index, 3, str4)
	    self.SetStringItem( index, 4, str5)
	    self.SetStringItem( index, 5, str6)
	    self.SetStringItem( index, 6, str7)


	# -- Заполнение массива идентификаторов записей ---
	    self.kod_record.append(str0)    
	    
	db.Destroy()
	
	self.currentItem=0


