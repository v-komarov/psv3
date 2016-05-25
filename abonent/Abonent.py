#coding:utf-8

""" Интерфейс изменения данных абонента, ввода и отображения платежей и удержаний """


import  wx
import	RWCfg
import	ReadSpr
import	Check
import	MoneyIntoLs
import	MoneyOutLs
import	MessageList
import	LSList
import	Net
import	NewPay
import	TaskList
import	MateList
import	wx.lib.printout as printout
from	abonent.RunSQL	import	ShowBalans
from	abonent.RunSQL	import	SaveEditAbonent
from	abonent.RunSQL	import	GetListUl
from	abonent.RunSQL	import	GetListTarifPlan
from	abonent.RunSQL	import	GetAbonentData
from	abonent.RunSQL	import	AddMac
from	abonent.RunSQL	import	DelMac
from	abonent.RunSQL	import	AddMoneyInto
from	abonent.RunSQL	import	DelInto
from	abonent.RunSQL	import	GetCommentPayIn
from	abonent.RunSQL	import	AddCommentInto
from	abonent.RunSQL	import	AddMoneyOut
from	abonent.RunSQL	import	DelOut
from	abonent.RunSQL	import	GetCommentPayOut
from	abonent.RunSQL	import	AddCommentOut
from	abonent.RunSQL	import	EnterMoneyOther
from	abonent.RunSQL	import	DelOther
from	abonent.RunSQL	import	GetCommentPayOther
from	abonent.RunSQL	import	AddCommentOther
from	abonent.RunSQL	import	NewMess
from	abonent.RunSQL	import	DelMess
from	abonent.RunSQL	import	Ostatok
from	abonent.RunSQL	import	Ostatok2
from	abonent.RunSQL	import	MoveOstatok
from	abonent.RunSQL	import	GetAbonentService
from	report.PrintData	import CartAbonent	as	CartAbonent2
from	report.PrintData	import CheckAbonent
from	report.PrintData	import	ListAct
from	report.PeriodForm	import	GetPeriodService
from	tools.Messages		import	ErrorValue
from	DBTools	import	DBTools




class Abonent(wx.Frame):
    def __init__(self,parent,ID,title, pos=wx.DefaultPosition,
            size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE
	):


	### -- Соединение с базой данных ---
	db = DBTools()


#### --- Предварительная подготовка данных ---


#### --- Получение данных учетной записи абонента ---
	self.re = GetAbonentData(db)



        wx.Frame.__init__(self,parent,ID, title, pos, size, style)
        panel = wx.Panel(self, -1)
	
	mainsizer = wx.BoxSizer(wx.VERTICAL)

	tID = wx.NewId()


#### --- Заголовок ---
	sizer = wx.BoxSizer(wx.HORIZONTAL)
	topLbl = wx.StaticText(panel, -1, "Данные абонента")
	topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
	sizer.Add(topLbl, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_LEFT|wx.ALL, 5)
	mainsizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)

#### --- Первая строка интерфейса ---
	sizer = wx.BoxSizer(wx.HORIZONTAL)
	label = wx.StaticText(panel, -1, "Улица")
        self.cb0 = wx.ComboBox(panel, -1,"", size=(150, -1),choices=GetListUl(db), style=wx.CB_DROPDOWN|wx.CB_READONLY)		
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.cb0, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

	label = wx.StaticText(panel, -1, "Дом")
        self.field2 = wx.TextCtrl(panel, -1, "")
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field2, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

	label = wx.StaticText(panel, -1, "Квартира")
        self.field3 = wx.TextCtrl(panel, -1, "")
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field3, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

	label = wx.StaticText(panel, -1, "Под.")
        self.field8 = wx.TextCtrl(panel, -1, "" , size=(30,-1))
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field8, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_LEFT|wx.ALL, 5)




#### --- Вторая строка интерфейса ---
	sizer = wx.BoxSizer(wx.HORIZONTAL)
	label = wx.StaticText(panel, -1, "Телефон")
        self.field4 = wx.TextCtrl(panel, -1, "")
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field4, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

	label = wx.StaticText(panel, -1, "Контакт", pos=(240,50))
        self.field5 = wx.TextCtrl(panel, -1, "",pos=(290,50),size=(290, -1))
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field5, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_LEFT|wx.ALL, 5)




