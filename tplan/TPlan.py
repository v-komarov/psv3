#coding:utf-8

""" Работа с тарифными планами: ввод нового, наполнение услугами, переименование """

import  wx
import	DBTools
import	RWCfg
import	ReadSpr
import	Check
from	tplan.RunSQL	import	GetListTarifPlan
from	tplan.RunSQL	import	ReNameTarifPlan
from	tplan.RunSQL	import	NewTarifPlan
from	tplan.RunSQL	import	DelSerFromTP
from	tplan.RunSQL	import	AddService
from	tplan.RunSQL	import	SetCostService
from	tplan.ServiceList	import	ListServ
from	tplan.ServiceList	import	SetCostService as SetCost




#### -- Добавление нового тарифного плана через хранимую функцию ps_addtarifplan() --- ####
def AddTarifPlan(self):
		
    dlg = wx.TextEntryDialog(self, 'Введите наименование тарифного плана','Новый тарифный план','', style=wx.OK|wx.CANCEL)

    if dlg.ShowModal() == wx.ID_OK:
	if NewTarifPlan(dlg.GetValue()) == 'OK':
	    dlg2 = wx.MessageDialog(self, 'Тарифный план добавлен', 'Сообщение', wx.OK|wx.ICON_INFORMATION)
	    dlg2.ShowModal()
	    dlg2.Destroy()
	else:
	    dlg2 = wx.MessageDialog(self, 'Такой тарифный видимо уже существует.', 'Сообщение', wx.OK|wx.ICON_INFORMATION)
	    dlg2.ShowModal()
	    dlg2.Destroy()




#### --- Изменение наименования тарифного плана --- ####
def EditTarifPlanName(self):
    dlg = wx.SingleChoiceDialog(self, 'Выбор тарифного плана', 'Тарифный план', GetListTarifPlan())

    if dlg.ShowModal() == wx.ID_OK:
	NameOld = dlg.GetStringSelection()
	dlg2 = wx.TextEntryDialog(self, 'Введите новое наименование тарифного плана','Переименование тарифного плана', NameOld, style=wx.OK|wx.CANCEL)

	if dlg2.ShowModal() == wx.ID_OK:
	    NameNew = dlg2.GetValue()
	    
	    if ReNameTarifPlan(NameOld,NameNew) != 'OK':
		dlg3 = wx.MessageDialog(self, 'Такой тарифный видимо уже существует.', 'Сообщение', wx.OK|wx.ICON_INFORMATION)
		dlg3.ShowModal()
		dlg3.Destroy()

	dlg2.Destroy()

    dlg.Destroy()






#### --- Изменение услуг тарифного плана --- ####
class ServiceTarifPlan(wx.Frame):
    def __init__(self,parent,ID,title, pos=wx.DefaultPosition,
            size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE
	):

        wx.Frame.__init__(self,parent,ID, title, pos, size, style)
        panel = wx.Panel(self, -1)
	tID = wx.NewId()



	mainsizer = wx.BoxSizer(wx.VERTICAL)

#### --- Заголовок ----
	sizer = wx.BoxSizer(wx.HORIZONTAL)
	topLbl = wx.StaticText(panel, -1, "Состав тарифного плана")
	topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
	sizer.Add(topLbl, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_LEFT|wx.ALL, 5)
	mainsizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
	
	

#### --- Выбор тарифного плана ---
	sizer = wx.BoxSizer(wx.HORIZONTAL)
	label = wx.StaticText(panel, -1, "Тарифный план")
        self.ch = wx.ComboBox(panel, -1, "" , size=(200,-1), choices=GetListTarifPlan())		
	sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	sizer.Add(self.ch, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_LEFT|wx.ALL, 5)

#### --- Отображения услуг по выбранному тарифному плану ---
	sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.ctrl1 = ListServ(panel, tID,
                                 style=wx.LC_REPORT
                                 | wx.LC_SORT_ASCENDING
                                 )
	sizer.Add(self.ctrl1, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_LEFT|wx.ALL, 5)


#### --- Кнопка добавления услуги к тарифному плану ---
	sizer = wx.BoxSizer(wx.HORIZONTAL)
	self.button = wx.Button(panel, 1004, "Дабавить новую услугу")
	sizer.Add(self.button, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

     
	panel.SetSizer(mainsizer)
	mainsizer.Fit(self)


        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
	self.ch.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.ch)
	self.button.Bind(wx.EVT_BUTTON, self.AddService, self.button)
	self.ctrl1.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.ShowMenu1, self.ctrl1)	
	self.ctrl1.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem1, self.ctrl1)




    def OnCloseWindow(self, event):
        self.Destroy()


#### --- Регистрация выбора тарифного плана ---
    def EvtComboBox(self,event):
	self.ctrl1.Populate(event.GetString())
	self.ctrl1.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)


#### --- Добавление услуги к тарифному плану ---
    def AddService(self,event):
	dlg = wx.SingleChoiceDialog(self, 'Выбор услуги', 'Услуги', ReadSpr.ReadAllServices())
	if dlg.ShowModal() == wx.ID_OK and len(self.ch.GetValue())!=0:
	    NameService = dlg.GetStringSelection()
	    if AddService(NameService,self.ch.GetValue()) != 'OK':
		dlg3 = wx.MessageDialog(self, 'Такая услуга видимо уже существует.', 'Сообщение', wx.OK|wx.ICON_INFORMATION)
		dlg3.ShowModal()
		dlg3.Destroy()

	    else:
		self.ctrl1.Populate(self.ch.GetValue())
	    
	    
	dlg.Destroy()
	


#### --- Присвоение значения по выбранной строке платежа ---
    def ReadItem1(self,event):
	self.ctrl1.currentItem = event.m_itemIndex



#### --- Меню для списка платежей ---
    def	ShowMenu1(self,event):
	self.popupID1=wx.NewId()
	self.popupID2=wx.NewId()
	self.menu1=wx.Menu()
	self.menu1.Append(self.popupID1,"Установить значение стоимости") 
	self.menu1.Append(self.popupID2,"Удалить услугу из тарифного плана")
	self.menu1.Bind(wx.EVT_MENU, self.SetMoney1, id=self.popupID1)
	self.menu1.Bind(wx.EVT_MENU, self.Delete1, id=self.popupID2)
	self.PopupMenu(self.menu1)
	self.menu1.Destroy() 



#### --- Установка стоимости услуги ----
    def SetMoney1(self,event):
	item=self.ctrl1.currentItem
	kod = self.ctrl1.ps_rec_id[item]
 	dlg=SetCost(self,-1,"Установка стоимости", size=(350,200), style=wx.DEFAULT_DIALOG_STYLE)
	dlg.Centre()
	if dlg.ShowModal()==wx.ID_OK and Check.ReCheckPass(self)=='OK':
            cost = dlg.sc.GetValue()
	    SetCostService(kod,cost)
	    self.ctrl1.Populate(self.ch.GetValue())
	dlg.Destroy()	



#### --- Удалить услугу из тарифного плана ----
    def Delete1(self,event):
	item=self.ctrl1.currentItem
	kod = self.ctrl1.ps_rec_id[item]
	dlg=wx.MessageDialog(self,'Удалить запись?','Удаление')
	if dlg.ShowModal()==wx.ID_OK and Check.ReCheckPass(self)=='OK':
	    DelSerFromTP(kod)
	    self.ctrl1.Populate(self.ch.GetValue())
	dlg.Destroy()
