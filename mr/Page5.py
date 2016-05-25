#coding:utf-8

""" Закладка 5 - отображения наличия на складах 
    вынесено в этот файл (что удалось), чтобы не загромождать MainForm.py
"""


import  wx
import	sys
from	RunSQLPage5	import	GetListStoreQ
from	tools.Messages	import	NotAccess
from	tools.Messages	import	ErrorData
from	tools.Messages	import	SaveDone



#### --- закладка 5 : Список наличия на складах , функция вызывается из MainForm.py ---
def Page5(self):
    page5 = self.Page()
    pagesizer = wx.BoxSizer(wx.VERTICAL)
    tID = wx.NewId()
    self.ctrl5 = ListStoreQ(page5, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
    self.ctrl5.Populate(self.rec_kod)
    self.ctrl5.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
    pagesizer.Add(self.ctrl5, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    ### --- Кнопки ---
#    sizer = wx.BoxSizer(wx.HORIZONTAL)
#    self.button5Add = wx.Button(page5, 501, "Добавить")
#    self.button5Del = wx.Button(page5, 502, "Удалить")
#    sizer.Add(self.button5Add, 0, wx.ALIGN_CENTER|wx.ALL, 5)
#    sizer.Add(self.button5Del, 0, wx.ALIGN_CENTER|wx.ALL, 5)
#    pagesizer.Add(sizer, 0, wx.ALIGN_CENTER, 5)
    page5.SetSizer(pagesizer)
    pagesizer.Fit(self)


#    self.Bind(wx.EVT_BUTTON, self.Add5, self.button5Add)
#    self.Bind(wx.EVT_BUTTON, self.Del1, self.button1Del)
#    self.ctrl1.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ctrl1.ReadItem, self.ctrl1)



    return page5








#### --- Элемент со списком наличия на складах  ----
class ListStoreQ(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0), size=(500,200), style=0):
	wx.ListCtrl.__init__(self, parent, ID, pos, size, style)

	self.InsertColumn(0,"Склад")
	self.InsertColumn(1,"Ед.из.")
	self.InsertColumn(2,"Количество")

	self.SetColumnWidth(0, 300)
	self.SetColumnWidth(1, 100)
	self.SetColumnWidth(2, 100)


    #### --- Отображение списка ---
    def Populate(self, kod):
	self.DeleteAllItems()

	#### --- Массив идентификаторов строк ---
	self.kod_record = []
	
	### --- Получение списка ---
	for row in  GetListStoreQ(kod):
	    index = self.InsertStringItem(sys.maxint, row[0]+'#'+str(row[2]))
	    self.SetStringItem(index, 0, row[0])
	    self.SetStringItem(index, 1, row[1])
	    self.SetStringItem(index, 2, row[2])
	    
	    #### --- Заполнение массива идентификаторов строк ---
	    self.kod_record.append(row[0])
	    
	#### --- текущая первая строка ---    
	self.currentItem=0
	

    #### --- Присвоение значения по выбранной строке  ---
    def ReadItem(self,event):
	self.currentItem = event.m_itemIndex












