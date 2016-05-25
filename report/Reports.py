#coding:utf-8

import	wx
import	DBTools
import  wx.grid
import	wx.lib.printout as printout
from	report.UlDom	import	ListUlDom
from	report.UlDom	import	ListUlDom2
from	report.UlDom	import	ListServiceMonthSum
from	report.RunSQL	import	ShowAbonentAll
from	report.RunSQL	import	ShowAbonentPart
from	report.RunSQL	import	GetTarifServiceData2
from	report.RunSQL	import	GetListAllTask
from	report.RunSQL	import	GetListNoCloseTask
from	report.RunSQL	import	GetListService



#### --- Выбор улицы и номера дома ----
class ChoiseUlDom(wx.Dialog):
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
        self.ctrl1 = ListUlDom(pre, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl1.Populate()
	self.ctrl1.SetItemState(0,wx.LIST_STATE_SELECTED,wx.LIST_STATE_SELECTED)
        box.Add(self.ctrl1, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)
        btn = wx.Button(self, wx.ID_OK)        
        btn.SetDefault()
        box.Add(btn, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL|wx.TOP, 5)

        btn2 = wx.Button(self, wx.ID_CANCEL)
        box.Add(btn2, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL|wx.TOP, 5)
        sizer.Add(box, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)


	self.ctrl1.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem, self.ctrl1)



#### --- Присвоение значения по выбранной строке ---
    def ReadItem(self,event):
	self.ctrl1.currentItem = event.m_itemIndex





#### --- Выбор улицы, номера дома, услуги ----
class ChoiseUlDomSer(wx.Dialog):
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
        self.ctrl1 = ListUlDom2(pre, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl1.Populate()
	self.ctrl1.SetItemState(0,wx.LIST_STATE_SELECTED,wx.LIST_STATE_SELECTED)
        box.Add(self.ctrl1, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)


        box = wx.BoxSizer(wx.HORIZONTAL)
	self.label_0 = wx.StaticText(self, -1, "Услуга : ")
	self.field_0 = wx.ComboBox(self, -1, size=(200,-1), choices=GetListService(), style=wx.CB_DROPDOWN|wx.CB_READONLY)
        box.Add(self.label_0, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(self.field_0, 1, wx.ALIGN_CENTRE|wx.ALL, 5)	
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)
        btn = wx.Button(self, wx.ID_OK)        
        btn.SetDefault()
        box.Add(btn, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL|wx.TOP, 5)

        btn2 = wx.Button(self, wx.ID_CANCEL)
        box.Add(btn2, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL|wx.TOP, 5)
        sizer.Add(box, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)


	self.ctrl1.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem, self.ctrl1)






#### --- Присвоение значения по выбранной строке ---
    def ReadItem(self,event):
	self.ctrl1.currentItem = event.m_itemIndex
	









#### --- Выбор улицы, номера дома, услуги, количества месяцев задолженности, минимальной суммы долга  ----
class ChoiseUlDomSer2(wx.Dialog):
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
        self.ctrl1 = ListUlDom2(pre, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl1.Populate()
	self.ctrl1.SetItemState(0,wx.LIST_STATE_SELECTED,wx.LIST_STATE_SELECTED)
        box.Add(self.ctrl1, 1, wx.ALIGN_CENTRE|wx.ALL|wx.GROW, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)






	label_0 = wx.StaticText(self, -1, "Услуга")
	label_1 = wx.StaticText(self, -1, "Месяцев долг")
	label_2 = wx.StaticText(self, -1, "Мин. сумма долга")

	self.field_0 = wx.ComboBox(self, -1, size=(200,-1), choices=GetListService(), style=wx.CB_DROPDOWN|wx.CB_READONLY)
	self.field_1 = wx.TextCtrl(self, -1, u"3", size = (70,-1))
	self.field_2 = wx.TextCtrl(self, -1, u"100.0", size = (70,-1))

	fgsizer = wx.FlexGridSizer(rows=3, cols=2, hgap=100, vgap=10)
	fgsizer.Add(label_0)
	fgsizer.Add(self.field_0)
	fgsizer.Add(label_1)
	fgsizer.Add(self.field_1)
	fgsizer.Add(label_2)
	fgsizer.Add(self.field_2)

        sizer.Add(fgsizer, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)
        btn = wx.Button(self, wx.ID_OK)        
        btn.SetDefault()
        box.Add(btn, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL|wx.TOP, 5)

        btn2 = wx.Button(self, wx.ID_CANCEL)
        box.Add(btn2, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL|wx.TOP, 5)
        sizer.Add(box, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)


	self.ctrl1.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem, self.ctrl1)