#### --- Третья строка интерфейса ---
	sizer = wx.BoxSizer(wx.HORIZONTAL)
	label = wx.StaticText(panel, -1, "Баланс", pos=(10,90))
        self.field6 = wx.TextCtrl(panel, -1, "",pos=(60,90),size=(80, -1), style=wx.TE_READONLY)
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field6, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

	label = wx.StaticText(panel, -1, "Тарифный план", pos=(240,90))
        self.cb1 = wx.ComboBox(panel, -1, "", size=(300, -1),choices=GetListTarifPlan(db), style=wx.CB_DROPDOWN|wx.CB_READONLY)
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.cb1, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_LEFT|wx.ALL, 5)




#### --- Четвертая строка интерфейса ---
	sizer = wx.BoxSizer(wx.HORIZONTAL)
	label = wx.StaticText(panel, -1, "Номер лицевого счёта")
        self.field7 = wx.TextCtrl(panel, -1, "", size=(150, -1), style=wx.TE_READONLY)
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field7, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_LEFT|wx.ALL, 5)



#### --- Кнопки Сохранения и закрытия формы ----
	mainsizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
	sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.button2 = wx.Button(panel, 1003, "Сохранить")
        self.button22 = wx.Button(panel, 1022, "Карточка абонента")
        self.button23 = wx.Button(panel, 1023, "Копия чека")
        self.button24 = wx.Button(panel, 1024, "Копия чека +")
        self.button10 = wx.Button(panel, 1005, "Закрыть")
	sizer.Add(self.button2, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.button22, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.button23, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.button24, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.button10, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_CENTER|wx.ALL, 5)
	sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.button26 = wx.Button(panel, 1026, "Акт сверки")
	sizer.Add(self.button26, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_CENTER|wx.ALL, 5)
	mainsizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)


#### --- Форма с закладками ----
	sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.note = wx.Notebook(panel, -1)
	sizer.Add(self.note, 0, wx.ALIGN_CENTRE|wx.ALL|wx.GROW, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_CENTER|wx.ALL|wx.GROW, 5)


