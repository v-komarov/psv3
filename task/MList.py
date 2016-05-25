#coding:utf-8

"""
    Отображение расхода материалов
"""

import  wx
import	sys


from	RunSQL	import	GetListMateGroup
from	RunSQL	import	GetListMateStore
from	RunSQL	import	GetListMate



#### --- Элемент со списком материалов  ----
class ListTaskMate(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0), size=(400,100), style=0):
	wx.ListCtrl.__init__(self, parent, ID, pos, size, style)

	self.InsertColumn(0,"Название")
	self.InsertColumn(1,"Ед.из.")
	self.InsertColumn(2,"Кол-во")
	self.InsertColumn(3,"Цена")
	self.InsertColumn(4,"Сумма")

	self.SetColumnWidth(0, 150)
	self.SetColumnWidth(1, 70)
	self.SetColumnWidth(2, 70)
	self.SetColumnWidth(3, 70)
	self.SetColumnWidth(4, 100)


    #### --- Отображение списка ---
    def Populate(self, task_kod):
	self.DeleteAllItems()

	#### --- Массив идентификаторов строк ---
	self.kod_record = []
	
	### --- Получение списка ---
	for row in  GetListMate(task_kod):
	    index = self.InsertStringItem(sys.maxint, row[0])
	    self.SetStringItem(index, 0, row[2])
	    self.SetStringItem(index, 1, row[3])
	    self.SetStringItem(index, 2, row[4])
	    self.SetStringItem(index, 3, row[5])
	    self.SetStringItem(index, 4, row[6])
	    
	    #### --- Заполнение массива идентификаторов строк ---
	    self.kod_record.append(row[0])
	    
	#### --- текущая первая строка ---    
	self.currentItem=0
	

    #### --- Присвоение значения по выбранной строке  ---
    def ReadItem(self,event):
	self.currentItem = event.m_itemIndex









#### --- Форма выбора  ----
class ChMate(wx.Dialog):
    def __init__(self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE):

    	pre = wx.PreDialog()
    	pre.Create(parent, ID, title, pos, size, style)

    	self.PostCreate(pre)

	tID = wx.NewId()

    	sizer = wx.BoxSizer(wx.VERTICAL)

	
	#### --- Форма ввода данных ---
	#### --- Метки ------
	self.label0 = wx.StaticText(self, -1, "Группа")	

	#### --- Поля ввода ---
	self.field_0 = wx.ComboBox(self, -1, "", size=(300,-1), choices=GetListMateGroup(), style=wx.CB_DROPDOWN|wx.CB_READONLY)


	#### --- Размещение
	fgsizer = wx.FlexGridSizer( rows = 1, cols = 2, hgap = 10, vgap = 10 )
	fgsizer.Add(self.label0,0,0)
	fgsizer.Add(self.field_0,0,0)
    	sizer.Add(fgsizer, 0, wx.GROW|wx.ALIGN_CENTER|wx.ALL, 5)



	## -- Кнопка сохранения значения полей --
	self.btn = wx.Button(self, wx.ID_OK)
	self.btn2 = wx.Button(self, wx.ID_CANCEL)


   	line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
    	sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER|wx.TOP, 5)


        box = wx.BoxSizer(wx.HORIZONTAL)
        self.ctrl0 = ListMate(pre, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
        box.Add(self.ctrl0, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)



	#### --- Метки ------
	self.label1 = wx.StaticText(self, -1, "Количество")
	
	#### --- Поля ввода ---
	self.field_1 = wx.TextCtrl(self, -1, "1", size=(100,-1))

	#### --- Размещение
	fgsizer2 = wx.FlexGridSizer( rows = 1, cols = 2, hgap = 10, vgap = 10 )
	fgsizer2.Add(self.label1,0,0)
	fgsizer2.Add(self.field_1,0,0)
    	sizer.Add(fgsizer2, 0, wx.GROW|wx.ALIGN_CENTER|wx.ALL, 5)


   	line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
    	sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER|wx.TOP, 5)

	
	box = wx.BoxSizer(wx.HORIZONTAL)
    	box.Add(self.btn, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    	box.Add(self.btn2, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    	sizer.Add(box, 0, wx.ALIGN_CENTER|wx.ALL, 5)



    	self.SetSizer(sizer)
    	sizer.Fit(self)



	self.ctrl0.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem, self.ctrl0)
	self.Bind(wx.EVT_COMBOBOX, self.ChGroup, self.field_0)



	
#### --- Присвоение значения по выбранной строке ---
    def ReadItem(self,event):
	self.ctrl0.currentItem = event.m_itemIndex




#### ---- Смена группы материала ---
    def	ChGroup(self,event):
	group = self.field_0.GetValue()
	self.ctrl0.Populate(group)
	self.ctrl0.SetItemState(0,wx.LIST_STATE_SELECTED,wx.LIST_STATE_SELECTED)






class ListMate(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0),size=(600,300), style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)


        self.InsertColumn(0, "Название")
        self.InsertColumn(1, "Ед.из.")
        self.InsertColumn(2, "Кол-во")
        self.InsertColumn(3, "Цена")
        self.InsertColumn(4, "Склад")

    	self.SetColumnWidth(0, 300)
    	self.SetColumnWidth(1, 70)
    	self.SetColumnWidth(2, 70)
    	self.SetColumnWidth(3, 70)
    	self.SetColumnWidth(4, 200)



    def Populate(self,group):

	self.DeleteAllItems()


#### --- Отображение данных в форме ---
	self.kod_record=[] # массив идентификаторов записей
	     
	for row in GetListMateStore(group):
	    index=self.InsertStringItem(sys.maxint, row[0])
	    self.SetStringItem( index, 0, row[1])
	    self.SetStringItem( index, 1, row[2])
	    self.SetStringItem( index, 2, row[4])
	    self.SetStringItem( index, 3, row[6])
	    self.SetStringItem( index, 4, row[7])
	# -- Заполнение массива идентификаторов записей ---
	    self.kod_record.append(row[0])    
	    
	self.currentItem=0

















