#coding:utf-8

import  wx
import	wx.calendar
import	sys
import	string	
from	task.Task	import	EditTask
from	task.PrintTask	import	RemList
from	task.PrintTask	import	MonList
from	task.RunSQL	import	NewTask
from	task.RunSQL	import	NewTask2
from	task.RunSQL	import	GetListTask
from	task.RunSQL	import	GetListTask2
from	task.RunSQL	import	DelTask
from	tools.Messages	import	SaveDone
from	tools.Messages	import	ErrorData
from	tools.Messages	import	NotAccess






#### --- Форма списка заявок ---
class MainListTask(wx.Frame):
    def __init__(self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, style=wx.DEFAULT_FRAME_STYLE):
#    def __init__(
#            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, 
#            style=wx.DEFAULT_DIALOG_STYLE
#            ):

	self.date0 = wx.DateTime_Now()

        pre = wx.PreDialog()
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)

	tID = wx.NewId()


#### --- Заголовок ---
        sizer = wx.BoxSizer(wx.VERTICAL)

	boxlist = wx.BoxSizer(wx.VERTICAL)
	boxcal = wx.BoxSizer(wx.HORIZONTAL)

        self.label = wx.StaticText(self, -1, "Список заявок")
        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
	self.cal = wx.calendar.CalendarCtrl(pre,-1,wx.DateTime_Now(), size=(-1,-1), pos=(0,0), style=wx.calendar.CAL_SHOW_HOLIDAYS|wx.calendar.CAL_MONDAY_FIRST|wx.calendar.CAL_SEQUENTIAL_MONTH_SELECTION)
	self.ctrl0 = List(pre, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.label.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))

        sizer.Add(self.label, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER, 5)
	boxcal.Add(self.cal, 1, wx.ALIGN_LEFT|wx.ALL, 5)	
	boxcal.Add(boxlist, 0, wx.ALIGN_RIGHT, 5)
	boxlist.Add(self.ctrl0, 1, wx.ALIGN_CENTER|wx.ALL, 5)	
	sizer.Add(boxcal, 0, wx.ALIGN_LEFT, 5)

	self.ctrl0.Populate(str(self.date0.GetYear())+'-' + str(self.date0.GetMonth()+1) +'-'+ str(self.date0.GetDay()))
	self.ctrl0.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER, 5)