#### --- Присвоение значения по выбранной строке ---
    def ReadItem(self,event):
	self.ctrl1.currentItem = event.m_itemIndex
	






#### --- Выбор улицы, номера дома, услуги, количества месяцев задолженности, минимальной суммы долга  ----
class ChoiseUlDomSer3(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, 
            style=wx.DEFAULT_DIALOG_STYLE
            ):


	### --- Список услуг, месяцев, суммы ---
	self.item = []


        pre = wx.PreDialog()
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)
	
	tID = wx.NewId()

        sizer = wx.BoxSizer(wx.VERTICAL)
        box = wx.BoxSizer(wx.HORIZONTAL)
        self.ctrl1 = ListUlDom2(pre, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl1.Populate()
	self.ctrl1.SetItemState(0,wx.LIST_STATE_SELECTED,wx.LIST_STATE_SELECTED)
        box.Add(self.ctrl1, 1, wx.ALIGN_CENTRE|wx.ALL|wx.GROW, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)


        box = wx.BoxSizer(wx.HORIZONTAL)
        self.ctrl2 = ListServiceMonthSum(pre, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
        box.Add(self.ctrl2, 1, wx.ALIGN_CENTRE|wx.ALL|wx.GROW, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)



        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)
        btn = wx.Button(self, wx.ID_OK)        
        btn.SetDefault()
        box.Add(btn, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL|wx.TOP, 5)

        btn1 = wx.Button(self, -1, "Выбор")        
        box.Add(btn1, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL|wx.TOP, 5)

        btn2 = wx.Button(self, wx.ID_CANCEL)
        box.Add(btn2, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL|wx.TOP, 5)
        sizer.Add(box, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)


	self.ctrl1.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem, self.ctrl1)
	self.Bind(wx.EVT_BUTTON, self.ItemAdd, btn1)



#### --- Присвоение значения по выбранной строке ---
    def ReadItem(self,event):
	self.ctrl1.currentItem = event.m_itemIndex

	
    #### --- Добавление услуги в список ---
    def	ItemAdd(self,event):
	dlg = ChoiceSerMonthSum(self, -1, "Выбор услуги", size=(350,200), style=wx.DEFAULT_DIALOG_STYLE)
	if dlg.ShowModal() == wx.ID_OK:
	    ser = dlg.field_0.GetValue()
	    month = dlg.field_1.GetValue()
	    sum = dlg.field_2.GetValue()

	    list = []
	    list.append(ser)
	    list.append(month)
	    list.append(sum)


	    l = []
	    for a in self.item:
		l.append(a[0])

	    if l.count(ser) == 0 and ser != '' and month != '' and sum != ''  :
		self.item.append(list)
		
		
	    self.ctrl2.Populate(self.item)

	dlg.Destroy()






#### --- Выбор услуги, числа месяцев задолженности, минимальной суммы долга  ----
class ChoiceSerMonthSum(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, 
            style=wx.DEFAULT_DIALOG_STYLE
            ):


        pre = wx.PreDialog()
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)
	
	tID = wx.NewId()

        sizer = wx.BoxSizer(wx.VERTICAL)


	label_0 = wx.StaticText(self, -1, "Услуга")
	label_1 = wx.StaticText(self, -1, "Месяцев долг")
	label_2 = wx.StaticText(self, -1, "Мин. сумма долга")

	self.field_0 = wx.ComboBox(self, -1, size=(200,-1), choices=GetListService(), style=wx.CB_DROPDOWN|wx.CB_READONLY)
	self.field_1 = wx.TextCtrl(self, -1, u"3", size = (70,-1))
	self.field_2 = wx.TextCtrl(self, -1, u"100.0", size = (70,-1))

	fgsizer = wx.FlexGridSizer(rows=3, cols=2, hgap=100, vgap=10)
	fgsizer.Add(label_0)
	fgsizer.Add(self.field_0)
	fgsizer.Add(label_1)
	fgsizer.Add(self.field_1)
	fgsizer.Add(label_2)
	fgsizer.Add(self.field_2)

        sizer.Add(fgsizer, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)
        btn = wx.Button(self, wx.ID_OK)        
        btn.SetDefault()
        box.Add(btn, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL|wx.TOP, 5)

        btn2 = wx.Button(self, wx.ID_CANCEL)
        box.Add(btn2, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL|wx.TOP, 5)
        sizer.Add(box, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)









	

