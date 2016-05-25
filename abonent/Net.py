#coding:utf-8
import	sys
import  wx
from	abonent.RunSQL	import	GetListMac



class List(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0),
                 size=(580,150), style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)


        self.InsertColumn(0, "Тип")
	self.InsertColumn(1, "MAC address")

    	self.SetColumnWidth(0, 150)
    	self.SetColumnWidth(1, 430)



#        self.Populate()




    def Populate(self,db,kod_ab):

	self.DeleteAllItems()

	self.kod_record = [] # массив идентификаторов записей

#### --- Отображение данных в форме ---
	for row in GetListMac(db,kod_ab):
	    index=self.InsertStringItem(sys.maxint, row[0])
	    if row[2]==1:
		self.SetStringItem( index, 0, 'INTERNET')
	    elif row[2]==2:
		self.SetStringItem( index, 0, 'IPTV')
	    
	    self.SetStringItem( index, 1, row[3])
	# -- Заполнение массива идентификаторов записей ---
	    self.kod_record.append(row[0])
    
	    
	
	self.currentItem=0








#*************************************************************************
# Форма для ввода нового MAC
#*************************************************************************



#### --- Новый MAC ----
class AddMAC(wx.Dialog):
    def __init__(self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE):

    	pre = wx.PreDialog()
    	pre.Create(parent, ID, title, pos, size, style)

    	self.PostCreate(pre)

	tID = wx.NewId()


    	sizer = wx.BoxSizer(wx.VERTICAL)
	
	#### --- Форма ввода данных ---
	#### --- Метки ------
	self.label0 = wx.StaticText(self, -1, "Тип")
	self.label1 = wx.StaticText(self, -1, "MAC")
	

	#### --- Поля ввода ---
	self.field_0 = wx.ComboBox(self, -1, "", size=(300,-1),choices=["INTERNET","IPTV"], style=wx.CB_DROPDOWN|wx.CB_READONLY)
	self.field_1 = wx.TextCtrl(self, -1, "#:::::", size=(300,-1))


	## -- Кнопка сохранения значения полей --
	self.btn = wx.Button(self, wx.ID_OK)
	self.btn2 = wx.Button(self, wx.ID_CANCEL)
	

	#### --- Размещение
	fgsizer = wx.FlexGridSizer( rows = 2, cols = 2, hgap = 10, vgap = 10 )
	fgsizer.Add(self.label0,0,0)
	fgsizer.Add(self.field_0,0,0)
	fgsizer.Add(self.label1,0,0)
	fgsizer.Add(self.field_1,0,0)
    	sizer.Add(fgsizer, 0, wx.GROW|wx.ALIGN_CENTER|wx.ALL, 5)

   	line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
    	sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER|wx.TOP, 5)
	
	box = wx.BoxSizer(wx.HORIZONTAL)
    	box.Add(self.btn, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    	box.Add(self.btn2, 0, wx.ALIGN_CENTER|wx.ALL, 5)
    	sizer.Add(box, 0, wx.ALIGN_CENTER|wx.ALL, 5)





    	self.SetSizer(sizer)
    	sizer.Fit(self)
	



