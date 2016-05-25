#coding:utf-8
import  wx
import	wx.lib.masked as masked
import	DBTools
import	cp1251
import	ReadSpr
from	abonent.RunSQL	import	GetAbonentData2


class NewTarif(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, 
            style=wx.DEFAULT_DIALOG_STYLE
            ):


        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)

        sizer = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, -1, "Стоимость трафика")
        sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)


        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)


        box = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self, -1, "Название тарифа")
        box.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.text0 = masked.TextCtrl(self, -1, "", name = "", mask="C{30}", formatcodes='F_')
        box.Add(self.text0, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
#	self.text0.SetValue(RWCfg.ReadValue('ServerDb'))
        sizer.Add(box, 0, wx.ALIGN_CENTER_VERTICAL, 5)


        box = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self, -1, "Цена за 1 МБайт")
        box.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.text1 = masked.TextCtrl(self, -1, "", name = "", mask="####.##", formatcodes='F-_', excludeChars="")
        box.Add(self.text1, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
#	self.text1.SetValue(RWCfg.ReadValue('NameDb'))
        sizer.Add(box, 0, wx.ALIGN_CENTER_VERTICAL, 5)



        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

        
        box = wx.BoxSizer(wx.HORIZONTAL)

        btn = wx.Button(self, wx.ID_OK)
        btn.SetDefault()
        box.Add(btn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)


        btn2 = wx.Button(self, wx.ID_CANCEL)
        box.Add(btn2, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        sizer.Add(box, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)







class EditTarif(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, 
            style=wx.DEFAULT_DIALOG_STYLE, name_tarif=''
            ):

#### --- Предварительная подготовка данных по выбранному тарифу ---
	db = DBTools.DBTools()
	rez = db.GetDataTarif(name_tarif)
	db.Destroy()
#### --- Идентификатор строки тарифа ---
	self.rec=rez[0]

        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)

        sizer = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, -1, "Стоимость трафика")
        sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)


        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)


        box = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self, -1, "Название тарифа")
        box.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.text0 = wx.TextCtrl(self,-1,"",size=(300,-1))
        box.Add(self.text0, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
	self.text0.SetValue(cp1251.win2utf(rez[1]))
        sizer.Add(box, 0, wx.ALIGN_CENTER_VERTICAL, 5)


        box = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self, -1, "Цена за 1 МБайт")
        box.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.text1 = wx.TextCtrl(self,-1,"", size=(80,-1))
        box.Add(self.text1, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
	self.text1.SetValue(rez[2])
        sizer.Add(box, 0, wx.ALIGN_CENTER_VERTICAL, 5)



        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

        
        box = wx.BoxSizer(wx.HORIZONTAL)

        btn = wx.Button(self, wx.ID_OK)
        btn.SetDefault()
        box.Add(btn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)


        btn2 = wx.Button(self, wx.ID_CANCEL)
        box.Add(btn2, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        sizer.Add(box, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)


	    

#### --- Добавление нового тарифа ---
def AddTarif(name,cost):
    db = DBTools.DBTools()
    rez = db.AddIntTarif(name,str(cost))
    db.Destroy()
    return rez



#### --- Изменение тарифа ---
def UpdateTarif(rec,name,cost):
    db = DBTools.DBTools()
    rez = db.UpdateIntTarif(rec,name,str(cost))
    db.Destroy()
    return rez




class LoginList(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, 
            style=wx.DEFAULT_DIALOG_STYLE
            ):


        pre = wx.PreDialog()
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)
	
	tID = wx.NewId()

        sizer = wx.BoxSizer(wx.VERTICAL)
        box = wx.BoxSizer(wx.HORIZONTAL)
	self.ctrl1 = ReadSpr.IntListLogin(pre, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl1.Populate()
        box.Add(self.ctrl1, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)
        btn = wx.Button(self, wx.ID_OK)        
        btn.SetDefault()
        box.Add(btn, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL|wx.TOP, 5)

        btn2 = wx.Button(self, wx.ID_CANCEL)
        box.Add(btn2, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL|wx.TOP, 5)
        sizer.Add(box, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)


	self.ctrl1.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem, self.ctrl1)



#### --- Присвоение значения по выбранной строке ---
    def ReadItem(self,event):
	self.ctrl1.currentItem = event.m_itemIndex
	



#### --- Форма с данными учетной записи ---
class Account(wx.Frame):
    def __init__(self,parent,ID,title, pos=wx.DefaultPosition,
            size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, rec=''
	):


#### --- Предварительная подготовка данных ---

#### --- Начальные значения выбора тарифа ---
	self.ch_t="zero"


#### --- Получение данных учетной записи абонента ---
	self.re = GetAbonentData2(rec)
	self.re2 = ReadSpr.GetAccount(rec)
	self.rec = rec

#### --- Получение значений лицевого счета услуги INTERNET и данных трафика в текущем месяце ---
	db = DBTools.DBTools()
	self.sumls = db.GetIntLs(rec)
	self.sumtraf = db.GetMonthTraf(rec)
	db.Destroy()

#### --- Справочник тарифных планов ---
#	self.choice_tp = ReadSpr.ReadTp(self.re[7])



        wx.Frame.__init__(self,parent,ID, title, pos, size, style)
        panel = wx.Panel(self, -1)
	
	mainsizer = wx.BoxSizer(wx.VERTICAL)

	tID = wx.NewId()


#### --- Заголовок ---
	sizer = wx.BoxSizer(wx.HORIZONTAL)
	topLbl = wx.StaticText(panel, -1, "Учетная запись")
	topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
	sizer.Add(topLbl, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_LEFT|wx.ALL, 5)
	mainsizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)