#### --- Первая закладка ---
	page1 = self.Page()
	pagesizer = wx.BoxSizer(wx.VERTICAL)
	self.ctrl1 = MoneyIntoLs.MoneyInto(page1, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl1.Populate(db,self.re[0])
	self.button3 = wx.Button(page1, 1003, "Новый платеж")
	pagesizer.Add(self.ctrl1, 0, wx.ALIGN_CENTER|wx.ALL, 5)
	pagesizer.Add(self.button3, 0, wx.ALIGN_CENTER|wx.ALL, 5)
	page1.SetSizer(pagesizer)
	pagesizer.Fit(self)


#### --- Вторая закладка ---	
	page2 = self.Page()
	pagesizer = wx.BoxSizer(wx.VERTICAL)
	self.ctrl2 = MoneyOutLs.MoneyOut(page2, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl2.Populate(db,self.re[0])
	self.button4 = wx.Button(page2, 1004, "Новое удержание")
	pagesizer.Add(self.ctrl2, 0, wx.ALIGN_CENTER|wx.ALL, 5)
	pagesizer.Add(self.button4, 0, wx.ALIGN_CENTER|wx.ALL, 5)
	page2.SetSizer(pagesizer)
	pagesizer.Fit(self)


#### --- Третья закладка ---
	page3 = self.Page()
	pagesizer = wx.BoxSizer(wx.VERTICAL)
	self.ctrl3 = MoneyIntoLs.OtherInto(page3, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl3.Populate(db,self.re[0])
	self.button5 = wx.Button(page3, 1005, "Новый платеж")
	pagesizer.Add(self.ctrl3, 0, wx.ALIGN_CENTER|wx.ALL, 5)
	pagesizer.Add(self.button5, 0, wx.ALIGN_CENTER|wx.ALL, 5)
	page3.SetSizer(pagesizer)
	pagesizer.Fit(self)


#### --- Четвертая закладка ---
	page4 = self.Page()
	pagesizer = wx.BoxSizer(wx.VERTICAL)
	self.ctrl4 = MessageList.MList(page4, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl4.Populate(db,self.re[0])
	self.button6 = wx.Button(page4, 1006, "Новая заметка")
	pagesizer.Add(self.ctrl4, 0, wx.ALIGN_CENTER|wx.ALL, 5)
	pagesizer.Add(self.button6, 0, wx.ALIGN_CENTER|wx.ALL, 5)
	page4.SetSizer(pagesizer)
	pagesizer.Fit(self)


#### --- Пятая закладка ---
	page5 = self.Page()
	pagesizer = wx.BoxSizer(wx.VERTICAL)
	self.ctrl5 = LSList.List(page5, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl5.Populate(db,self.re[0])
	self.button0 = wx.Button(page5, 1007, "Ввод остатка")
	pagesizer.Add(self.ctrl5, 0, wx.ALIGN_CENTER|wx.ALL, 5)
	pagesizer.Add(self.button0, 0, wx.ALIGN_CENTER|wx.ALL, 5)
	page5.SetSizer(pagesizer)
	pagesizer.Fit(self)



#### --- Шестая закладка ---
	page6 = self.Page()
	pagesizer = wx.BoxSizer(wx.VERTICAL)
	self.ctrl6 = Net.List(page6, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl6.Populate(db,self.re[0])
	self.ctrl6.SetItemState(0,wx.LIST_STATE_SELECTED,wx.LIST_STATE_SELECTED)
	self.button7add = wx.Button(page6, 1008, "Добавить")
	self.button7del = wx.Button(page6, 1009, "Удалить")
	pagesizer.Add(self.ctrl6, 0, wx.ALIGN_CENTER|wx.ALL, 5)
	sizer6 = wx.BoxSizer(wx.HORIZONTAL)
	sizer6.Add(self.button7add, 0, wx.ALIGN_CENTER|wx.ALL, 5)
	sizer6.Add(self.button7del, 0, wx.ALIGN_CENTER|wx.ALL, 5)
	pagesizer.Add(sizer6, 0, wx.ALIGN_CENTER|wx.ALL, 5)
	page6.SetSizer(pagesizer)
	pagesizer.Fit(self)




#### --- Седьмая закладка ---
	page7 = self.Page()
	pagesizer = wx.BoxSizer(wx.VERTICAL)
	self.ctrl7 = TaskList.List(page7, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl7.Populate(db,self.re[0])
	self.ctrl7.SetItemState(0,wx.LIST_STATE_SELECTED,wx.LIST_STATE_SELECTED)
	pagesizer.Add(self.ctrl7, 0, wx.ALIGN_CENTER|wx.ALL, 5)
	page7.SetSizer(pagesizer)
	pagesizer.Fit(self)




#### --- Восьмая закладка ---
	page8 = self.Page()
	pagesizer = wx.BoxSizer(wx.VERTICAL)
	self.ctrl8 = MateList.List(page8, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl8.Populate(db,self.re[0])
	self.ctrl8.SetItemState(0,wx.LIST_STATE_SELECTED,wx.LIST_STATE_SELECTED)
	pagesizer.Add(self.ctrl8, 0, wx.ALIGN_CENTER|wx.ALL, 5)
	page8.SetSizer(pagesizer)
	pagesizer.Fit(self)



	### --- Отключение от базы данных ---
	db.Destroy()

	### --- Вставка данных ---
	self.ShowData(self.re)


	
	self.note.AddPage(page1,'Платежи')
	self.note.AddPage(page2,'Удержания')
	self.note.AddPage(page3,'Прочие платежи')
	self.note.AddPage(page4,'Заметки/История')
	self.note.AddPage(page5,'Лицевые счета')
	self.note.AddPage(page6,'MAC')
	self.note.AddPage(page7,'Заявки')
	self.note.AddPage(page8,'Материалы')




	panel.SetSizer(mainsizer)
	mainsizer.Fit(self)

#### --- Обработка событий ----
	self.button2.Bind(wx.EVT_BUTTON, self.SaveData, self.button2)	
	self.button22.Bind(wx.EVT_BUTTON, self.CartAbonent, self.button22)	
	self.button23.Bind(wx.EVT_BUTTON, self.Check, self.button23)	
	self.button24.Bind(wx.EVT_BUTTON, self.Check_adv, self.button24)
	self.button26.Bind(wx.EVT_BUTTON, self.Act, self.button26)	
	self.button0.Bind(wx.EVT_BUTTON, self.EnterOstatok, self.button0)	
	self.button6.Bind(wx.EVT_BUTTON, self.EnterMessage, self.button6)	
	self.button10.Bind(wx.EVT_BUTTON, self.OnCloseWindow, self.button10)	
	self.button7add.Bind(wx.EVT_BUTTON, self.AddMAC, self.button7add)	
	self.button7del.Bind(wx.EVT_BUTTON, self.DelMAC, self.button7del)	
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

	self.ctrl1.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.ShowMenu1, self.ctrl1)	
	self.ctrl1.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem1, self.ctrl1)
	self.ctrl2.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.ShowMenu2, self.ctrl2)	
	self.ctrl2.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem2, self.ctrl2)
	self.ctrl3.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.ShowMenu3, self.ctrl3)	
	self.ctrl3.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem3, self.ctrl3)
	self.ctrl4.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.ShowMenu4, self.ctrl4)	
	self.ctrl4.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem4, self.ctrl4)
	self.ctrl5.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.ShowMenu5, self.ctrl5)	
	self.ctrl5.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem5, self.ctrl5)
	self.ctrl6.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem6, self.ctrl6)

        self.button3.Bind(wx.EVT_BUTTON, self.NewMoneyInto, self.button3)
        self.button4.Bind(wx.EVT_BUTTON, self.NewMoneyOut, self.button4)
	self.button5.Bind(wx.EVT_BUTTON, self.NewMoneyOther, self.button5)	



    #### ---- Вставка данных в поля ввода ---
    def ShowData(self,re):
	self.cb0.SetValue(re[1])
	self.field2.SetValue(re[2])
	self.field3.SetValue(re[3])
	self.field8.SetValue(re[10])
	self.field4.SetValue(re[5])
	self.field5.SetValue(re[6])
	self.field6.SetValue(re[4])
	self.cb1.SetValue(re[7])
	self.field7.SetValue(re[9])






    def OnCloseWindow(self, event):
        self.Destroy()



