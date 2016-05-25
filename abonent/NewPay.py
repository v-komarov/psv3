#coding:utf-8

import  wx
import	anydbm
import	RWCfg
import	ReadSpr
from	abonent.RunSQL	import	GetAbonentService
from	abonent.RunSQL	import	GetAbonentService2
from	DBTools	import	DBTools




#### --- Ввод нового платежа ----
class NewPayInto(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition,
            style=wx.DEFAULT_DIALOG_STYLE
            ):


        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)

        sizer = wx.BoxSizer(wx.VERTICAL)

        label = wx.StaticText(self, -1, "Укажите услугу и введите сумму платежа")
        sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)


#### --- Список сервисов для выбора платежа ---
	db = DBTools()
	self.ch = wx.Choice(self,-1,(160,10), choices=GetAbonentService2(db,RWCfg.ReadValue('IDAbonent')))
        box.Add(self.ch, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
	self.ch.Bind(wx.EVT_CHOICE, self.ChoiceServ, self.ch)
	self.ch="" # Начальное значение
	db.Destroy()
	
#### --- Сумма платежа ---
        self.text0 = wx.TextCtrl(self, -1, "", size=(80,-1))
        box.Add(self.text0, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
#	self.text0.SetValue('0.00')


        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)



        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

        self.btnsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.btn = wx.Button(self, wx.ID_OK)
        self.btn.SetDefault()
        self.btnsizer.Add(self.btn, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.btn2 = wx.Button(self, wx.ID_CANCEL)
        self.btnsizer.Add(self.btn2, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(self.btnsizer, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)


    def ChoiceServ(self,event):
	self.ch=event.GetString()
	
	
	
	



#### --- Новое удержание ---
class NewPayOut(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition,
            style=wx.DEFAULT_DIALOG_STYLE
            ):



        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)

        sizer = wx.BoxSizer(wx.VERTICAL)

        label = wx.StaticText(self, -1, "Укажите услугу и введите сумму удержания")
        sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)

	db=DBTools()

#### --- Список сервисов для выбора платежа ---
	self.ch = wx.Choice(self,-1,(160,10), choices=GetAbonentService2(db,RWCfg.ReadValue('IDAbonent')))
        box.Add(self.ch, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
	self.ch.Bind(wx.EVT_CHOICE, self.ChoiceServ, self.ch)
	self.ch="" # Первоначальное значение 

	db.Destroy()

#### --- Сумма платежа ---
        self.text0 = wx.TextCtrl(self, -1, "", size=(80,-1))
        box.Add(self.text0, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
#	self.text0.SetValue('0.00')


        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)



        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

        self.btnsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.btn = wx.Button(self, wx.ID_OK)	        
        self.btn.SetDefault()
        self.btnsizer.Add(self.btn, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.btn2 = wx.Button(self, wx.ID_CANCEL)
        self.btnsizer.Add(self.btn2, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(self.btnsizer, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)


    def ChoiceServ(self,event):
	self.ch=event.GetString()
	





#### --- Ввод начальных остатков ---
class Ostatok(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition,
            style=wx.DEFAULT_DIALOG_STYLE
            ):



        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)

        sizer = wx.BoxSizer(wx.VERTICAL)

        label = wx.StaticText(self, -1, "Укажите услугу и введите сумму остатка")
        sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)

	db = DBTools()

#### --- Список сервисов для выбора платежа ---
	self.ch = wx.Choice(self,-1,(160,10), choices=GetAbonentService2(db,RWCfg.ReadValue('IDAbonent')))
        box.Add(self.ch, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
	self.ch.Bind(wx.EVT_CHOICE, self.ChoiceServ, self.ch)
	self.ch="" # Начальное значение

	db.Destroy()
	
#### --- Сумма  ---
        self.text0 = wx.TextCtrl(self, -1, "", size=(80,-1))
        box.Add(self.text0, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
#	self.text0.SetValue('0.00')


        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)
        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

        self.btnsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.btn = wx.Button(self, wx.ID_OK)	        
        self.btn.SetDefault()
        self.btnsizer.Add(self.btn, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.btn2 = wx.Button(self, wx.ID_CANCEL)
        self.btnsizer.Add(self.btn2, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(self.btnsizer, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)


    def ChoiceServ(self,event):
	self.ch=event.GetString()
	





	
#### ---- Добавление новой записи дополнительного платежа ---
class NewPayOther(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition,
            style=wx.DEFAULT_DIALOG_STYLE
            ):



        pre = wx.PreDialog()
#        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)

        sizer = wx.BoxSizer(wx.VERTICAL)

        label = wx.StaticText(self, -1, "Введите назначение и сумму")
        sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

	box = wx.BoxSizer(wx.HORIZONTAL)
#### --- Сумма  ---
        self.sc = wx.SpinCtrl(self, -1, "", size=(100,-1))
        self.sc.SetRange(0,10000)
        self.sc.SetValue(0)
	self.field = wx.TextCtrl(pre, -1, size=(200,-1))
        box.Add(self.field, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(self.sc, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.ALIGN_CENTRE|wx.ALL, 5)


	sizer.Add(wx.StaticLine(pre), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)


        self.btnsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.btn = wx.Button(self, wx.ID_OK)
        self.btn.SetDefault()
        self.btnsizer.Add(self.btn, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.btn2 = wx.Button(self, wx.ID_CANCEL)
        self.btnsizer.Add(self.btn2, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(self.btnsizer, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)


	
		