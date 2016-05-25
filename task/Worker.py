#coding:utf-8

import  wx
import	sys
from	task.RunSQL	import	AddWorker
from	task.RunSQL	import	GetListWorker
from	task.RunSQL	import	GetWorker
from	task.RunSQL	import	EditWorker
from	task.RunSQL	import	DelWorker
from	tools.Messages	import	SaveDone
from	tools.Messages	import	ErrorData
from	tools.Messages	import	NotAccess




#### --- Форма ввода нового исполнителя и редактирования ---
class EditPerson(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, 
            style=wx.DEFAULT_DIALOG_STYLE, kod_rec='NONE'
            ):

	self.kod_rec = kod_rec

        pre = wx.PreDialog()
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)



#### --- Заголовок ---
        sizer = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, -1, "Исполнитель")
	label.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(label, 0, wx.ALIGN_LEFT|wx.ALL, 5)


        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER, 5)


#### --- Текстовые метки ---
        label0 = wx.StaticText(self, -1, "Фамилия")
        label1 = wx.StaticText(self, -1, "Имя")
        label2 = wx.StaticText(self, -1, "Отчество")

#### --- Поля ввода информации ---
    	self.field_0 = wx.TextCtrl(self, -1, "", size=(300,-1))
    	self.field_1 = wx.TextCtrl(self, -1, "", size=(300,-1))
    	self.field_2 = wx.TextCtrl(self, -1, "", size=(300,-1))
	

#### --- Размещение элементов ---
	fgsizer = wx.FlexGridSizer(rows = 3, cols = 2, hgap = 10, vgap = 10)
	fgsizer.Add(label0,0,0)
	fgsizer.Add(self.field_0,0,0)
	fgsizer.Add(label1,0,0)
	fgsizer.Add(self.field_1,0,0)
	fgsizer.Add(label2,0,0)
	fgsizer.Add(self.field_2,0,0)

        sizer.Add(fgsizer, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER, 5)


#### --- Кнопки ---
        box = wx.BoxSizer(wx.HORIZONTAL)
        btn = wx.Button(self, wx.ID_OK)
        box.Add(btn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        btn2 = wx.Button(self, wx.ID_CANCEL)
        box.Add(btn2, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)

	    
	if self.kod_rec != 'NONE':
	    self.ShowValue()



#### --- Отображение значений в форме ----
    def	ShowValue(self):
	r = GetWorker(self.kod_rec)
	self.field_0.SetValue(r[1])
	self.field_1.SetValue(r[2])
	self.field_2.SetValue(r[3])






#### --- Форма списка исполнителей ---
class ListPerson(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, 
            style=wx.DEFAULT_DIALOG_STYLE
            ):


        pre = wx.PreDialog()
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)

	tID = wx.NewId()


#### --- Заголовок ---
        sizer = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, -1, "Исполнители")
	label.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(label, 0, wx.ALIGN_LEFT|wx.ALL, 5)

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER, 5)

	box = wx.BoxSizer(wx.HORIZONTAL)
	self.ctrl0 = List(pre, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl0.Populate()
	self.ctrl0.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
	box.Add(self.ctrl0, 1, wx.ALIGN_CENTRE|wx.ALL, 5)	
	sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER, 5)


#### --- Кнопки ---
        btn = wx.Button(self, wx.ID_ADD)
        btn1 = wx.Button(self, wx.ID_DELETE)
        btn3 = wx.Button(self, wx.ID_CLOSE)

        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(btn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(btn1, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(btn3, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)
	    
	self.Bind(wx.EVT_BUTTON, self.Add, btn)
	self.Bind(wx.EVT_BUTTON, self.Del, btn1)
	self.Bind(wx.EVT_BUTTON, self.Cancel, btn3)
	self.ctrl0.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem, self.ctrl0)
	self.ctrl0.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.Edit, self.ctrl0)





#### --- Присвоение значение по выбранной строке ----
    def ReadItem(self,event):
	self.ctrl0.currentItem = event.m_itemIndex
	
#### --- Кнопка Cancel ----
    def Cancel(self,event):
	self.Destroy()


#### --- Кнопка добавить ---
    def	Add(self,event):
	dlg = EditPerson(self,-1,"Новый исполнитель", size=(450,300), style = wx.DEFAULT_DIALOG_STYLE)
	if dlg.ShowModal() == wx.ID_OK:
	    result = AddWorker(dlg.field_0.GetValue(),dlg.field_1.GetValue(),dlg.field_2.GetValue())
	    if result == 'OK':
		self.ctrl0.Populate()
		self.ctrl0.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
	    elif result == 'NOTACCESS':
		NotAccess(self)
	    elif result == 'ERRORDATA':
		ErrorData(self)
	dlg.Destroy()




#### --- Изменение (редактирование) ---
    def	Edit(self,event):
	kod_row = self.ctrl0.kod_record[self.ctrl0.currentItem]
	select_id = self.ctrl0.currentItem
	dlg = EditPerson(self,-1,"Исполнитель", size=(450,300), style = wx.DEFAULT_DIALOG_STYLE, kod_rec=kod_row)
	if dlg.ShowModal() == wx.ID_OK:
	    result = EditWorker(kod_row,dlg.field_0.GetValue(),dlg.field_1.GetValue(),dlg.field_2.GetValue())
	    if result == 'OK':
		self.ctrl0.Populate()
		self.ctrl0.SetItemState(select_id, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
	    elif result == 'NOTACCESS':
		NotAccess(self)
	    elif result == 'ERRORDATA':
		ErrorData(self)
	dlg.Destroy()




#### --- Кнопка удалить ---
    def	Del(self,event):
	kod_row = self.ctrl0.kod_record[self.ctrl0.currentItem]
	if len(kod_row) == 24:
	    dlg = wx.MessageDialog(self,"Удалить исполнителя?","Удаление",style=wx.YES_NO)
	    if dlg.ShowModal() == wx.ID_YES:
		result = DelWorker(kod_row)
		if result == 'OK':
		    self.ctrl0.Populate()
		    self.ctrl0.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
		elif result == 'NOTACCESS':
		    NotAccess(self)
		elif result == 'ERRORDATA':
		    ErrorData(self)
	    dlg.Destroy()





#### --- Элемент со списком  ----
class List(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0), size=(600,300), style=0):
	wx.ListCtrl.__init__(self, parent, ID, pos, size, style)

	self.InsertColumn(0,"Фамилия")
	self.InsertColumn(1,"Имя")
	self.InsertColumn(2,"Отчество")

	self.SetColumnWidth(0, 200)
	self.SetColumnWidth(1, 200)
	self.SetColumnWidth(2, 200)


    #### --- Отображение списка ---
    def Populate(self):
	self.DeleteAllItems()

	#### --- Массив идентификаторов строк ---
	self.kod_record = []
	
	### --- Получение списка ---
	for row in  GetListWorker():
	    index = self.InsertStringItem(sys.maxint, row[0])
	    self.SetStringItem(index, 0, row[1])
	    self.SetStringItem(index, 1, row[2])
	    self.SetStringItem(index, 2, row[3])
	    
	    #### --- Заполнение массива идентификаторов строк ---
	    self.kod_record.append(row[0])
	    
	#### --- текущая первая строка ---    
	self.currentItem=0
	