#### --- Страница закладки ----
    def Page(self):
	return wx.Panel(self.note, -1)


        
#### --- Карточка абонента ---
    def CartAbonent(self,event):
	CartAbonent2(self.re[0])


#### --- Копия чека ---
    def	Check(self,event):
	address = 'ул '+self.re[1]+', дом '+self.re[2]+', кв. '+self.re[3]
	CheckAbonent(self.re[0],address,self.re[9])
    

#### --- Копия чека с объявлением ---
    def	Check_adv(self,event):
	address = 'ул '+self.re[1]+', дом '+self.re[2]+', кв. '+self.re[3]
	CheckAbonent(self.re[0],address,self.re[9],adv=1)


#### --- Печатная форма акта сверки ---
    def	Act(self,event):
	dlg = GetPeriodService(self,-1,"Период", size=(350,200), style = wx.DEFAULT_DIALOG_STYLE)
	if dlg.ShowModal() == wx.ID_OK:
	    date0 = str(dlg.field_0.GetValue().GetYear())+'-' + str(dlg.field_0.GetValue().GetMonth()+1) +'-'+ str(dlg.field_0.GetValue().GetDay())
	    date1 = str(dlg.field_1.GetValue().GetYear())+'-' + str(dlg.field_1.GetValue().GetMonth()+1) +'-'+ str(dlg.field_1.GetValue().GetDay())
	    periodstr = str(str(dlg.field_0.GetValue().GetDay())+'.'+str(dlg.field_0.GetValue().GetMonth()+1)+'.'+str(dlg.field_0.GetValue().GetYear())+' - '+str(dlg.field_1.GetValue().GetDay())+'.'+str(dlg.field_1.GetValue().GetMonth()+1)+'.'+str(dlg.field_1.GetValue().GetYear()))
	    service = dlg.field_2.GetValue()
	    if service == '':
		ErrorValue(self)
	    else:
		address_str = 'ул '+self.re[1]+', дом '+self.re[2]+', кв. '+self.re[3]
		ListAct(self.re[0],date0,date1,periodstr,service,address_str)
	dlg.Destroy()
	


    

#### --- Сохранение данных абонента ---
    def SaveData(self,event):
	rec=self.re[0]
	ul=self.cb0.GetValue()
	dom=self.field2.GetValue()
	kv=self.field3.GetValue()
	tel=self.field4.GetValue()
	fio=self.field5.GetValue()
	tp=self.cb1.GetValue()
	np=self.field8.GetValue()

	db = DBTools()


	save_ok=SaveEditAbonent(db,rec,ul,dom,kv,tel,fio,tp,np)

	if save_ok!='OK':
	
	    dlg1=wx.MessageDialog(self,'Проверьте корректность данных!','Ошибка сохранения',wx.OK)
	    dlg1.ShowModal()
	    dlg1.Destroy()
	    
	else:
	
	### --- Освежить данные в полях формы ---
	    self.ShowData(GetAbonentData(db))
	
	    dlg2=wx.MessageDialog(self,'Данные абонента сохранены!','Сохранение',wx.OK)
	    dlg2.ShowModal()
	    dlg2.Destroy()
	### -- Освежить форму спсика лицевых счетов ---
	    self.ctrl5.Populate(db,self.re[0])
    
	    db.Destroy()	
		