#### --- Вывод списка всех абонентов ---
class AbonentShowAll(wx.grid.Grid):
    def __init__(self, parent, UlDom):
        wx.grid.Grid.__init__(self, parent, -1)
        self.moveTo = None
	
	maxrow = 1000
	
        self.CreateGrid(maxrow, 6, selmode=wx.grid.Grid.SelectRows)
        self.EnableEditing(False)

	attr = wx.grid.GridCellAttr()
	attr.SetBackgroundColour("YELLOW")

	attr2 = wx.grid.GridCellAttr()
	attr2.SetBackgroundColour("RED")

	
	for row in range(maxrow):
	    self.SetRowLabelValue(row, str(row))


        # simple cell formatting
        self.SetColSize(0, 150)
        self.SetColSize(1, 70)
        self.SetColSize(2, 70)
        self.SetColSize(3, 100)
        self.SetColSize(4, 200)
        self.SetColSize(5, 100)


	n = 0
	for row in ShowAbonentAll(UlDom):
	    self.SetCellValue(n, 0, row[1])
	    self.SetCellValue(n, 1, row[2])
	    self.SetCellValue(n, 2, row[3])
	    self.SetCellValue(n, 3, row[4])
	    self.SetCellValue(n, 4, row[7])
	    self.SetCellValue(n, 5, row[10])

	    if eval(row[4])<0 and eval(row[4])>=(-1000):
		self.SetRowAttr(n, attr)
	    elif eval(row[4])<(-1000):
		self.SetRowAttr(n, attr2)
		
	    n = n+1



        self.SetColLabelValue(0, "Улица")
        self.SetColLabelValue(1, "Дом")
        self.SetColLabelValue(2, "Квартира")
        self.SetColLabelValue(3, "Общий баланс")
        self.SetColLabelValue(4, "Тарифный план")
        self.SetColLabelValue(5, "Подъезд")


        self.SetColLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_BOTTOM)


	








#### --- Вывод списка должников (новый) ---
class AbonentShowPart(wx.grid.Grid): 
    def __init__(self, parent, UlDom):
        wx.grid.Grid.__init__(self, parent, -1)
        self.moveTo = None
	
	maxrow = 3000
	
        self.CreateGrid(maxrow, 8, selmode=wx.grid.Grid.SelectRows)
        self.EnableEditing(False)

	attr = wx.grid.GridCellAttr()
	attr.SetBackgroundColour("YELLOW")

	attr2 = wx.grid.GridCellAttr()
	attr2.SetBackgroundColour("RED")

	
	for row in range(maxrow):
	    self.SetRowLabelValue(row, str(row))


        # simple cell formatting
        self.SetColSize(0, 150)
        self.SetColSize(1, 70)
        self.SetColSize(2, 70)
        self.SetColSize(3, 200)
        self.SetColSize(4, 150)
        self.SetColSize(5, 70)
        self.SetColSize(6, 70)
        self.SetColSize(7, 100)


	n = 0
	for row in ShowAbonentPart(UlDom):
	    self.SetCellValue(n, 0, row[1])
	    self.SetCellValue(n, 1, row[2])
	    self.SetCellValue(n, 2, row[3])
	    self.SetCellValue(n, 3, row[6])
	    self.SetCellValue(n, 4, row[7])
	    self.SetCellValue(n, 5, row[9])
	    self.SetCellValue(n, 6, row[12])
	    self.SetCellValue(n, 7, row[15])

	    if row[13]>=6:
		self.SetRowAttr(n, attr2)
	    elif row[13]>=3 and row[13]<6:
		self.SetRowAttr(n, attr)
		
	    n = n+1



        self.SetColLabelValue(0, "Улица")
        self.SetColLabelValue(1, "Дом")
        self.SetColLabelValue(2, "Квартира")
        self.SetColLabelValue(3, "Тарифный план")
        self.SetColLabelValue(4, "Услуга")
        self.SetColLabelValue(5, "Стоимость")
        self.SetColLabelValue(6, "Долг")
        self.SetColLabelValue(7, "Подъезд")


        self.SetColLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_BOTTOM)






#### --- Список тарифных планов  ---
class TarifPlanList(wx.grid.Grid): 
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1)
        self.moveTo = None


	maxrow = 300
	
        self.CreateGrid(maxrow, 3, selmode=wx.grid.Grid.SelectRows)
        self.EnableEditing(False)

	
	for row in range(300):
	    self.SetRowLabelValue(row, str(row))


        # simple cell formatting
        self.SetColSize(0, 300)
        self.SetColSize(1, 300)
        self.SetColSize(2, 150)


	n = 0
	for row in GetTarifServiceData2():
	    self.SetCellValue(n, 0, row[1])
	    self.SetCellValue(n, 1, row[2])
	    self.SetCellValue(n, 2, str(row[3]))
	    n = n+1


        self.SetColLabelValue(0, "Тарифный план")
        self.SetColLabelValue(1, "Услуга")
        self.SetColLabelValue(2, "Стоимость")


        self.SetColLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_BOTTOM)


	







