#coding:utf-8
import	sys
import  wx
from	abonent.RunSQL	import	ShowLSStatus
from	abonent.RunSQL	import	ShowLSStatus2



class List(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0),
                 size=(580,150), style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)


        self.InsertColumn(0, "Статус")
	self.InsertColumn(1, "Услуга")
	self.InsertColumn(2, "Сумма")

    	self.SetColumnWidth(0, 150)
    	self.SetColumnWidth(1, 350)
    	self.SetColumnWidth(2, 100)



#        self.Populate()




    def Populate(self,db,kod_ab):

	self.DeleteAllItems()

#### --- Получение данных по удержаниям абонента ---	
#	db=DBTools.DBTools()

#### --- Отображение данных в форме ---
	self.ps_rec_id=[] # массив идентификаторов записей
	for row in ShowLSStatus(db,kod_ab):
	    str0=row[0]
	    str1=ShowLSStatus2(db,kod_ab,row[3])[0]	    
	    str2=row[2]
	    str3=row[4]
	    index=self.InsertStringItem(sys.maxint, str0)
	    self.SetStringItem( index, 0, str1)
	    self.SetStringItem( index, 1, str2)
	    self.SetStringItem( index, 2, str3)
	# -- Заполнение массива идентификаторов записей ---
	    self.ps_rec_id.append(str0)
    
	    
	
	self.currentItem=0