#### --- Обновление информации формы общего баланса ---
    def ReFreshBalans(self,db):
	self.field6.SetValue(ShowBalans(db,self.re[0]))



#### --- Ввод начальных остатков ---
    def EnterOstatok(self,event):
	import NewPay
	# -- Передача кода абонента в форму диалога через запись в файл ---
	RWCfg.WriteValue('IDAbonent', self.re[0])

	dlg=NewPay.Ostatok(self,-1,"Начальные остатки", size=(350,200), style=wx.DEFAULT_DIALOG_STYLE)
	dlg.Centre()
	if dlg.ShowModal()==wx.ID_OK:
	    ser=dlg.ch
	    sum=dlg.text0.GetValue()
	    db=DBTools()
	    if Ostatok(db,self.re[0], ser, sum)=='OK':
		self.ReFreshBalans(db)
		self.ctrl5.Populate(db,self.re[0])
		self.ctrl4.Populate(db,self.re[0])
			    
	    else:
		#### --- Даже при наличии движений по услуге иногда необходимо ввести остаток
		#### --- Запрос пароля на подтверждение ввода остатка
		dlg2=wx.TextEntryDialog(self, 'При наличии платежей и удержаний по услуге\nввод остаков по этой услуге требует подтверждения.','Ввод пароля', '', style=wx.TE_PASSWORD|wx.OK|wx.CANCEL)
		if dlg2.ShowModal() == wx.ID_OK:
		    if dlg2.GetValue() == RWCfg.ReadValue('PassDb'):
			### --- Пароль верный - операция принимается к выполнению ---
			if Ostatok2(db,self.re[0], ser, sum)=='OK':
			    ### --- Сообщение об успешности операции ---
			    self.ReFreshBalans(db)
			    self.ctrl5.Populate(db,self.re[0])
			    self.ctrl4.Populate(db,self.re[0])
#			    dlg3=wx.MessageDialog(self,'Остаток введен!','Сообщение', wx.OK|wx.ICON_INFORMATION)
#			    dlg3.ShowModal()
#			    dlg3.Destroy()
			else:
			    ### --- Сообщение об неизвестной причине по которой операция не выполнена ---
			    dlg3=wx.MessageDialog(self,'Остаток не введен!\nТип ошибки не известен.','Ошибка', wx.OK|wx.ICON_INFORMATION)
			    dlg3.ShowModal()
			    dlg3.Destroy()

		    else:
			### --- Сообщение о том что пароль не верный ---
			dlg3=wx.MessageDialog(self,'Остаток не введен!\nПароль не верный!','Ошибка', wx.OK|wx.ICON_INFORMATION)
			dlg3.ShowModal()
			dlg3.Destroy()
			
			
		dlg2.Destroy()
	    	
	    db.Destroy()

	dlg.Destroy()	




#### --- Присвоение значения по выбранной строке платежа ---
    def ReadItem1(self,event):
	self.ctrl1.currentItem = event.m_itemIndex


#### --- Присвоение значения по выбранной строке удержания ---
    def ReadItem2(self,event):
	self.ctrl2.currentItem = event.m_itemIndex


#### --- Присвоение значения по выбранной строке  ---
    def ReadItem3(self,event):
	self.ctrl3.currentItem = event.m_itemIndex


#### --- Присвоение значения по выбранной строке заметки ---
    def ReadItem4(self,event):
	self.ctrl4.currentItem = event.m_itemIndex


#### --- Присвоение значения по выбранной строке лицевого счета ---
    def ReadItem5(self,event):
	self.ctrl5.currentItem = event.m_itemIndex


#### --- Присвоение значения по выбранной строке MAC адреса ---
    def ReadItem6(self,event):
	self.ctrl6.currentItem = event.m_itemIndex

	