#### --- Список всех заявок по дому ---- 
class TaskListDom(wx.grid.Grid): 
    def __init__(self, parent, UlDom):
        wx.grid.Grid.__init__(self, parent, -1)
        self.moveTo = None


	maxrow = 3000
	
        self.CreateGrid(maxrow, 9, selmode=wx.grid.Grid.SelectRows)
        self.EnableEditing(False)

	
	for row in range(maxrow):
	    self.SetRowLabelValue(row, str(row))


        # simple cell formatting
        self.SetColSize(0, 80)
        self.SetColSize(1, 50)
        self.SetColSize(2, 100)
        self.SetColSize(3, 100)
        self.SetColSize(4, 300)
        self.SetColSize(5, 200)
        self.SetColSize(6, 100)
        self.SetColSize(7, 100)
        self.SetColSize(8, 100)


	n = 0
	for row in GetListAllTask(UlDom):
	    self.SetCellValue(n, 0, row[2])
	    self.SetCellValue(n, 1, row[3])
	    self.SetCellValue(n, 2, row[7])
	    if row[8] == 0:
		self.SetCellValue(n, 3, 'НЕТ')
	    elif row[8] == 1:
		self.SetCellValue(n, 3, 'РЕМОНТ')
	    elif row[8] == 2:
		self.SetCellValue(n, 3, 'МОНТАЖ')

	    self.SetCellValue(n, 4, row[9])
	    self.SetCellValue(n, 5, row[10])
	    self.SetCellValue(n, 6, row[11])
	    self.SetCellValue(n, 7, row[12])
	    self.SetCellValue(n, 8, row[13])
	    n = n+1


        self.SetColLabelValue(0, "Дата")
        self.SetColLabelValue(1, "Время")
        self.SetColLabelValue(2, "Статус")
        self.SetColLabelValue(3, "Тип")
        self.SetColLabelValue(4, "Заявка")
        self.SetColLabelValue(5, "Улица")
        self.SetColLabelValue(6, "Дом")
        self.SetColLabelValue(7, "Квартира")
        self.SetColLabelValue(8, "Подъезд")


        self.SetColLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_BOTTOM)





#### --- Список незавершенных заявок  ---- 
class TaskListNoClose(wx.grid.Grid): 
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1)
        self.moveTo = None


	maxrow = 5000
	
        self.CreateGrid(maxrow, 9, selmode=wx.grid.Grid.SelectRows)
        self.EnableEditing(False)

	
	for row in range(maxrow):
	    self.SetRowLabelValue(row, str(row))


        # simple cell formatting
        self.SetColSize(0, 80)
        self.SetColSize(1, 50)
        self.SetColSize(2, 100)
        self.SetColSize(3, 100)
        self.SetColSize(4, 300)
        self.SetColSize(5, 200)
        self.SetColSize(6, 100)
        self.SetColSize(7, 100)
        self.SetColSize(8, 100)


	n = 0
	for row in GetListNoCloseTask():
	    self.SetCellValue(n, 0, row[2])
	    self.SetCellValue(n, 1, row[3])
	    self.SetCellValue(n, 2, row[7])
	    if row[8] == 0:
		self.SetCellValue(n, 3, 'НЕТ')
	    elif row[8] == 1:
		self.SetCellValue(n, 3, 'РЕМОНТ')
	    elif row[8] == 2:
		self.SetCellValue(n, 3, 'МОНТАЖ')

	    self.SetCellValue(n, 4, row[9])
	    self.SetCellValue(n, 5, row[10])
	    self.SetCellValue(n, 6, row[11])
	    self.SetCellValue(n, 7, row[12])
	    self.SetCellValue(n, 8, row[13])
	    n = n+1


        self.SetColLabelValue(0, "Дата")
        self.SetColLabelValue(1, "Время")
        self.SetColLabelValue(2, "Статус")
        self.SetColLabelValue(3, "Тип")
        self.SetColLabelValue(4, "Заявка")
        self.SetColLabelValue(5, "Улица")
        self.SetColLabelValue(6, "Дом")
        self.SetColLabelValue(7, "Квартира")
        self.SetColLabelValue(8, "Подъезд")


        self.SetColLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_BOTTOM)

