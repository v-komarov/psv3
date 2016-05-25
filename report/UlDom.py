#coding:utf-8

""" Вспомогательные интерфейсы для отчетных форм """


import	RWCfg
import	wx
import	sys
from	report.RunSQL	import	GetUlDom




class ListUlDom(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0),
                 size=(270,200), style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)


        self.InsertColumn(0, "Улица")
	self.InsertColumn(1, "Дом")

    	self.SetColumnWidth(0, 200)
    	self.SetColumnWidth(1, 70)







    def Populate(self):

	self.DeleteAllItems()


#### --- Отображение данных в форме ---
	self.kod_record=[] # массив идентификаторов записей
	for row in GetUlDom():
	    str0=row[0]
	    str1=row[1]
	    index=self.InsertStringItem(sys.maxint, str0)
	    self.SetStringItem( index, 0, str0)
	    self.SetStringItem( index, 1, str1)
	# -- Заполнение массива идентификаторов записей ---
	    self.kod_record.append(row[0]+":"+row[1])    
	    
	self.currentItem=0








class ListUlDom2(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0),
                 size=(270,200), style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)


        self.InsertColumn(0, "Улица")
	self.InsertColumn(1, "Дом")

    	self.SetColumnWidth(0, 300)
    	self.SetColumnWidth(1, 100)







    def Populate(self):

	self.DeleteAllItems()


#### --- Отображение данных в форме ---
	self.kod_record=[] # массив идентификаторов записей
	for row in GetUlDom():
	    str0=row[0]
	    str1=row[1]
	    index=self.InsertStringItem(sys.maxint, str0)
	    self.SetStringItem( index, 0, str0)
	    self.SetStringItem( index, 1, str1)
	# -- Заполнение массива идентификаторов записей ---
	    self.kod_record.append(row[0]+":"+row[1])    
	    
	self.currentItem=0







class ListServiceMonthSum(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0),
                 size=(400,150), style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)


        self.InsertColumn(0, "Услуга")
	self.InsertColumn(1, "Мес.долг")
	self.InsertColumn(2, "Сум.долг")

    	self.SetColumnWidth(0, 200)
    	self.SetColumnWidth(1, 100)
    	self.SetColumnWidth(2, 100)







    def Populate(self,item):

	self.DeleteAllItems()


#### --- Отображение данных в форме ---
	self.kod_record=[] # массив идентификаторов записей

	if len(item)!=0:

	    for row in item:
		index=self.InsertStringItem(sys.maxint, row[0])
		self.SetStringItem( index, 0, row[0])
		self.SetStringItem( index, 1, row[1])
		self.SetStringItem( index, 2, row[2])
	    # -- Заполнение массива идентификаторов записей ---
		self.kod_record.append(row[0])    
	    
	    self.currentItem=0