#### --- Меню для списка платежей ---
    def	ShowMenu1(self,event):
	self.popupID1=wx.NewId()
	self.popupID2=wx.NewId()
	self.menu1=wx.Menu()
	self.menu1.Append(self.popupID1,"Примечание") 
	self.menu1.Append(self.popupID2,"Удалить")
	self.menu1.Bind(wx.EVT_MENU, self.MakeInfo1, id=self.popupID1)
	self.menu1.Bind(wx.EVT_MENU, self.Delete1, id=self.popupID2)
	self.PopupMenu(self.menu1)
	self.menu1.Destroy() 



#### --- Меню для списка удержаний ---
    def	ShowMenu2(self,event):
	self.popupID3=wx.NewId()
	self.popupID4=wx.NewId()
	self.menu2=wx.Menu()
	self.menu2.Append(self.popupID3,"Примечание") 
	self.menu2.Append(self.popupID4,"Удалить")
	self.menu2.Bind(wx.EVT_MENU, self.MakeInfo2, id=self.popupID3)
	self.menu2.Bind(wx.EVT_MENU, self.Delete2, id=self.popupID4)
	self.PopupMenu(self.menu2)
	self.menu2.Destroy() 



#### --- Меню для списка прочих платежей ---
    def	ShowMenu3(self,event):
	self.popupID5=wx.NewId()
	self.popupID6=wx.NewId()
	self.menu3=wx.Menu()
	self.menu3.Append(self.popupID5,"Примечание") 
	self.menu3.Append(self.popupID6,"Удалить")
	self.menu3.Bind(wx.EVT_MENU, self.MakeInfo3, id=self.popupID5)
	self.menu3.Bind(wx.EVT_MENU, self.Delete3, id=self.popupID6)
	self.PopupMenu(self.menu3)
	self.menu3.Destroy() 



#### --- Меню для списка заметок ---
    def	ShowMenu4(self,event):
	self.popupID88=wx.NewId()
	self.menu4=wx.Menu()
	self.menu4.Append(self.popupID88,"Удалить земетку") 
	self.menu4.Bind(wx.EVT_MENU, self.DeleteMessage, id=self.popupID88)
	self.PopupMenu(self.menu4)
	self.menu4.Destroy() 



#### --- Меню для списка лицевых счетов ---
    def	ShowMenu5(self,event):
	self.popupID99=wx.NewId()
	self.menu5=wx.Menu()
	self.menu5.Append(self.popupID99,"Перенести остатки") 
	self.menu5.Bind(wx.EVT_MENU, self.MoveOstatok, id=self.popupID99)
	self.PopupMenu(self.menu5)
	self.menu5.Destroy() 



#### --- Добавление коментария к записи платежа ---	
    def MakeInfo1(self,event):
	item=self.ctrl1.currentItem
	kod=self.ctrl1.ps_rec_id[item]
#### --- Предыдущее значение примечания ---
	db=DBTools()
	messold = GetCommentPayIn(db,kod)
	db.Destroy()	    

	dlg=wx.TextEntryDialog(self,'Введите текст примечания','Примечание')
	dlg.SetValue(messold)
	if dlg.ShowModal()==wx.ID_OK:
	    mess=dlg.GetValue()
	    db=DBTools()
	    AddCommentInto(db,kod,mess)
	    self.ctrl1.Populate(db,self.re[0])
	    db.Destroy()	    

	dlg.Destroy()



#### --- Удаление записи платежа ---	
    def Delete1(self,event):
	item=self.ctrl1.currentItem
	kod=self.ctrl1.ps_rec_id[item]
	
##	dlg=wx.MessageDialog(self,'Удалить запись?','Удаление')

	dlg=wx.TextEntryDialog(self, 'Действие требует подтверждения.','Ввод пароля', '', style=wx.TE_PASSWORD|wx.OK|wx.CANCEL)
	if dlg.ShowModal() == wx.ID_OK:
	    if dlg.GetValue() == RWCfg.ReadValue('PassDb'):
##	if dlg.ShowModal()==wx.ID_OK:
		db=DBTools()
		DelInto(db,kod)
		self.ctrl1.Populate(db,self.re[0])
		self.ReFreshBalans(db)
		self.ctrl5.Populate(db,self.re[0])
		db.Destroy()	    

	dlg.Destroy()
	


#### --- Добавление коментария к записи удержания ---	
    def MakeInfo2(self,event):
	item=self.ctrl2.currentItem
	kod=self.ctrl2.ps_rec_id[item]
