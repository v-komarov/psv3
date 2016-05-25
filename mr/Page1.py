#coding:utf-8

""" Закладка 1 - отображения списка поступлений 
    вынесено в этот файл (что удалось), чтобы не загромождать MainForm.py
"""


import  wx
import	sys
from	RunSQLPage1	import	GetListStore
from	RunSQLPage1	import	GetListMateIn
from	tools.Messages	import	NotAccess
from	tools.Messages	import	ErrorData
from	tools.Messages	import	SaveDone



#### --- закладка 1 : Список поступлений , функция вызывается из MainForm.py ---
def Page1(self):
    page1 = self.Page()
    pagesizer = wx.BoxSizer(wx.VERTICAL)
    tID = wx.NewId()
    self.ctrl1 = ListMateIn(page1, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
    self.ctrl1.Populate(self.rec_kod)
    self.ctrl1.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
    pagesizer.Add(self.ctrl1, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    ### --- Кнопки ---
    sizer = wx.BoxSizer(wx.HORIZONTAL)
    self.button1Add = wx.Button(page1, 1008, "Добавить")
    self.button1Del = wx.Button(page1, 1009, "Удалить")
    sizer.Add(self.button1Add, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    sizer.Add(self.button1Del, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    pagesizer.Add(sizer, 0, wx.ALIGN_CENTER, 5)
    page1.SetSizer(pagesizer)
    pagesizer.Fit(self)


    self.Bind(wx.EVT_BUTTON, self.Add1, self.button1Add)
    self.Bind(wx.EVT_BUTTON, self.Del1, self.button1Del)
    self.ctrl1.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ctrl1.ReadItem, self.ctrl1)



    return page1








#### --- Элемент со списком поступлений  ----
class ListMateIn(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0), size=(500,200), style=0):
	wx.ListCtrl.__init__(self, parent, ID, pos, size, style)

	self.InsertColumn(0,"Дата")
	self.InsertColumn(1,"Склад")
	self.InsertColumn(2,"Ед.из.")
	self.InsertColumn(3,"Количество")
	self.InsertColumn(4,"Цена")
	self.InsertColumn(5,"Сумма")

	self.SetColumnWidth(0, 100)
	self.SetColumnWidth(1, 200)
	self.SetColumnWidth(2, 100)
	self.SetColumnWidth(3, 100)
	self.SetColumnWidth(4, 100)
	self.SetColumnWidth(5, 100)


    #### --- Отображение списка ---
    def Populate(self, kod):
	self.DeleteAllItems()

	#### --- Массив идентификаторов строк ---
	self.kod_record = []
	
	### --- Получение списка ---
	for row in  GetListMateIn(kod):
	    index = self.InsertStringItem(sys.maxint, row[0])
	    self.SetStringItem(index, 0, row[1])
	    self.SetStringItem(index, 1, row[2])
	    self.SetStringItem(index, 2, row[3])
	    self.SetStringItem(index, 3, row[4])
	    self.SetStringItem(index, 4, row[5])
	    self.SetStringItem(index, 5, row[6])
	    
	    #### --- Заполнение массива идентификаторов строк ---
	    self.kod_record.append(row[0])
	    
	#### --- текущая первая строка ---    
	self.currentItem=0
	

    #### --- Присвоение значения по выбранной строке  ---
    def ReadItem(self,event):
	self.currentItem = event.m_itemIndex






#*************************************************************************
# Форма для ввода нового поступления
#*************************************************************************



#### --- Новое поступление ----
class AddMateIn(wx.Dialog):
    def __init__(self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE, abonent_kod=''):

    	pre = wx.PreDialog()
    	pre.Create(parent, ID, title, pos, size, style)

    	self.PostCreate(pre)

	tID = wx.NewId()

	self.abonent_kod = abonent_kod

    	sizer = wx.BoxSizer(wx.VERTICAL)
	
	#### --- Форма ввода данных ---
	#### --- Метки ------
	self.label0 = wx.StaticText(self, -1, "Склад")
	self.label1 = wx.StaticText(self, -1, "Количество")
	self.label2 = wx.StaticText(self, -1, "Цена")
	

	#### --- Поля ввода ---
	self.field_0 = wx.ComboBox(self, -1, "", size=(200,-1),choices=GetListStore(),style=wx.CB_DROPDOWN|wx.CB_READONLY)
	self.field_1 = wx.TextCtrl(self, -1, "0.00", size=(100,-1))
	self.field_2 = wx.TextCtrl(self, -1, "0.00", size=(100,-1))


	## -- Кнопка сохранения значения полей --
	self.btn = wx.Button(self, wx.ID_OK)
	self.btn2 = wx.Button(self, wx.ID_CANCEL)
	

	#### --- Размещение
	fgsizer = wx.FlexGridSizer( rows = 3, cols = 2, hgap = 10, vgap = 10 )
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
	











