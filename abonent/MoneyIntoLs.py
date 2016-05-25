#coding:utf-8
import	sys
import  wx
from	abonent.RunSQL	import	GetMoneyOther
from	abonent.RunSQL	import	GetMoneyInfoList


class MoneyInto(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0),
                 size=(580,150), style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)


        self.InsertColumn(0, "Дата")
	self.InsertColumn(1, "План")
	self.InsertColumn(2, "Услуга")
    	self.InsertColumn(3, "Сумма")
    	self.InsertColumn(4, "Баланс до...")
    	self.InsertColumn(5, "Баланс после...")
    	self.InsertColumn(6, "Касса")
    	self.InsertColumn(7, "Примечание")

    	self.SetColumnWidth(0, 100)
    	self.SetColumnWidth(1, 70)
        self.SetColumnWidth(2, 70)
        self.SetColumnWidth(3, 70)
        self.SetColumnWidth(4, 70)
        self.SetColumnWidth(5, 70)
        self.SetColumnWidth(6, 150)
        self.SetColumnWidth(7, 200)



#        self.Populate()




    def Populate(self,db,kod_ab):

	self.DeleteAllItems()


#### --- Отображение данных в форме ---
	self.ps_rec_id = [] # массив идентификаторв строк записей 
	for row in GetMoneyInfoList(db,kod_ab):
	    str0=row[0]
	    str1=row[1]	    
	    str2=row[3]
	    str3=row[4]
	    str4=row[5]
	    str5=row[6]
	    str6=row[7]
	    str7=row[8]
	    str8=row[10]
	    
	    index=self.InsertStringItem(sys.maxint, str0)
	    self.SetStringItem( index, 0, str1)
	    self.SetStringItem( index, 1, str2)
	    self.SetStringItem( index, 2, str3)
	    self.SetStringItem( index, 3, str4)
	    self.SetStringItem( index, 4, str5)
	    self.SetStringItem( index, 5, str6)
	    self.SetStringItem( index, 6, str8)
	    self.SetStringItem( index, 7, str7)
	# -- Формирование массива из идентификаторов записей ---
	    self.ps_rec_id.append(str0)
	
	
	
	

	
class OtherInto(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0),
                 size=(580,150), style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)


        self.InsertColumn(0, "Дата")
	self.InsertColumn(1, "Назначение")
    	self.InsertColumn(2, "Сумма")
    	self.InsertColumn(3, "Примечание")

    	self.SetColumnWidth(0, 100)
    	self.SetColumnWidth(1, 300)
        self.SetColumnWidth(2, 70)
        self.SetColumnWidth(3, 200)



#        self.Populate()




    def Populate(self,db,kod_ab):

	self.DeleteAllItems()


#### --- Отображение данных в форме ---
	self.ps_rec_id = [] # массив идентификаторв строк записей 
	for row in GetMoneyOther(db,kod_ab):
	    str0=row[0]
	    str1=row[1]	    
	    str2=row[3]
	    str3=row[4]
	    str4=row[5]

	    index=self.InsertStringItem(sys.maxint, str0)
	    self.SetStringItem( index, 0, str1)
	    self.SetStringItem( index, 1, str2)
	    self.SetStringItem( index, 2, str3)
	    self.SetStringItem( index, 3, str4)
	# -- Формирование массива из идентификаторов записей ---
	    self.ps_rec_id.append(str0)
		    
	
	self.currentItem=0
