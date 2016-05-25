 
#coding:utf-8


import	sys
import  wx

from	RunSQL	import	GetListKassa
from	RunSQL	import	GetUlDomP
from	RunSQL	import	GetUlDom
from	RunSQL	import	GetListStore
from	RunSQL	import	GetListGroup
from	RunSQL	import	GetListService


#*************************************************************************
# Форма получения периода
#*************************************************************************



#### --- Период ----
class GetPeriod(wx.Dialog):
    def __init__(self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE):

    	pre = wx.PreDialog()
    	pre.Create(parent, ID, title, pos, size, style)

    	self.PostCreate(pre)

	tID = wx.NewId()


    	sizer = wx.BoxSizer(wx.VERTICAL)
	
	#### --- Форма ввода данных ---
	#### --- Метки ------
	self.label0 = wx.StaticText(self, -1, "С даты")
	self.label1 = wx.StaticText(self, -1, "по дату")
	

	#### --- Поля ввода ---
	self.field_0 = wx.DatePickerCtrl(self, -1, size=(150,-1), style=wx.DP_DROPDOWN|wx.DP_SHOWCENTURY)
	self.field_1 = wx.DatePickerCtrl(self, -1, size=(150,-1), style=wx.DP_DROPDOWN|wx.DP_SHOWCENTURY)


	## -- Кнопка сохранения значения полей --
	self.btn = wx.Button(self, wx.ID_OK)
	self.btn2 = wx.Button(self, wx.ID_CANCEL)
	

	#### --- Размещение
	fgsizer = wx.FlexGridSizer( rows = 2, cols = 2, hgap = 10, vgap = 10 )
	fgsizer.Add(self.label0,0,0)
	fgsizer.Add(self.field_0,0,0)
	fgsizer.Add(self.label1,0,0)
	fgsizer.Add(self.field_1,0,0)
    	sizer.Add(fgsizer, 0, wx.GROW|wx.ALIGN_CENTER|wx.ALL, 5)

   	line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
    	sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER|wx.TOP, 5)
	
	box = wx.BoxSizer(wx.HORIZONTAL)
    	box.Add(self.btn, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    	box.Add(self.btn2, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    	sizer.Add(box, 0, wx.ALIGN_CENTER|wx.ALL, 5)





    	self.SetSizer(sizer)
    	sizer.Fit(self)
	











#### --- Период и выбор кассы ----
class GetPeriodKassa(wx.Dialog):
    def __init__(self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE):

    	pre = wx.PreDialog()
    	pre.Create(parent, ID, title, pos, size, style)

    	self.PostCreate(pre)

	tID = wx.NewId()


    	sizer = wx.BoxSizer(wx.VERTICAL)
	
	#### --- Форма ввода данных ---
	#### --- Метки ------
	self.label0 = wx.StaticText(self, -1, "С даты")
	self.label1 = wx.StaticText(self, -1, "по дату")
	self.label2 = wx.StaticText(self, -1, "Касса")
	

	#### --- Поля ввода ---
	self.field_0 = wx.DatePickerCtrl(self, -1, size=(150,-1), style=wx.DP_DROPDOWN|wx.DP_SHOWCENTURY)
	self.field_1 = wx.DatePickerCtrl(self, -1, size=(150,-1), style=wx.DP_DROPDOWN|wx.DP_SHOWCENTURY)
	self.field_2 = wx.ComboBox(self, -1, "BCE",size=(200,-1), choices=GetListKassa(), style=wx.CB_DROPDOWN|wx.CB_READONLY)


	## -- Кнопка сохранения значения полей --
	self.btn = wx.Button(self, wx.ID_OK)
	self.btn2 = wx.Button(self, wx.ID_CANCEL)
	

	#### --- Размещение
	fgsizer = wx.FlexGridSizer( rows = 2, cols = 2, hgap = 10, vgap = 10 )
	fgsizer.Add(self.label0,0,0)
	fgsizer.Add(self.field_0,0,0)
	fgsizer.Add(self.label1,0,0)
	fgsizer.Add(self.field_1,0,0)
	fgsizer.Add(self.label2,0,0)
	fgsizer.Add(self.field_2,0,0)
    	sizer.Add(fgsizer, 0, wx.GROW|wx.ALIGN_CENTER|wx.ALL, 5)

   	line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
    	sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER|wx.TOP, 5)
	
	box = wx.BoxSizer(wx.HORIZONTAL)
    	box.Add(self.btn, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    	box.Add(self.btn2, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    	sizer.Add(box, 0, wx.ALIGN_CENTER|wx.ALL, 5)





    	self.SetSizer(sizer)
    	sizer.Fit(self)
	










#### --- Период и выбор услуги ----
class GetPeriodService(wx.Dialog):
    def __init__(self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE):

    	pre = wx.PreDialog()
    	pre.Create(parent, ID, title, pos, size, style)

    	self.PostCreate(pre)

	tID = wx.NewId()


    	sizer = wx.BoxSizer(wx.VERTICAL)
	
	#### --- Форма ввода данных ---
	#### --- Метки ------
	self.label0 = wx.StaticText(self, -1, "С даты")
	self.label1 = wx.StaticText(self, -1, "по дату")
	self.label2 = wx.StaticText(self, -1, "Услуга")
	

	#### --- Поля ввода ---
	self.field_0 = wx.DatePickerCtrl(self, -1, size=(150,-1), style=wx.DP_DROPDOWN|wx.DP_SHOWCENTURY)
	self.field_1 = wx.DatePickerCtrl(self, -1, size=(150,-1), style=wx.DP_DROPDOWN|wx.DP_SHOWCENTURY)
	self.field_2 = wx.ComboBox(self, -1,"" ,size=(200,-1), choices=GetListService(), style=wx.CB_DROPDOWN|wx.CB_READONLY)


	## -- Кнопка сохранения значения полей --
	self.btn = wx.Button(self, wx.ID_OK)
	self.btn2 = wx.Button(self, wx.ID_CANCEL)
	

	#### --- Размещение
	fgsizer = wx.FlexGridSizer( rows = 2, cols = 2, hgap = 10, vgap = 10 )
	fgsizer.Add(self.label0,0,0)
	fgsizer.Add(self.field_0,0,0)
	fgsizer.Add(self.label1,0,0)
	fgsizer.Add(self.field_1,0,0)
	fgsizer.Add(self.label2,0,0)
	fgsizer.Add(self.field_2,0,0)
    	sizer.Add(fgsizer, 0, wx.GROW|wx.ALIGN_CENTER|wx.ALL, 5)

   	line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
    	sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER|wx.TOP, 5)
	
	box = wx.BoxSizer(wx.HORIZONTAL)
    	box.Add(self.btn, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    	box.Add(self.btn2, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    	sizer.Add(box, 0, wx.ALIGN_CENTER|wx.ALL, 5)





    	self.SetSizer(sizer)
    	sizer.Fit(self)
	












#### --- Период и выбор склада ----
class GetPeriodStore(wx.Dialog):
    def __init__(self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE):

    	pre = wx.PreDialog()
    	pre.Create(parent, ID, title, pos, size, style)

    	self.PostCreate(pre)

	tID = wx.NewId()


    	sizer = wx.BoxSizer(wx.VERTICAL)
	
	#### --- Форма ввода данных ---
	#### --- Метки ------
	self.label0 = wx.StaticText(self, -1, "С даты")
	self.label1 = wx.StaticText(self, -1, "по дату")
	self.label2 = wx.StaticText(self, -1, "Склад")
	

	#### --- Поля ввода ---
	self.field_0 = wx.DatePickerCtrl(self, -1, size=(150,-1), style=wx.DP_DROPDOWN|wx.DP_SHOWCENTURY)
	self.field_1 = wx.DatePickerCtrl(self, -1, size=(150,-1), style=wx.DP_DROPDOWN|wx.DP_SHOWCENTURY)
	self.field_2 = wx.ComboBox(self, -1, "",size=(200,-1), choices=GetListStore(), style=wx.CB_DROPDOWN|wx.CB_READONLY)


	## -- Кнопка сохранения значения полей --
	self.btn = wx.Button(self, wx.ID_OK)
	self.btn2 = wx.Button(self, wx.ID_CANCEL)
	

	#### --- Размещение
	fgsizer = wx.FlexGridSizer( rows = 2, cols = 2, hgap = 10, vgap = 10 )
	fgsizer.Add(self.label0,0,0)
	fgsizer.Add(self.field_0,0,0)
	fgsizer.Add(self.label1,0,0)
	fgsizer.Add(self.field_1,0,0)
	fgsizer.Add(self.label2,0,0)
	fgsizer.Add(self.field_2,0,0)
    	sizer.Add(fgsizer, 0, wx.GROW|wx.ALIGN_CENTER|wx.ALL, 5)

   	line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
    	sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER|wx.TOP, 5)
	
	box = wx.BoxSizer(wx.HORIZONTAL)
    	box.Add(self.btn, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    	box.Add(self.btn2, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    	sizer.Add(box, 0, wx.ALIGN_CENTER|wx.ALL, 5)





    	self.SetSizer(sizer)
    	sizer.Fit(self)
	










#### --- Выбор периода, улицы, номера дома, номера подъезда ----
class ChoiseUlDomP(wx.Dialog):
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
        self.ctrl1 = ListUlDomP(pre, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl1.Populate()
	self.ctrl1.SetItemState(0,wx.LIST_STATE_SELECTED,wx.LIST_STATE_SELECTED)
        box.Add(self.ctrl1, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)


        box = wx.BoxSizer(wx.HORIZONTAL)

	#### --- Метки ------
	self.label0 = wx.StaticText(self, -1, "С")
	self.label1 = wx.StaticText(self, -1, "по")

	#### --- Поля ввода ---
	self.field_0 = wx.DatePickerCtrl(self, -1, size=(150,-1), style=wx.DP_DROPDOWN|wx.DP_SHOWCENTURY)
	self.field_1 = wx.DatePickerCtrl(self, -1, size=(150,-1), style=wx.DP_DROPDOWN|wx.DP_SHOWCENTURY)

	#### --- Размещение
	fgsizer = wx.FlexGridSizer( rows = 1, cols = 4, hgap = 10, vgap = 10 )
	fgsizer.Add(self.label0,0,0)
	fgsizer.Add(self.field_0,0,0)
	fgsizer.Add(self.label1,0,0)
	fgsizer.Add(self.field_1,0,0)
    	box.Add(fgsizer, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL, 5)


        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL, 5)

        

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTRE|wx.TOP, 5)

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
	




	

#### --- Элемент со списком улиц, домов и подъездов  ----
class ListUlDomP(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0), size=(370,200), style=0):
	wx.ListCtrl.__init__(self, parent, ID, pos, size, style)

	self.InsertColumn(0,"Улица")
	self.InsertColumn(1,"Дом")
	self.InsertColumn(2,"Подъезд")

	self.SetColumnWidth(0, 200)
	self.SetColumnWidth(1, 100)
	self.SetColumnWidth(2, 70)


    #### --- Отображение списка ---
    def Populate(self):
	self.DeleteAllItems()

	#### --- Массив идентификаторов строк ---
	self.kod_record = []
	
	### --- Получение списка ---
	for row in  GetUlDomP():
	    index = self.InsertStringItem(sys.maxint, row[0])
	    self.SetStringItem(index, 0, row[1])
	    self.SetStringItem(index, 1, row[2])
	    self.SetStringItem(index, 2, row[3])
	    
	    #### --- Заполнение массива идентификаторов строк ---
	    self.kod_record.append(row[0])
	    
	#### --- текущая первая строка ---    
	self.currentItem=0
	

    #### --- Присвоение значения по выбранной строке  ---
    def ReadItem(self,event):
	self.currentItem = event.m_itemIndex








#### --- Выбор склада и группы материалов ----
class ChoiceStoreGroup(wx.Dialog):
    def __init__(self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE):

    	pre = wx.PreDialog()
    	pre.Create(parent, ID, title, pos, size, style)

    	self.PostCreate(pre)

	tID = wx.NewId()


    	sizer = wx.BoxSizer(wx.VERTICAL)
	
	#### --- Форма ввода данных ---
	#### --- Метки ------
	self.label0 = wx.StaticText(self, -1, "Склад")
	self.label1 = wx.StaticText(self, -1, "Группа")
	

	#### --- Поля ввода ---
	self.field_0 = wx.ComboBox(self, -1, "",size=(200,-1), choices=GetListStore(), style=wx.CB_DROPDOWN|wx.CB_READONLY)
	self.field_1 = wx.ComboBox(self, -1, "",size=(200,-1), choices=GetListGroup(), style=wx.CB_DROPDOWN|wx.CB_READONLY)


	## -- Кнопка сохранения значения полей --
	self.btn = wx.Button(self, wx.ID_OK)
	self.btn2 = wx.Button(self, wx.ID_CANCEL)
	

	#### --- Размещение
	fgsizer = wx.FlexGridSizer( rows = 2, cols = 2, hgap = 10, vgap = 10 )
	fgsizer.Add(self.label0,0,0)
	fgsizer.Add(self.field_0,0,0)
	fgsizer.Add(self.label1,0,0)
	fgsizer.Add(self.field_1,0,0)
    	sizer.Add(fgsizer, 0, wx.GROW|wx.ALIGN_CENTER|wx.ALL, 5)

   	line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
    	sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER|wx.TOP, 5)
	
	box = wx.BoxSizer(wx.HORIZONTAL)
    	box.Add(self.btn, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    	box.Add(self.btn2, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    	sizer.Add(box, 0, wx.ALIGN_CENTER|wx.ALL, 5)





    	self.SetSizer(sizer)
    	sizer.Fit(self)
	









#### --- Выбор даты, улицы, номера дома ----
class ChoiseDateUlDom(wx.Dialog):
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
        self.ctrl1 = ListUlDom(pre, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl1.Populate()
	self.ctrl1.SetItemState(0,wx.LIST_STATE_SELECTED,wx.LIST_STATE_SELECTED)
        box.Add(self.ctrl1, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)


        box = wx.BoxSizer(wx.HORIZONTAL)

	#### --- Метки ------
	self.label0 = wx.StaticText(self, -1, "Дата")

	#### --- Поля ввода ---
	self.field_0 = wx.DatePickerCtrl(self, -1, size=(150,-1), style=wx.DP_DROPDOWN|wx.DP_SHOWCENTURY)

	#### --- Размещение
	fgsizer = wx.FlexGridSizer( rows = 1, cols = 4, hgap = 10, vgap = 10 )
	fgsizer.Add(self.label0,0,0)
	fgsizer.Add(self.field_0,0,0)
    	box.Add(fgsizer, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL, 5)


        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL, 5)

        

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTRE|wx.TOP, 5)

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
	




#### --- Элемент со списком улиц, домов  ----
class ListUlDom(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0), size=(220,200), style=0):
	wx.ListCtrl.__init__(self, parent, ID, pos, size, style)

	self.InsertColumn(0,"Улица")
	self.InsertColumn(1,"Дом")

	self.SetColumnWidth(0, 150)
	self.SetColumnWidth(1, 70)


    #### --- Отображение списка ---
    def Populate(self):
	self.DeleteAllItems()

	#### --- Массив идентификаторов строк ---
	self.kod_record = []
	
	### --- Получение списка ---
	for row in  GetUlDom():
	    index = self.InsertStringItem(sys.maxint, row[0])
	    self.SetStringItem(index, 0, row[0])
	    self.SetStringItem(index, 1, row[1])
	    
	    #### --- Заполнение массива идентификаторов строк ---
	    self.kod_record.append(row[0]+':'+row[1])
	    
	#### --- текущая первая строка ---    
	self.currentItem=0
	

    #### --- Присвоение значения по выбранной строке  ---
    def ReadItem(self,event):
	self.currentItem = event.m_itemIndex