#### --- Первая строка интерфейса ---
	sizer = wx.BoxSizer(wx.HORIZONTAL)
	label = wx.StaticText(panel, -1, "Улица")
        self.field1 = wx.TextCtrl(panel, -1, "", size=(200,-1), style=wx.TE_READONLY)
	self.field1.SetValue(cp1251.win2utf(self.re[1]))
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field1, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

	label = wx.StaticText(panel, -1, "Дом")
        self.field2 = wx.TextCtrl(panel, -1, "", style=wx.TE_READONLY)
	self.field2.SetValue(cp1251.win2utf(self.re[2]))
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field2, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

	label = wx.StaticText(panel, -1, "Квартира")
        self.field3 = wx.TextCtrl(panel, -1, "", style=wx.TE_READONLY)
	self.field3.SetValue(cp1251.win2utf(self.re[3]))
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field3, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_LEFT|wx.ALL, 5)


#### --- Вторая строка интерфейса ---
	sizer = wx.BoxSizer(wx.HORIZONTAL)
	label = wx.StaticText(panel, -1, "Телефон")
        self.field4 = wx.TextCtrl(panel, -1, "", size=(200,-1), style=wx.TE_READONLY)
	self.field4.SetValue(cp1251.win2utf(self.re[5]))
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field4, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

	label = wx.StaticText(panel, -1, "Контакт", pos=(240,50))
        self.field5 = wx.TextCtrl(panel, -1, "",pos=(290,50),size=(290, -1),style=wx.TE_READONLY)
	self.field5.SetValue(cp1251.win2utf(self.re[6]))
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field5, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_LEFT|wx.ALL, 5)



#### --- Третья строка интерфейса ---
	sizer = wx.BoxSizer(wx.HORIZONTAL)
	label = wx.StaticText(panel, -1, "Лицевой счет (руб.)", pos=(10,90))
        self.field6 = wx.TextCtrl(panel, -1, "",pos=(60,90),size=(80, -1), style=wx.TE_READONLY)
	self.field6.SetValue(str(self.sumls))
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field6, 0, wx.ALIGN_CENTRE|wx.ALL, 5)


	label = wx.StaticText(panel, -1, "Трафик в текущем месяце (МБайт)", pos=(10,90))
        self.field7 = wx.TextCtrl(panel, -1, "",pos=(60,90),size=(80, -1), style=wx.TE_READONLY)
	self.field7.SetValue(str(self.sumtraf))
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field7, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_LEFT|wx.ALL, 5)




#### --- Четвертая строка интерфейса ---
	sizer = wx.BoxSizer(wx.HORIZONTAL)
	label = wx.StaticText(panel, -1, "Логин", pos=(10,90))
        self.field8 = wx.TextCtrl(panel, -1, "",pos=(60,90),size=(200, -1), style=wx.TE_READONLY)
	self.field8.SetValue(self.re2[6])
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field8, 0, wx.ALIGN_CENTRE|wx.ALL, 5)


	label = wx.StaticText(panel, -1, "Пароль", pos=(10,90))
        self.field9 = wx.TextCtrl(panel, -1, "",pos=(60,90),size=(200, -1), style=wx.TE_READONLY|wx.TE_PASSWORD)
	self.field9.SetValue(self.re2[6])
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field9, 0, wx.ALIGN_CENTRE|wx.ALL, 5)


        self.button2 = wx.Button(panel, 1003, "Изменить пароль", style=wx.BU_EXACTFIT|wx.NO_BORDER)
	sizer.Add(self.button2, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_LEFT|wx.ALL, 5)



