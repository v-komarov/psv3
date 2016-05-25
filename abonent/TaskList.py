#coding:utf-8
import	sys
import  wx
from	abonent.RunSQL	import	GetListTask



class List(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0),
                 size=(580,200), style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)


        self.InsertColumn(0, "Дата")
	self.InsertColumn(1, "Время")
	self.InsertColumn(2, "Статус")
	self.InsertColumn(3, "Заявка")
	self.InsertColumn(4, "Тип")
	self.InsertColumn(5, "Примечание")

    	self.SetColumnWidth(0, 100)
    	self.SetColumnWidth(1, 80)
    	self.SetColumnWidth(2, 100)
    	self.SetColumnWidth(3, 200)
    	self.SetColumnWidth(4, 100)
    	self.SetColumnWidth(5, 300)



#        self.Populate()




    def Populate(self,db,kod_ab):

	self.DeleteAllItems()

	self.kod_record = [] # массив идентификаторов записей

#### --- Отображение данных в форме ---
	for row in GetListTask(db,kod_ab):
	    index=self.InsertStringItem(sys.maxint, row[1])
	    self.SetStringItem( index, 0, row[3])
	    self.SetStringItem( index, 1, row[4])
	    self.SetStringItem( index, 2, row[5])
	    self.SetStringItem( index, 3, row[7])
	    if row[6]==1:
		self.SetStringItem( index, 4, 'РЕМОНТ')
	    elif row[6]==2:
		self.SetStringItem( index, 4, 'МОНТАЖ')
	    elif row[6]==0:
		self.SetStringItem( index, 4, 'НЕТ')
	    self.SetStringItem( index, 5, row[13])
	    
	# -- Заполнение массива идентификаторов записей ---
	    self.kod_record.append(row[0])
    
	    
	
	self.currentItem=0









