#coding:utf-8

""" 
    Форма добавления нового материала, поиска - выбора из списка

"""


import  wx
import	sys


from	RunSQLMate	import	GetListGroup
from	RunSQLMate	import	GetListEds
from	RunSQLMate	import	GetMateGroupList




#### --- Добавить новый материал ---
class NewMate(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, 
            style=wx.DEFAULT_DIALOG_STYLE, tp=''
            ):


        pre = wx.PreDialog()
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)



    #### --- Заголовок ---
        sizer = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, -1, "Материал")
	label.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(label, 0, wx.ALIGN_LEFT|wx.ALL, 5)


        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)


    #### --- Текстовые метки ---
        label0 = wx.StaticText(self, -1, "Название")
        label1 = wx.StaticText(self, -1, "Ед. измер.")
        label2 = wx.StaticText(self, -1, "Группа")

#### --- Поля ввода информации ---
    	self.field_0 = wx.TextCtrl(self, -1, "", size=(300,-1))
    	self.field_1 = wx.ComboBox(self, -1, "", size=(200,-1), choices=GetListEds(), style=wx.CB_DROPDOWN|wx.CB_READONLY)
    	self.field_2 = wx.ComboBox(self, -1, "", size=(300,-1), choices=GetListGroup(), style=wx.CB_DROPDOWN|wx.CB_READONLY)
	

#### --- Размещение элементов ---
	fgsizer = wx.FlexGridSizer(rows = 4, cols = 2, hgap = 10, vgap = 10)
	fgsizer.Add(label0,0,0)
	fgsizer.Add(self.field_0,0,0)
	fgsizer.Add(label1,0,0)
	fgsizer.Add(self.field_1,0,0)
	fgsizer.Add(label2,0,0)
	fgsizer.Add(self.field_2,0,0)

        sizer.Add(fgsizer, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)


#### --- Кнопки ---
        box = wx.BoxSizer(wx.HORIZONTAL)
        btn = wx.Button(self, wx.ID_OK)
        box.Add(btn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        btn2 = wx.Button(self, wx.ID_CANCEL)
        box.Add(btn2, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)
	    





#### --- Форма списка для выбора конкретного материала ---
class ShowFindListMate(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, 
            style=wx.DEFAULT_DIALOG_STYLE, mate_list = []):

	### --- Список найденного ---
	self.mate_list = mate_list


        pre = wx.PreDialog()
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)

	tID = wx.NewId()

        sizer = wx.BoxSizer(wx.VERTICAL)
	box = wx.BoxSizer(wx.HORIZONTAL)
	self.ctrl0 = ListFindMate(pre, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl0.Populate(self.mate_list)
	self.ctrl0.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
	box.Add(self.ctrl0, 1, wx.ALIGN_CENTRE|wx.ALL, 5)	
	sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

#### --- Кнопки ---
        box = wx.BoxSizer(wx.HORIZONTAL)
        btn = wx.Button(self, wx.ID_OK)
        box.Add(btn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        btn2 = wx.Button(self, wx.ID_CANCEL)
        box.Add(btn2, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)
	    
	self.ctrl0.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem, self.ctrl0)




#### --- Присвоение значение по выбранной строке ----
    def ReadItem(self,event):
	self.ctrl0.currentItem = event.m_itemIndex

	


#### --- Элемент со списком материалов ----
class ListFindMate(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0), size=(500,250), style=0):
	wx.ListCtrl.__init__(self, parent, ID, pos, size, style)

	self.InsertColumn(0,"Название")
	self.InsertColumn(1,"Ед. изм.")
	self.InsertColumn(2,"Группа")


	self.SetColumnWidth(0, 200)
	self.SetColumnWidth(1, 100)
	self.SetColumnWidth(2, 200)



    #### --- Отображение списка ---
    def Populate(self,mate_list):
	self.DeleteAllItems()

	#### --- Массив идентификаторов строк ---
	self.kod_record = []
	
	### --- Получение списка ---
	for row in mate_list:
	    index = self.InsertStringItem(sys.maxint, row[0])
	    self.SetStringItem(index, 0, row[1])
	    self.SetStringItem(index, 1, row[3])
	    self.SetStringItem(index, 2, row[4])

	    
	    #### --- Заполнение массива идентификаторов строк ---
	    self.kod_record.append(row[0])
	    
	#### --- текущая первая строка ---    
	self.currentItem=0
	