#### --- Пятая строка интерфейса ---
	sizer = wx.BoxSizer(wx.HORIZONTAL)
	label = wx.StaticText(panel, -1, "Тариф", pos=(10,90))
        self.field10 = wx.TextCtrl(panel, -1, "",pos=(60,90),size=(300, -1), style=wx.TE_READONLY)
	self.field10.SetValue(cp1251.win2utf(self.re2[5]))
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field10, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.button10 = wx.Button(panel, 1005, "Изменить тариф", style=wx.BU_EXACTFIT|wx.NO_BORDER)
	sizer.Add(self.button10, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_LEFT|wx.ALL, 5)




#### --- Шестая строка интерфейса ---
	sizer = wx.BoxSizer(wx.HORIZONTAL)
	label = wx.StaticText(panel, -1, "IP адрес", pos=(10,90))
        self.field11 = wx.TextCtrl(panel, -1, "",pos=(60,90),size=(150, -1), style=wx.TE_READONLY)
	self.field11.SetValue(cp1251.win2utf(self.re2[7]))
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field11, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

	label = wx.StaticText(panel, -1, "Дата и время", pos=(10,90))
        self.field12 = wx.TextCtrl(panel, -1, "",pos=(60,90),size=(150, -1), style=wx.TE_READONLY)
	self.field12.SetValue(cp1251.win2utf(str(self.re2[8])))
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field12, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_LEFT|wx.ALL, 5)



#### --- Таблица с данными сессий ----
	mainsizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
	self.ctrl1 = ReadSpr.IntListTrafik(panel, tID, size=(200,200), style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl1.Populate(rec)
        sizer.Add(self.ctrl1, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_CENTRE|wx.ALL|wx.GROW, 5)


	panel.SetSizer(mainsizer)
	mainsizer.Fit(self)
	


	self.button2.Bind(wx.EVT_BUTTON, self.NewPasswd, self.button2)
	self.button10.Bind(wx.EVT_BUTTON, self.ChTarif, self.button10)
	self.ctrl1.Bind(wx.EVT_LIST_ITEM_SELECTED,self.ReadItem1,self.ctrl1)
	self.ctrl1.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK,self.ShowMenu1,self.ctrl1)
	


#### --- Выбор строки ---
    def	ReadItem1(self,event):
	self.ctrl1.currentItem = event.m_itemIndex
	
	
#### --- Меню для выбранной строки ---
    def	ShowMenu1(self,event):
	self.popupID1 = wx.NewId()
	self.menu1 = wx.Menu()
	self.menu1.Append(self.popupID1, "Удалить")
	self.menu1.Bind(wx.EVT_MENU, self.Delete1, id=self.popupID1)
        self.PopupMenu(self.menu1)
	self.menu1.Destroy()
	

#### --- Удаление выбранного удержания конкретной сессии ---
    def	Delete1(self,event):
	item = self.ctrl1.currentItem
	kod = self.ctrl1.kod_record[item]
	dlg = wx.MessageDialog(self,'Удалить запись?', 'Удаление')
	if dlg.ShowModal()==wx.ID_OK:
	    db = DBTools.DBTools()
	    if db.DelTrafSes(self.rec,kod)=='OK':
		### --- Перерисовка данных по сессиям, балансу, трафику за месяц ---
		self.sumls = db.GetIntLs(self.rec)
		self.sumtraf = db.GetMonthTraf(self.rec)
		self.ctrl1.Populate(self.rec)
		self.field6.SetValue(str(self.sumls))
		self.field7.SetValue(str(self.sumtraf))
	    db.Destroy()
	    
	dlg.Destroy()


#### --- Изменение пароля учетной записи ---
    def NewPasswd(self,evt):
	dlg = wx.MessageDialog(self,'Изменить пароль?','INTERNET')
	if dlg.ShowModal()==wx.ID_OK:
	    db = DBTools.DBTools()
	    if db.UpdatePasswd(self.rec)=='OK':
		dlg2 = wx.MessageDialog(self,'Пароль доступа INTERNET изменен,\nзначение пароля можно получить через\nпечатную форму "Карточка абонента".','Сообщение', style = wx.OK)
		dlg2.ShowModal()
		dlg2.Destroy()
	    db.Destroy()
	dlg.Destroy()
	    

#### --- Изменение тарифа Internet ---	    
    def ChTarif(self,evt):
	dlg = wx.SingleChoiceDialog(self, 'Internet тариф', 'Internet', ReadSpr.ReadIntTarif())
	if dlg.ShowModal() == wx.ID_OK:
	    tarif = dlg.GetStringSelection()
	    db = DBTools.DBTools()
	    if db.UpdateTarifAccount(self.rec,tarif) == 'OK':
		self.field10.SetValue(tarif)
	    db.Destroy()
	dlg.Destroy()	
	