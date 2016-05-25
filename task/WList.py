#coding:utf-8



import  wx
import	sys
from	RunSQL		import	GetListWorker2
from	RunSQL		import	GetListWorker





#### --- Элемент со списком исполнителей  ----
class ListTaskWorker(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0), size=(400,100), style=0):
	wx.ListCtrl.__init__(self, parent, ID, pos, size, style)

	self.InsertColumn(0,"Фамилия")
	self.InsertColumn(1,"Имя")
	self.InsertColumn(2,"Отчество")

	self.SetColumnWidth(0, 200)
	self.SetColumnWidth(1, 100)
	self.SetColumnWidth(2, 100)


    #### --- Отображение списка ---
    def Populate(self, task_id):
	self.DeleteAllItems()

	#### --- Массив идентификаторов строк ---
	self.kod_record = []
	
	### --- Получение списка ---
	for row in  GetListWorker2(task_id):
	    index = self.InsertStringItem(sys.maxint, row[0])
	    self.SetStringItem(index, 0, row[2])
	    self.SetStringItem(index, 1, row[3])
	    self.SetStringItem(index, 2, row[4])
	    
	    #### --- Заполнение массива идентификаторов строк ---
	    self.kod_record.append(row[0])
	    
	#### --- текущая первая строка ---    
	self.currentItem=0
	

    #### --- Присвоение значения по выбранной строке  ---
    def ReadItem(self,event):
	self.currentItem = event.m_itemIndex








### --- Выбор исполнителя из общего списка ---
class ChWorker(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, 
            style=wx.DEFAULT_DIALOG_STYLE
            ):


        pre = wx.PreDialog()
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)
	
	tID = wx.NewId()

        sizer = wx.BoxSizer(wx.VERTICAL)
        box = wx.BoxSizer(wx.HORIZONTAL)
        self.ctrl0 = ListW(pre, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl0.Populate()
	self.ctrl0.SetItemState(0,wx.LIST_STATE_SELECTED,wx.LIST_STATE_SELECTED)
        box.Add(self.ctrl0, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER|wx.TOP, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)

        btn = wx.Button(self, wx.ID_OK)        
        btn2 = wx.Button(self, wx.ID_CANCEL)


        btn2.SetDefault()
        box.Add(btn, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL|wx.TOP, 5)
        box.Add(btn2, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL|wx.TOP, 5)
        sizer.Add(box, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)


	self.Bind(wx.EVT_BUTTON, self.Cancel, btn2)
	self.ctrl0.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem, self.ctrl0)




#### --- Закрытие формы ---
    def	Cancel(self,event):
	self.Destroy()



#### --- Присвоение значения по выбранной строке ---
    def ReadItem(self,event):
	self.ctrl0.currentItem = event.m_itemIndex








class ListW(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0),size=(400,300), style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)


        self.InsertColumn(0, "Фамилия")
        self.InsertColumn(1, "Имя")
        self.InsertColumn(2, "Отчество")

    	self.SetColumnWidth(0, 200)
    	self.SetColumnWidth(1, 100)
    	self.SetColumnWidth(2, 100)



    def Populate(self):

	self.DeleteAllItems()


#### --- Отображение данных в форме ---
	self.kod_record=[] # массив идентификаторов записей
	for row in GetListWorker():
	    index=self.InsertStringItem(sys.maxint, row[0])
	    self.SetStringItem( index, 0, row[1])
	    self.SetStringItem( index, 1, row[2])
	    self.SetStringItem( index, 2, row[3])

	    self.kod_record.append(row[0])    
	    
	self.currentItem=0