#### --- Кнопки ---
        btn = wx.Button(self, wx.ID_ADD)
        btn1 = wx.Button(self, wx.ID_DELETE)
        btn2 = wx.Button(self, wx.ID_REFRESH)
        btn3 = wx.Button(self, wx.ID_CLOSE)
        btn4 = wx.Button(self, -1, "Ремонт")
        btn5 = wx.Button(self, -1, "Монтаж")

        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(btn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(btn1, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(btn2, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(btn3, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(btn4, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(btn5, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)
	    
	self.Bind(wx.EVT_BUTTON, self.Add, btn)
	self.Bind(wx.EVT_BUTTON, self.Del, btn1)
	self.Bind(wx.EVT_BUTTON, self.ReFresh, btn2)
	self.Bind(wx.EVT_BUTTON, self.Cancel, btn3)
	self.Bind(wx.EVT_BUTTON, self.RemTask, btn4)
	self.Bind(wx.EVT_BUTTON, self.MonTask, btn5)
	self.ctrl0.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem, self.ctrl0)
	self.ctrl0.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.Edit, self.ctrl0)
	self.Bind(wx.calendar.EVT_CALENDAR, self.OnCalSelected, id=self.cal.GetId())



    def	OnCalSelected(self,evt):
	self.date0 = self.cal.GetDate()
	self.ctrl0.Populate(str(self.date0.GetYear())+'-' + str(self.date0.GetMonth()+1) +'-'+ str(self.date0.GetDay()))
	self.ctrl0.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)


#### --- Присвоение значение по выбранной строке ----
    def ReadItem(self,event):
	self.ctrl0.currentItem = event.m_itemIndex
	
#### --- Кнопка Cancel ----
    def Cancel(self,event):
	self.Destroy()


#### --- Кнопка добавить ---
    def	Add(self,event):
	dlg = wx.TextEntryDialog(self,'Введите адрес', 'Ввод адреса','')	
	date = str(self.date0.GetYear())+'-' + str(self.date0.GetMonth()+1) +'-'+ str(self.date0.GetDay()) + " 09:00"	
	if dlg.ShowModal() == wx.ID_OK:
	    qaddress = string.split(dlg.GetValue())
	    if len(qaddress)==3:
		ul = qaddress[0]
		dom = qaddress[1]
		kv = qaddress[2]
		result = NewTask(ul,dom,kv,date)
		if result=='ERRORDATE':
		    ErrorData(self)
		elif result=='NOTACCESS':
		    NotAccess(self)
		elif len(result)==24:
		    self.ctrl0.Populate(str(self.date0.GetYear())+'-' + str(self.date0.GetMonth()+1) +'-'+ str(self.date0.GetDay()))
		    self.ctrl0.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
		    dlg2 = EditTask(self,-1,"Заявка", size=(450,300), style = wx.DEFAULT_DIALOG_STYLE, kod_rec=result)
		    if dlg2.ShowModal() == wx.ID_OK:
			pass
		    dlg2.Destroy()
		    self.ctrl0.Populate(str(self.date0.GetYear())+'-' + str(self.date0.GetMonth()+1) +'-'+ str(self.date0.GetDay()))
		    self.ctrl0.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
		
	    elif len(qaddress)==2:
		ul = qaddress[0]
		dom = qaddress[1]
		result = NewTask2(ul,dom,date)
		if result=='ERRORDATE':
		    ErrorData(self)
		elif result=='NOTACCESS':
		    NotAccess(self)
		elif len(result)==24:
		    self.ctrl0.Populate(str(self.date0.GetYear())+'-' + str(self.date0.GetMonth()+1) +'-'+ str(self.date0.GetDay()))
		    self.ctrl0.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
		    dlg2 = EditTask(self,-1,"Заявка", size=(450,300), style = wx.DEFAULT_DIALOG_STYLE, kod_rec=result)
		    if dlg2.ShowModal() == wx.ID_OK:
			pass
		    dlg2.Destroy()
		    self.ctrl0.Populate(str(self.date0.GetYear())+'-' + str(self.date0.GetMonth()+1) +'-'+ str(self.date0.GetDay()))
		    self.ctrl0.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
		
	dlg.Destroy()



#### --- Обновления данных по заявкам ---
    def	ReFresh(self,event):
	date = str(self.date0.GetYear())+'-' + str(self.date0.GetMonth()+1) +'-'+ str(self.date0.GetDay()) + " 09:00"	
	self.ctrl0.Populate(str(self.date0.GetYear())+'-' + str(self.date0.GetMonth()+1) +'-'+ str(self.date0.GetDay()))
	self.ctrl0.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
    



#### --- Изменение (редактирование) ---
    def	Edit(self,event):
	kod_row = self.ctrl0.kod_record[self.ctrl0.currentItem]
	select_id = self.ctrl0.currentItem
	dlg = EditTask(self,-1,"Заявка", size=(450,300), style = wx.DEFAULT_DIALOG_STYLE, kod_rec=kod_row)
	if dlg.ShowModal() == wx.ID_OK:
	    result = EditWorker(kod_row,dlg.field_0.GetValue(),dlg.field_1.GetValue(),dlg.field_2.GetValue())
	    if result == 'OK':
		pass
	    elif result == 'NOTACCESS':
		NotAccess(self)
	    elif result == 'ERRORDATA':
		ErrorData(self)
	dlg.Destroy()
	self.ctrl0.Populate(str(self.date0.GetYear())+'-' + str(self.date0.GetMonth()+1) +'-'+ str(self.date0.GetDay()))
	self.ctrl0.SetItemState(select_id, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)




#### --- Кнопка удалить ---
    def	Del(self,event):
	kod_row = self.ctrl0.kod_record[self.ctrl0.currentItem]
	if len(kod_row) == 24:
	    dlg = wx.MessageDialog(self,"Удалить заявку?","Удаление",style=wx.YES_NO)
	    if dlg.ShowModal() == wx.ID_YES:
		result = DelTask(kod_row)
		if result == 'OK':
		    self.ctrl0.Populate(str(self.date0.GetYear())+'-' + str(self.date0.GetMonth()+1) +'-'+ str(self.date0.GetDay()))
		    self.ctrl0.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
		elif result == 'NOTACCESS':
		    NotAccess(self)
		elif result == 'ERRORDATA':
		    ErrorData(self)
	    dlg.Destroy()




#### --- Печать заявок на ремонт ---
    def	RemTask(self,event):
	RemList(str(self.date0.GetYear())+'-' + str(self.date0.GetMonth()+1) +'-'+ str(self.date0.GetDay()))



#### --- Печать заявок на монтаж ---
    def	MonTask(self,event):
	MonList(str(self.date0.GetYear())+'-' + str(self.date0.GetMonth()+1) +'-'+ str(self.date0.GetDay()))




#### --- Элемент со списком  ----
class List(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0), size=(800,400), style=0):
	wx.ListCtrl.__init__(self, parent, ID, pos, size, style)

	self.InsertColumn(0,"Дата")
	self.InsertColumn(1,"Время")
	self.InsertColumn(2,"Статус")
	self.InsertColumn(3,"Тип")
	self.InsertColumn(4,"Заявка")
	self.InsertColumn(5,"Улица")
	self.InsertColumn(6,"Дом")
	self.InsertColumn(7,"Квартира")
	self.InsertColumn(8,"Подъезд")

	self.SetColumnWidth(0, 100)
	self.SetColumnWidth(1, 80)
	self.SetColumnWidth(2, 85)
	self.SetColumnWidth(3, 85)
	self.SetColumnWidth(4, 200)
	self.SetColumnWidth(5, 100)
	self.SetColumnWidth(6, 50)
	self.SetColumnWidth(7, 50)
	self.SetColumnWidth(8, 50)


    #### --- Отображение списка ---
    def Populate(self,date):
	self.DeleteAllItems()

	#### --- Массив идентификаторов строк ---
	self.kod_record = []
	
	### --- Получение списка ---
	for row in  GetListTask2(date):
	    index = self.InsertStringItem(sys.maxint, row[0])
	    self.SetStringItem(index, 0, row[2])
	    self.SetStringItem(index, 1, row[3])
	    self.SetStringItem(index, 2, row[7])
	    if row[8] == 0:
		self.SetStringItem(index, 3, u'НЕТ')
	    if row[8] == 1:
		self.SetStringItem(index, 3, u'РЕМОНТ')
	    if row[8] == 2:
		self.SetStringItem(index, 3, u'МОНТАЖ')
	    self.SetStringItem(index, 4, row[9])
	    self.SetStringItem(index, 5, row[10])
	    self.SetStringItem(index, 6, row[11])
	    self.SetStringItem(index, 7, row[12])
	    self.SetStringItem(index, 8, row[13])


	    ### --- Окрашиваем в синий если заявка закрыта ---
	    if row[21]==1:
		self.SetItemTextColour(index,wx.BLUE)

	    ### --- Окрашиваем в красный если заявка удалена ---
	    if len(row[20])!=0:
		self.SetItemTextColour(index,wx.RED)


	    #### --- Заполнение массива идентификаторов строк ---
	    self.kod_record.append(row[0])
	    
	#### --- текущая первая строка ---    
	self.currentItem=0
	