#### --- Форма выбора из списка ----
class ChMate(wx.Dialog):
    def __init__(self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE):

    	pre = wx.PreDialog()
    	pre.Create(parent, ID, title, pos, size, style)

    	self.PostCreate(pre)

	tID = wx.NewId()

    	sizer = wx.BoxSizer(wx.VERTICAL)

	
	#### --- Форма ввода данных ---
	#### --- Метки ------
	self.label0 = wx.StaticText(self, -1, "Группа")	

	#### --- Поля ввода ---
	self.field_0 = wx.ComboBox(self, -1, "", size=(300,-1), choices=GetListGroup(), style=wx.CB_DROPDOWN|wx.CB_READONLY)


	#### --- Размещение
	fgsizer = wx.FlexGridSizer( rows = 1, cols = 2, hgap = 10, vgap = 10 )
	fgsizer.Add(self.label0,0,0)
	fgsizer.Add(self.field_0,0,0)
    	sizer.Add(fgsizer, 0, wx.GROW|wx.ALIGN_CENTER|wx.ALL, 5)



	## -- Кнопка сохранения значения полей --
	self.btn = wx.Button(self, wx.ID_OK)
	self.btn2 = wx.Button(self, wx.ID_CANCEL)


   	line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
    	sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER|wx.TOP, 5)


        box = wx.BoxSizer(wx.HORIZONTAL)
        self.ctrl0 = ListMate(pre, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
        box.Add(self.ctrl0, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)



	#### --- Метки ------
#	self.label1 = wx.StaticText(self, -1, "Количество")
	
	#### --- Поля ввода ---
#	self.field_1 = wx.TextCtrl(self, -1, "1", size=(100,-1))

	#### --- Размещение
#	fgsizer2 = wx.FlexGridSizer( rows = 1, cols = 2, hgap = 10, vgap = 10 )
#	fgsizer2.Add(self.label1,0,0)
#	fgsizer2.Add(self.field_1,0,0)
#    	sizer.Add(fgsizer2, 0, wx.GROW|wx.ALIGN_CENTER|wx.ALL, 5)


   	line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
    	sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER|wx.TOP, 5)

	
	box = wx.BoxSizer(wx.HORIZONTAL)
    	box.Add(self.btn, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    	box.Add(self.btn2, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    	sizer.Add(box, 0, wx.ALIGN_CENTER|wx.ALL, 5)



    	self.SetSizer(sizer)
    	sizer.Fit(self)



	self.ctrl0.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem, self.ctrl0)
	self.Bind(wx.EVT_COMBOBOX, self.ChGroup, self.field_0)



	
#### --- Присвоение значения по выбранной строке ---
    def ReadItem(self,event):
	self.ctrl0.currentItem = event.m_itemIndex




#### ---- Смена группы материала ---
    def	ChGroup(self,event):
	group = self.field_0.GetValue()
	self.ctrl0.Populate(group)
	self.ctrl0.SetItemState(0,wx.LIST_STATE_SELECTED,wx.LIST_STATE_SELECTED)






class ListMate(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0),size=(500,300), style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)


        self.InsertColumn(0, "Название")
        self.InsertColumn(1, "Ед.из.")

    	self.SetColumnWidth(0, 400)
    	self.SetColumnWidth(1, 100)



    def Populate(self,group):

	self.DeleteAllItems()


#### --- Отображение данных в форме ---
	self.kod_record=[] # массив идентификаторов записей
	     
	for row in GetMateGroupList(group):
	    index=self.InsertStringItem(sys.maxint, row[0])
	    self.SetStringItem( index, 0, row[1])
	    self.SetStringItem( index, 1, row[2])
	# -- Заполнение массива идентификаторов записей ---
	    self.kod_record.append(row[0])    
	    
	self.currentItem=0






