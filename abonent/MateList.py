#coding:utf-8
import	sys
import  wx
from	abonent.RunSQL	import	GetListMate



class List(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0),
                 size=(580,200), style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)


        self.InsertColumn(0, "Дата")
	self.InsertColumn(1, "Наименование")
	self.InsertColumn(2, "Ед.из.")
	self.InsertColumn(3, "Кол-во")
	self.InsertColumn(4, "Цена")
	self.InsertColumn(5, "Сумма")

    	self.SetColumnWidth(0, 100)
    	self.SetColumnWidth(1, 200)
    	self.SetColumnWidth(2, 70)
    	self.SetColumnWidth(3, 70)
    	self.SetColumnWidth(4, 100)
    	self.SetColumnWidth(5, 100)



#        self.Populate()




    def Populate(self,db,kod_ab):

	self.DeleteAllItems()

	self.kod_record = [] # массив идентификаторов записей

#### --- Отображение данных в форме ---
	for row in GetListMate(db,kod_ab):
	    index=self.InsertStringItem(sys.maxint, row[1])
	    self.SetStringItem( index, 0, row[1])
	    self.SetStringItem( index, 1, row[2])
	    self.SetStringItem( index, 2, row[3])
	    self.SetStringItem( index, 3, row[4])
	    self.SetStringItem( index, 4, row[5])
	    self.SetStringItem( index, 5, row[6])
	    
	# -- Заполнение массива идентификаторов записей ---
	    self.kod_record.append(row[0])
    
	    
	
	self.currentItem=0









