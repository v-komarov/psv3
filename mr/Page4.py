#coding:utf-8

""" Закладка 4 - отображения списка ввода остатков 
    вынесено в этот файл (что удалось), чтобы не загромождать MainForm.py
"""


import  wx
import	sys
from	RunSQLPage4	import	GetListMateSetStore
from	tools.Messages	import	NotAccess
from	tools.Messages	import	ErrorData
from	tools.Messages	import	SaveDone



#### --- закладка 4 : Список ввода остатков , функция вызывается из MainForm.py ---
def Page4(self):
    page4 = self.Page()
    pagesizer = wx.BoxSizer(wx.VERTICAL)
    tID = wx.NewId()
    self.ctrl4 = ListMateIn(page4, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
    self.ctrl4.Populate(self.rec_kod)
    self.ctrl4.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
    pagesizer.Add(self.ctrl4, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    ### --- Кнопки ---
    sizer = wx.BoxSizer(wx.HORIZONTAL)
    self.button4Add = wx.Button(page4, 401, "Остаток")
#    self.button4Del = wx.Button(page4, 402, "Удалить")
    sizer.Add(self.button4Add, 0, wx.ALIGN_CENTER|wx.ALL, 5)
#    sizer.Add(self.button4Del, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    pagesizer.Add(sizer, 0, wx.ALIGN_CENTER, 5)
    page4.SetSizer(pagesizer)
    pagesizer.Fit(self)


    self.Bind(wx.EVT_BUTTON, self.Add4, self.button4Add)
#    self.Bind(wx.EVT_BUTTON, self.Del1, self.button1Del)
    self.ctrl4.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ctrl4.ReadItem, self.ctrl4)



    return page4








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
	for row in  GetListMateSetStore(kod):
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