#### --- Предыдущее значение примечания ---
	db=DBTools()
	messold = GetCommentPayOut(db,kod)
	db.Destroy()	    

	dlg=wx.TextEntryDialog(self,'Введите текст примечания','Примечание')
	dlg.SetValue(messold)
	if dlg.ShowModal()==wx.ID_OK:
	    mess=dlg.GetValue()
	    db=DBTools()
	    AddCommentOut(db,kod,mess)
	    self.ctrl2.Populate(db,self.re[0])
	    db.Destroy()	    

	dlg.Destroy()
	    


#### --- Удаление записи удержания ---	
    def Delete2(self,event):
	item=self.ctrl2.currentItem
	kod=self.ctrl2.ps_rec_id[item]


##	dlg=wx.MessageDialog(self,'Удалить запись?','Удаление')

	dlg=wx.TextEntryDialog(self, 'Действие требует подтверждения.','Ввод пароля', '', style=wx.TE_PASSWORD|wx.OK|wx.CANCEL)
	if dlg.ShowModal() == wx.ID_OK:
	    if dlg.GetValue() == RWCfg.ReadValue('PassDb'):


##	if dlg.ShowModal()==wx.ID_OK:
		db=DBTools()
		DelOut(db,kod)
		self.ctrl2.Populate(db,self.re[0])
		self.ReFreshBalans(db)
		self.ctrl5.Populate(db,self.re[0])
		db.Destroy()	    

	dlg.Destroy()
	

#### --- Добавление коментария к записи дополнительного платежа ---	
    def MakeInfo3(self,event):
	item=self.ctrl3.currentItem
	kod=self.ctrl3.ps_rec_id[item]
#### --- Предыдущее значение примечания ---
	db=DBTools()
	messold = GetCommentPayOther(db,kod)
	db.Destroy()	    

	dlg=wx.TextEntryDialog(self,'Введите текст примечания','Примечание')
	dlg.SetValue(messold)
	if dlg.ShowModal()==wx.ID_OK:
	    mess=dlg.GetValue()
	    db=DBTools()
	    if AddCommentOther(db,kod,mess)[0] == 'OK':
		self.ctrl3.Populate(db,self.re[0])
	    db.Destroy()	    

	dlg.Destroy()


#### --- Удаление записи дополнительного платежа ---	
    def Delete3(self,event):
	item=self.ctrl3.currentItem
	kod=self.ctrl3.ps_rec_id[item]
	dlg=wx.MessageDialog(self,'Удалить запись?','Удаление')
	if dlg.ShowModal()==wx.ID_OK:
	    db=DBTools()
	    if DelOther(db,kod)[0] == 'OK':
		self.ctrl3.Populate(db,self.re[0])
	    db.Destroy()	    
	dlg.Destroy()



#### --- Новый платеж абонента ---
    def NewMoneyInto(self,event):
	# -- Передача кода абонента в форму диалога через запись в файл ---
	RWCfg.WriteValue('IDAbonent', self.re[0])


	dlg=NewPay.NewPayInto(self,-1,"Новый платеж", size=(350,200), style=wx.DEFAULT_DIALOG_STYLE)
	dlg.Centre()
	if dlg.ShowModal()==wx.ID_OK:
	    ser=dlg.ch
	    sum=dlg.text0.GetValue()
	    db=DBTools()
	    if AddMoneyInto(db,self.re[0], ser, sum)=='OK':
		self.ReFreshBalans(db)
		self.ctrl1.Populate(db,self.re[0])
		self.ctrl5.Populate(db,self.re[0])

			    
	    else:
		dlg2=wx.MessageDialog(self,'Ошибка ввода данных','Ошибка', wx.OK)
		dlg2.ShowModal()
		dlg2.Destroy()
	    	
	    db.Destroy()

	dlg.Destroy()	
	
	
#### --- Новое удержание абонента (ввод оператором) ---
    def NewMoneyOut(self,event):
	# -- Передача кода абонента в форму диалога через запись в файл ---
	RWCfg.WriteValue('IDAbonent', self.re[0])


	dlg=NewPay.NewPayOut(self,-1,"Новое удержание", size=(350,200), style=wx.DEFAULT_DIALOG_STYLE)
	dlg.Centre()
	if dlg.ShowModal()==wx.ID_OK:
	    ser=dlg.ch
	    sum=dlg.text0.GetValue()
	    db=DBTools()
	    if AddMoneyOut(db,self.re[0], ser, sum)=='OK':
		self.ReFreshBalans(db)
		self.ctrl2.Populate(db,self.re[0])
		self.ctrl5.Populate(db,self.re[0])

			    
	    else:
		dlg2=wx.MessageDialog(self,'Ошибка ввода данных','Ошибка', wx.OK)
		dlg2.ShowModal()
		dlg2.Destroy()

	    db.Destroy()

	dlg.Destroy()
	


