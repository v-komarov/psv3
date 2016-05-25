#coding:utf-8

""" Закладка 2 - Расход материала 
    вынесено в этот файл (что удалось), чтобы не загромождать MainForm.py
"""


import  wx
import	sys

from	RunSQLPage2	import	GetListMateTask


#### --- закладка 2 : Список расхода материала , функция вызывается из MainForm.py ---
def Page2(self):
    page2 = self.Page()
    pagesizer = wx.BoxSizer(wx.VERTICAL)
    tID = wx.NewId()
    self.ctrl2 = ListMateOut(page2, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
    self.ctrl2.Populate(self.rec_kod)
    self.ctrl2.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
    pagesizer.Add(self.ctrl2, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    ### --- Кнопки ---
#    sizer = wx.BoxSizer(wx.HORIZONTAL)
#    self.button2Add = wx.Button(page2, 1010, "Добавить")
#    self.button2Del = wx.Button(page2, 1011, "Удалить")
#    sizer.Add(self.button2Add, 0, wx.ALIGN_CENTER|wx.ALL, 5)
#    sizer.Add(self.button2Del, 0, wx.ALIGN_CENTER|wx.ALL, 5)
#    pagesizer.Add(sizer, 0, wx.ALIGN_CENTER, 5)
    page2.SetSizer(pagesizer)
    pagesizer.Fit(self)


#    self.Bind(wx.EVT_BUTTON, self.Add2, self.button2Add)
#    self.Bind(wx.EVT_BUTTON, self.Del2, self.button2Del)
#    self.ctrl2.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ctrl2.ReadItem, self.ctrl2)



    return page2





#### --- Элемент со списком расхода материалов  ----
class ListMateOut(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0), size=(500,200), style=0):
	wx.ListCtrl.__init__(self, parent, ID, pos, size, style)

	self.InsertColumn(0,"Дата")
	self.InsertColumn(1,"Заявка")
	self.InsertColumn(2,"Ед.из.")
	self.InsertColumn(3,"Количество")
	self.InsertColumn(4,"Цена")
	self.InsertColumn(5,"Сумма")
	self.InsertColumn(6,"Улица")
	self.InsertColumn(7,"Дом")
	self.InsertColumn(8,"Подъезд")
	self.InsertColumn(9,"Квартира")

	self.SetColumnWidth(0, 100)
	self.SetColumnWidth(1, 150)
	self.SetColumnWidth(2, 70)
	self.SetColumnWidth(3, 100)
	self.SetColumnWidth(4, 100)
	self.SetColumnWidth(5, 100)
	self.SetColumnWidth(6, 200)
	self.SetColumnWidth(7, 100)
	self.SetColumnWidth(8, 100)
	self.SetColumnWidth(9, 100)


    #### --- Отображение списка ---
    def Populate(self, kod):
	self.DeleteAllItems()

	#### --- Массив идентификаторов строк ---
	self.kod_record = []
	
	### --- Получение списка ---
	for row in  GetListMateTask(kod):
	    index = self.InsertStringItem(sys.maxint, str(row[0]))
	    self.SetStringItem(index, 0, row[1])
	    self.SetStringItem(index, 1, row[2])
	    self.SetStringItem(index, 2, row[3])
	    self.SetStringItem(index, 3, row[4])
	    self.SetStringItem(index, 4, row[5])
	    self.SetStringItem(index, 5, row[6])
	    self.SetStringItem(index, 6, row[7])
	    self.SetStringItem(index, 7, row[8])
	    self.SetStringItem(index, 8, row[9])
	    self.SetStringItem(index, 9, row[10])
	    
	    #### --- Заполнение массива идентификаторов строк ---
	    self.kod_record.append(str(row[0]))
	    
	#### --- текущая первая строка ---    
	self.currentItem=0
	

    #### --- Присвоение значения по выбранной строке  ---
    def ReadItem(self,event):
	self.currentItem = event.m_itemIndex




















