#coding:utf-8

""" Закладка 3 - Цены 
    вынесено в этот файл (что удалось), чтобы не загромождать MainForm.py
"""


import  wx
import	sys
from	RunSQLPage3	import	GetListCost
#from	base.Abonent	import	GetServiceOn


#### --- закладка 3 : Список цен , функция вызывается из MainForm.py ---
def Page3(self):
    page3 = self.Page()
    pagesizer = wx.BoxSizer(wx.VERTICAL)
    tID = wx.NewId()
    self.ctrl3 = ListCost(page3, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
    self.ctrl3.Populate(self.rec_kod)
    self.ctrl3.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
    pagesizer.Add(self.ctrl3, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    ### --- Кнопки ---
    sizer = wx.BoxSizer(wx.HORIZONTAL)
    self.button3Add = wx.Button(page3, 1030, "Добавить")
    self.button3Del = wx.Button(page3, 1031, "Удалить")
    sizer.Add(self.button3Add, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    sizer.Add(self.button3Del, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    pagesizer.Add(sizer, 0, wx.ALIGN_CENTER, 5)
    page3.SetSizer(pagesizer)
    pagesizer.Fit(self)


    self.Bind(wx.EVT_BUTTON, self.Add3, self.button3Add)
    self.Bind(wx.EVT_BUTTON, self.Del3, self.button3Del)
    self.ctrl3.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ctrl3.ReadItem, self.ctrl3)



    return page3





#### --- Элемент со списком цен  ----
class ListCost(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0), size=(500,200), style=0):
	wx.ListCtrl.__init__(self, parent, ID, pos, size, style)

	self.InsertColumn(0,"Дата начала действия")
	self.InsertColumn(1,"Ед. измерения")
	self.InsertColumn(2,"Цена")

	self.SetColumnWidth(0, 250)
	self.SetColumnWidth(1, 100)
	self.SetColumnWidth(2, 150)


    #### --- Отображение списка ---
    def Populate(self, kod):
	self.DeleteAllItems()

	#### --- Массив идентификаторов строк ---
	self.kod_record = []
	
	### --- Получение списка ---
	for row in  GetListCost(kod):
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









#*************************************************************************
# Форма ввода цены
#*************************************************************************



#### --- Новая цена ----
class AddNewCost(wx.Dialog):
    def __init__(self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE):

    	pre = wx.PreDialog()
    	pre.Create(parent, ID, title, pos, size, style)

    	self.PostCreate(pre)


	tID = wx.NewId()


    	sizer = wx.BoxSizer(wx.VERTICAL)
	
	#### --- Форма ввода данных ---
	#### --- Метки ------
	label0 = wx.StaticText(self, -1, "Действует с")
	label1 = wx.StaticText(self, -1, "Цена")
	

	#### --- Поля ввода ---
	self.field_0 = wx.DatePickerCtrl(self, -1, size=(150,-1),style=wx.DP_DROPDOWN|wx.DP_SHOWCENTURY)
	self.field_1 = wx.TextCtrl(self, -1, "0.00", size=(100,-1))


	## -- Кнопка сохранения значения полей --
	self.btn = wx.Button(self, wx.ID_OK)
	self.btn2 = wx.Button(self, wx.ID_CANCEL)
	

	#### --- Размещение
	fgsizer = wx.FlexGridSizer( rows = 10, cols = 2, hgap = 10, vgap = 10 )
	fgsizer.Add(label0,0,0)
	fgsizer.Add(self.field_0,0,0)
	fgsizer.Add(label1,0,0)
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
	