#### --- Новый дополнительный платеж ---
    def NewMoneyOther(self,event):
	dlg=NewPay.NewPayOther(self,-1,"Новый платеж", size=(350,200), style=wx.DEFAULT_DIALOG_STYLE)
	dlg.Centre()
	if dlg.ShowModal()==wx.ID_OK:
	    db = DBTools()
	    if EnterMoneyOther(db,self.re[0],dlg.field.GetValue(),dlg.sc.GetValue())[0] == 'OK':
		self.ctrl3.Populate(db,self.re[0])
	    else:
		dlg2=wx.MessageDialog(self,'Ошибка ввода данных','Ошибка', wx.OK)
		dlg2.ShowModal()
		dlg2.Destroy()
	    db.Destroy()
	dlg.Destroy()



#### --- Перенос остатка с лицевого счета ---
    def MoveOstatok(self,event):
	db = DBTools()
	dlg = wx.SingleChoiceDialog(self, 'Выбор лицевого счета', 'Перенос остатка', GetAbonentService(db,self.re[0]))
	if dlg.ShowModal() == wx.ID_OK and Check.ReCheckPass(self) == 'OK':
	    item=self.ctrl5.currentItem
	    kod=self.ctrl5.ps_rec_id[item]
	    if (MoveOstatok(db,kod, dlg.GetStringSelection()))[0] == 'OK':
		self.ctrl5.Populate(db,self.re[0])
		self.ctrl4.Populate(db,self.re[0])
	dlg.Destroy() 
	db.Destroy()
	


#### --- Ввод новой заметки ---   
    def EnterMessage(self,event):
	dlg = wx.TextEntryDialog(self, 'Ввод новой заметки', 'Заметка', '', style=wx.OK|wx.CANCEL)
	if dlg.ShowModal() == wx.ID_OK:
	    db = DBTools()
	    if (NewMess(db,self.re[0],dlg.GetValue()))[0] == 'OK':
		self.ctrl4.Populate(db,self.re[0])
	    db.Destroy()
	dlg.Destroy()


#### --- Удаление заметки ---   
    def DeleteMessage(self,event):
	item=self.ctrl4.currentItem
	kod=self.ctrl4.ps_rec_id[item]
	dlg=wx.MessageDialog(self,'Удалить заметку?','Удаление')
	db = DBTools()
	if dlg.ShowModal() == wx.ID_OK and (DelMess(db,kod))[0] == 'OK':
	    self.ctrl4.Populate(db,self.re[0])
	db.Destroy()
	dlg.Destroy()




#### --- Добавление MAC адреса ---
    def	AddMAC(self,event):
	dlg=Net.AddMAC(self,-1,"Новый MAC", size=(350,200), style=wx.DEFAULT_DIALOG_STYLE)
	dlg.Centre()
	if dlg.ShowModal()==wx.ID_OK:
	    db = DBTools()
	    if dlg.field_0.GetValue()=='INTERNET':
		t = 1
	    elif dlg.field_0.GetValue()=='IPTV':
		t = 2
	    result = AddMac(db,self.re[0],t,dlg.field_1.GetValue())
	    if result == 'OK':
		self.ctrl6.Populate(db,self.re[0])
		self.ctrl6.SetItemState(0,wx.LIST_STATE_SELECTED,wx.LIST_STATE_SELECTED)
	    db.Destroy()
	dlg.Destroy()




#### --- Удаление MAC адреса ---
    def	DelMAC(self,event):
	kod=self.ctrl6.kod_record[self.ctrl6.currentItem]
	dlg=wx.MessageDialog(self,'Удалить MAC?','Удаление')
	if dlg.ShowModal()==wx.ID_OK:
	    db = DBTools()
	    result = DelMac(db,kod)
	    if result == 'OK':
		self.ctrl6.Populate(db,self.re[0])
		self.ctrl6.SetItemState(0,wx.LIST_STATE_SELECTED,wx.LIST_STATE_SELECTED)
	    db.Destroy()
	dlg.Destroy()
		