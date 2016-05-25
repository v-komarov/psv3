#coding:utf-8

""" Изменение заявки """

import  wx
import	DBTools
import	wx.lib.masked as masked
from	WList		import	ListTaskWorker
from	WList		import	ChWorker
from	MList		import	ChMate
from	MList		import	ListTaskMate
from	task.RunSQL	import	GetListNameTask
from	task.RunSQL	import	GetTask
from	task.RunSQL	import	GetListStatus
from	task.RunSQL	import	GetListFIO
from	task.RunSQL	import	EditTask as TaskEdit
from	task.RunSQL	import	AddTaskWorker
from	task.RunSQL	import	DelTaskWorker
from	task.RunSQL	import	GetListTaskWorker
from	task.RunSQL	import	AddTaskMate
from	task.RunSQL	import	DelTaskMate
from	tools.Messages	import	NotAccess
from	tools.Messages	import	ErrorData
from	tools.Messages	import	SaveDone




class EditTask(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, 
            style=wx.DEFAULT_DIALOG_STYLE, kod_rec='NONE'):

	self.kod_rec = kod_rec

	self.fio = ''


        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)

	tID = wx.NewId()
	tID2 = wx.NewId()

        sizer = wx.BoxSizer(wx.VERTICAL)


#### ---- Строка интерфейса с датой и временем создания этой заявки ---
        box = wx.BoxSizer(wx.HORIZONTAL)
        label0 = wx.StaticText(self, -1, "Дата и время создания заявки: ")
	self.field_00 = wx.TextCtrl(self, -1, "", size=(150,-1), style=wx.TE_READONLY)
        box.Add(label0, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(self.field_00, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
	


#### ---- Строка интерфейса с датой и временем закрытия этой заявки ---
        box = wx.BoxSizer(wx.HORIZONTAL)
        label000 = wx.StaticText(self, -1, "Дата и время закрытия заявки: ")
	self.field_000 = wx.TextCtrl(self, -1, "", size=(150,-1), style=wx.TE_READONLY)
        box.Add(label000, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(self.field_000, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.ALIGN_CENTRE|wx.ALL, 5)



#### ---- Строка интерфейса с датой и временем заявки ---
        box = wx.BoxSizer(wx.HORIZONTAL)
        label1 = wx.StaticText(self, -1, "Дата")
        self.field_0 = wx.DatePickerCtrl(self, -1, size=(120,-1), style=wx.DP_DROPDOWN|wx.DP_SHOWCENTURY)
        label2 = wx.StaticText(self, -1, "Время")
	self.mytime = masked.TimeCtrl(self, -1, name="", fmt24hr=True, display_seconds = False)
        label3 = wx.StaticText(self, -1, "Статус")
        self.field_1 = wx.ComboBox(self, -1, "", size=(150,-1), choices=GetListStatus(), style=wx.CB_READONLY)
        label4 = wx.StaticText(self, -1, "Тип")
        self.field_2 = wx.ComboBox(self, -1, "", size=(150,-1), choices=['РЕМОНТ','МОНТАЖ'], style=wx.CB_READONLY)

        box.Add(label1, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(self.field_0, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(label2, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(self.mytime, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(label3, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(self.field_1, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(label4, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(self.field_2, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.ALIGN_CENTRE|wx.ALL, 5)


#### ---- Строка интерфейса с текстом заявки ---
        box = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self, -1, "Заявка")
        self.field_3 = wx.ComboBox(self, -1, "", size=(500,-1), choices=GetListNameTask())

        box.Add(label, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        box.Add(self.field_3, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        sizer.Add(box, 0, wx.ALIGN_LEFT|wx.ALL, 5)

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTRE, 5)



#### --- Адрес заявки ---
        box = wx.BoxSizer(wx.HORIZONTAL)

        label = wx.StaticText(self, -1, "Улица")
        label2 = wx.StaticText(self, -1, "Дом")
        label3 = wx.StaticText(self, -1, "Квартира")
        label4 = wx.StaticText(self, -1, "Подъезд")
        label5 = wx.StaticText(self, -1, "Телефон")

	self.field_4 = wx.TextCtrl(self, -1, "", size=(150,-1), style=wx.TE_READONLY)
	self.field_5 = wx.TextCtrl(self, -1, "", size=(50,-1), style=wx.TE_READONLY)
	self.field_6 = wx.TextCtrl(self, -1, "", size=(50,-1), style=wx.TE_READONLY)
	self.field_7 = wx.TextCtrl(self, -1, "", size=(50,-1))
	self.field_8 = wx.TextCtrl(self, -1, "", size=(150,-1))

        box.Add(label, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        box.Add(self.field_4, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        box.Add(label2, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        box.Add(self.field_5, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        box.Add(label3, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        box.Add(self.field_6, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        box.Add(label4, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        box.Add(self.field_7, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        box.Add(label5, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        box.Add(self.field_8, 0, wx.ALIGN_LEFT|wx.ALL, 5)

        sizer.Add(box, 0, wx.ALIGN_LEFT|wx.ALL, 5)


#### --- Количество сотрудников, человеко-часы ----
        box = wx.BoxSizer(wx.HORIZONTAL)

        label = wx.StaticText(self, -1, "Планируемые чел./часы")
        label2 = wx.StaticText(self, -1, "Количество исполнителей")
        label3 = wx.StaticText(self, -1, "Фактическое чел./часы")

	self.field_9 = wx.TextCtrl(self, -1, "", size=(50,-1))
	self.field_10 = wx.TextCtrl(self, -1, "", size=(50,-1))
	self.field_11 = wx.TextCtrl(self, -1, "", size=(50,-1))

        box.Add(label, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        box.Add(self.field_9, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        box.Add(label2, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        box.Add(self.field_10, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        box.Add(label3, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        box.Add(self.field_11, 0, wx.ALIGN_LEFT|wx.ALL, 5)

        sizer.Add(box, 0, wx.ALIGN_LEFT|wx.ALL, 5)



#### --- Примечание ----
        box = wx.BoxSizer(wx.HORIZONTAL)

        label = wx.StaticText(self, -1, "Примечание")
	self.field_12 = wx.TextCtrl(self, -1, "", size=(600,100), style=wx.TE_MULTILINE)
        box.Add(label, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        box.Add(self.field_12, 0, wx.ALIGN_LEFT|wx.ALL, 5)

#### ---- Кнопки управления ----        
        btnsizer = wx.BoxSizer(wx.VERTICAL)
        btn = wx.Button(self, wx.ID_SAVE)
        btn2 = wx.Button(self, wx.ID_CLOSE)
        btnsizer.Add(btn, 0, wx.ALIGN_CENTRE|wx.ALL|wx.GROW, 5)
        btnsizer.Add(btn2, 0, wx.ALIGN_CENTRE|wx.ALL|wx.GROW, 5)
        box.Add(btnsizer, 0, wx.ALIGN_CENTRE|wx.ALL, 5)


        sizer.Add(box, 0, wx.ALIGN_LEFT|wx.ALL, 5)

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTRE, 5)



#### --- Исполнители ----
        box = wx.BoxSizer(wx.HORIZONTAL)

	box_i = wx.BoxSizer(wx.VERTICAL)

        label = wx.StaticText(self, -1, "Исполнители")
	self.ctrl0 = ListTaskWorker(self,tID,style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl0.Populate(self.kod_rec)
	self.ctrl0.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)

        box_i.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        box_i.Add(self.ctrl0, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        btnsizer = wx.BoxSizer(wx.HORIZONTAL)
        btn5 = wx.Button(self, 101, "Добавить")
        btn6 = wx.Button(self, 102, "Удалить")
        btnsizer.Add(btn5, 0, wx.ALIGN_CENTRE|wx.ALL|wx.GROW, 5)
        btnsizer.Add(btn6, 0, wx.ALIGN_CENTRE|wx.ALL|wx.GROW, 5)
        box_i.Add(btnsizer, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        box.Add(box_i, 0, wx.ALIGN_CENTRE|wx.ALL, 5)



	box_ii = wx.BoxSizer(wx.VERTICAL)

        label = wx.StaticText(self, -1, "Материалы")
	self.ctrl1 = ListTaskMate(self,tID,style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl1.Populate(self.kod_rec)
	self.ctrl1.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)

        box_ii.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        box_ii.Add(self.ctrl1, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        btnsizer = wx.BoxSizer(wx.HORIZONTAL)
        btn7 = wx.Button(self, 201, "Добавить")
        btn8 = wx.Button(self, 202, "Удалить")
        btnsizer.Add(btn7, 0, wx.ALIGN_CENTRE|wx.ALL|wx.GROW, 5)
        btnsizer.Add(btn8, 0, wx.ALIGN_CENTRE|wx.ALL|wx.GROW, 5)
        box_ii.Add(btnsizer, 0, wx.ALIGN_CENTRE|wx.ALL, 5)


        box.Add(box_ii, 0, wx.ALIGN_CENTRE|wx.ALL, 5)




        sizer.Add(box, 0, wx.ALIGN_CENTRE|wx.ALL, 5)





        btnsizer = wx.BoxSizer(wx.VERTICAL)




        self.SetSizer(sizer)
        sizer.Fit(self)


	self.ShowValue()
	

	self.Bind(wx.EVT_BUTTON, self.Save, btn)
	self.Bind(wx.EVT_BUTTON, self.Close, btn2)
	self.Bind(wx.EVT_BUTTON, self.AddWorker, btn5)
	self.Bind(wx.EVT_BUTTON, self.DelWorker, btn6)
	self.Bind(wx.EVT_BUTTON, self.AddMate, btn7)
	self.Bind(wx.EVT_BUTTON, self.DelMate, btn8)
	self.Bind(wx.EVT_LISTBOX, self.EvtListBox, self.field_12)
	self.ctrl0.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem, self.ctrl0)
	self.ctrl1.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem2, self.ctrl0)


#### --- Присвоение значения по выбранной строке ---
    def ReadItem(self,event):
	self.ctrl0.currentItem = event.m_itemIndex



#### --- Присвоение значения по выбранной строке ---
    def ReadItem2(self,event):
	self.ctrl1.currentItem = event.m_itemIndex



#### --- Обработка лист бокса ---
    def	EvtListBox(self,evt):
	self.fio = evt.GetString()



#### ---- Закрыть форму ---
    def	Close(self,evt):
	self.Destroy()


#### ---- Сохранить данные ---
    def	Save(self,evt):
	date0 = str(self.field_0.GetValue().GetYear())+'-' + str(self.field_0.GetValue().GetMonth()+1) +'-'+ str(self.field_0.GetValue().GetDay()) + ' ' + self.mytime.GetValue()	

	if self.field_2.GetValue().encode("utf-8") == 'НЕТ':
	    kod_type = 0
	elif self.field_2.GetValue().encode("utf-8") == 'РЕМОНТ':
	    kod_type = 1
	elif self.field_2.GetValue().encode("utf-8") == 'МОНТАЖ':
	    kod_type = 2
	
	result = TaskEdit(self.kod_rec, date0, self.field_1.GetValue(), kod_type, self.field_3.GetValue(), self.field_7.GetValue(), self.field_8.GetValue(), self.field_9.GetValue(), self.field_10.GetValue(), self.field_11.GetValue(), self.field_12.GetValue())
	if result == 'ERRORDATA':
	    ErrorData(self)
	elif result == 'NOTACCESS':
	    NotAccess(self)
	    self.ShowValue()
	elif result == 'OK':
	    SaveDone(self)
	    self.ShowValue()



#### ---- Добавить исполнителя ----
    def	AddWorker(self,evt):
	dlg = ChWorker(self,-1,'Выбор исполнителя',size=(400,250),style=wx.DEFAULT_DIALOG_STYLE)
	if dlg.ShowModal() == wx.ID_OK:
	    row_id = dlg.ctrl0.kod_record[dlg.ctrl0.currentItem]
	    result = AddTaskWorker(self.kod_rec,row_id)
	    if result == 'ERRORDATA':
		ErrorData(self)
	    elif result == 'NOTACCESS':
		NotAccess(self)
	    elif result == 'OK':
		self.ctrl0.Populate(self.kod_rec)
		self.ctrl0.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
	dlg.Destroy()
    
    
#### ---- Удалить исполнителя ----
    def	DelWorker(self,evt):
	dlg = wx.MessageDialog(self,"Удалить исполнителя?","Удаление",style=wx.YES_NO)
	if dlg.ShowModal() == wx.ID_YES:
	    row_id = self.ctrl0.kod_record[self.ctrl0.currentItem]
	    result = DelTaskWorker(self.kod_rec,row_id)
	    if result == 'OK':
		self.ctrl0.Populate(self.kod_rec)
		self.ctrl0.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
	    elif result == 'NOTACCESS':
		NotAccess(self)
	    elif result == 'ERRORDATA':
		ErrorData(self)
	    dlg.Destroy()


#### ---- Добавить материал ----
    def	AddMate(self,evt):
	dlg = ChMate(self,-1,'Выбор материала',size=(400,250),style=wx.DEFAULT_DIALOG_STYLE)
	if dlg.ShowModal() == wx.ID_OK:
	    row_id = dlg.ctrl0.kod_record[dlg.ctrl0.currentItem]
	    result = AddTaskMate(row_id,row_id.split('#')[1],row_id.split('#')[0],dlg.field_1.GetValue(),self.kod_rec)
	    if result == 'ERRORDATA':
		ErrorData(self)
	    elif result == 'NOTACCESS':
		NotAccess(self)
	    elif result == 'OK':
		self.ctrl1.Populate(self.kod_rec)
		self.ctrl1.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
	dlg.Destroy()



#### ---- Удалить материал ----
    def	DelMate(self,evt):
	dlg = wx.MessageDialog(self,"Удалить материал?","Удаление",style=wx.YES_NO)
	if dlg.ShowModal() == wx.ID_YES:
	    row_id = self.ctrl1.kod_record[self.ctrl1.currentItem]
	    result = DelTaskMate(row_id)
	    if result == 'OK':
		self.ctrl1.Populate(self.kod_rec)
		self.ctrl1.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
	    elif result == 'NOTACCESS':
		NotAccess(self)
	    elif result == 'ERRORDATA':
		ErrorData(self)
	    dlg.Destroy()



#### ---- Получение данных в форму ----
    def	ShowValue(self):
	r = GetTask(self.kod_rec)


	## --- Дата и время создания заявки ---
	self.field_00.SetValue(r[19])

	## --- Дата и время закрытия заявки ---
	if r[21] == 1:
	    self.field_000.SetValue(r[22])
	    self.SetTitle("Заявка закрыта")
		
	## --- Заявка удалена ---
	if r[20] != '':
	    self.SetTitle("Заявка удалена!")
	    


	d0 = wx.DateTime()
	d0.SetYear(r[4])
	d0.SetMonth(r[5]-1)
	d0.SetDay(r[6])

	self.mytime.SetValue(r[3])

	self.field_0.SetValue(d0)
	self.field_1.SetValue(r[7])
	if r[8] == 0:
	    self.field_2.SetValue('НЕТ')
	elif r[8] == 1:
	    self.field_2.SetValue('РЕМОНТ')
	elif r[8] == 2:
	    self.field_2.SetValue('МОНТАЖ')	    

	self.field_3.SetValue(r[9])
	self.field_4.SetValue(r[10])
	self.field_5.SetValue(r[11])
	self.field_6.SetValue(r[12])
	self.field_7.SetValue(r[13])
	self.field_8.SetValue(r[14])
	self.field_9.SetValue(str(r[15]))
	self.field_10.SetValue(str(r[16]))
	self.field_11.SetValue(str(r[17]))
	self.field_12.SetValue(r[18])

