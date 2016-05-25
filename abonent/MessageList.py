#coding:utf-8
import	sys
import  wx
from	abonent.RunSQL	import	ListMess



class MList(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0),
                 size=(580,150), style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)


        self.InsertColumn(0, "Дата")
	self.InsertColumn(1, "Заметка")

    	self.SetColumnWidth(0, 100)
    	self.SetColumnWidth(1, 500)



#        self.Populate()




    def Populate(self,db,kod_ab):

	self.DeleteAllItems()


#### --- Отображение данных в форме ---
	self.ps_rec_id=[] # массив идентификаторов записей
	for row in ListMess(db,kod_ab):
	    str0=row[0]
	    str1=row[1]	    
	    str2=row[3]
	    index=self.InsertStringItem(sys.maxint, str0)
	    self.SetStringItem( index, 0, str1)
	    self.SetStringItem( index, 1, str2)
	# -- Заполнение массива идентификаторов записей ---
	    self.ps_rec_id.append(str0)
    
	
	self.currentItem=0
