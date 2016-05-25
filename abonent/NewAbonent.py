#coding:utf-8


""" Добавление нового абонента """


import  wx
import	ReadSpr
from	abonent.RunSQL	import	SaveNewAbonent
from	abonent.RunSQL	import	GetListUl
from	abonent.RunSQL	import	GetListTarifPlan
from	DBTools	import	DBTools
import	RWCfg
import	Abonent


class AbonentAdd(wx.Frame):
    def __init__(self,parent,ID,title, pos=wx.DefaultPosition,
            size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE
	):

        wx.Frame.__init__(self,parent,ID, title, pos, size, style)
	panel = wx.Panel(self, -1)

	mainsizer = wx.BoxSizer(wx.VERTICAL)

	sizer = wx.BoxSizer(wx.HORIZONTAL)
	topLbl = wx.StaticText(panel, -1, "Ввод нового абонента")
	topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
	sizer.Add(topLbl, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_LEFT|wx.ALL, 5)


	mainsizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)

	### --- Подключение к базе данных ---
	db = DBTools()


###--- Первая строка интерфейса ---
	sizer = wx.BoxSizer(wx.HORIZONTAL)
	label = wx.StaticText(panel, -1, "Улица", pos=(10,10))
        self.cb0 = wx.ComboBox(panel, -1, "", size=(200,-1), choices=GetListUl(db), style=wx.CB_DROPDOWN|wx.CB_READONLY)		
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.cb0, 0, wx.ALIGN_CENTRE|wx.ALL, 5)


	label = wx.StaticText(panel, -1, "Дом", pos=(240,10))
        self.field2 = wx.TextCtrl(panel, -1, "",pos=(270,10),size=(50, -1))
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field2, 0, wx.ALIGN_CENTRE|wx.ALL, 5)


	label = wx.StaticText(panel, -1, "Квартира", pos=(340,10))
        self.field3 = wx.TextCtrl(panel, -1, "",pos=(400,10),size=(50, -1))
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field3, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_LEFT|wx.ALL, 5)



###--- Вторая строка интерфейса ---
	sizer = wx.BoxSizer(wx.HORIZONTAL)
	label = wx.StaticText(panel, -1, "Телефон", pos=(10,50))
        self.field4 = wx.TextCtrl(panel, -1, "",pos=(60,50),size=(160, -1))
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field4, 0, wx.ALIGN_CENTRE|wx.ALL, 5)


	label = wx.StaticText(panel, -1, "Подъезд")
        self.field6 = wx.TextCtrl(panel, -1, "",size=(30, -1))
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field6, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_LEFT|wx.ALL, 5)



###--- Третья строка интерфейса ---
	sizer = wx.BoxSizer(wx.HORIZONTAL)
	label = wx.StaticText(panel, -1, "Контакт", pos=(240,50))
        self.field5 = wx.TextCtrl(panel, -1, "",pos=(290,50),size=(290, -1))
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.field5, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_LEFT|wx.ALL, 5)


###--- Четвертая строка интерфейса ---
	sizer = wx.BoxSizer(wx.HORIZONTAL)
	label = wx.StaticText(panel, -1, "Тарифный план", pos=(10,90))
        self.cb1 = wx.ComboBox(panel, -1, "", size=(300,-1), choices=GetListTarifPlan(db), style=wx.CB_DROPDOWN|wx.CB_READONLY)		
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.cb1, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_LEFT|wx.ALL, 5)
	mainsizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)


###--- Пятая строка интерфейса ---
	sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.button2 = wx.Button(panel, 1003, "Сохранить")
        self.button3 = wx.Button(panel, 1004, "Отмена")
	self.Bind(wx.EVT_BUTTON, self.OnCloseWindow, self.button3)
	sizer.Add(self.button2, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.button3, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_CENTRE|wx.ALL, 5)


	### --- Отключение от базы данных ---
	db.Destroy()


	panel.SetSizer(mainsizer)
	mainsizer.Fit(self)


        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.Bind(wx.EVT_BUTTON, self.SaveData, self.button2)
	


    def OnCloseWindow(self, event):
        self.Destroy()



#### --- Функция сохранения данных в базе данных ---
    def SaveData(self,event):
	
	ul=self.cb0.GetValue()
	dom=self.field2.GetValue()
	kv=self.field3.GetValue()
	tel=self.field4.GetValue()
	fio=self.field5.GetValue()
	tp=self.cb1.GetValue()
	p=self.field6.GetValue()
		
	save_ok = SaveNewAbonent(ul,dom,kv,tel,fio,tp,p)
	
	if save_ok[:2]!='OK':
	    dlg1=wx.MessageDialog(self,'Проверьте правильность данных!\nВозможно данные не полные\nлибо такой абонент уже есть в базе.','Ошибка сохранения',wx.OK)
	    dlg1.ShowModal()
	    dlg1.Destroy()        
	    
	else:
#	    self.Show(False)
	    RWCfg.WriteValue('FoundRecord', save_ok[2:])
	    ab = Abonent.Abonent(self,-1,"Абонент", pos=wx.DefaultPosition,
	    size=(600,490), style=wx.MINIMIZE_BOX|wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.FRAME_FLOAT_ON_PARENT)
	    ab.Centre()
	    ab.Show(True)

	


