#coding:utf-8
import	sys
import  wx
import	DBTools


class ListServ(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0),
                 size=(380,190), style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)


        self.InsertColumn(0, "Услуга")
	self.InsertColumn(1, "Стоимость")
    	self.InsertColumn(2, "Периодичность оказания (удержания)")

    	self.SetColumnWidth(0, 200)
        self.SetColumnWidth(1, 100)
        self.SetColumnWidth(2, 200)



#        self.Populate()




    def Populate(self,tp):

	self.DeleteAllItems()

#### --- Получение данных по услугам тарифного плана ---	
	db=DBTools.DBTools()
	self.ps_rec_id = [] # массив идентификаторв строк записей 
#### --- Отображение данных в форме ---
	for row in db.GetTarifServiceData(tp):
	    str2=row[2]
	    str3=row[3]	    
	    str4=row[4]
	    index=self.InsertStringItem(sys.maxint, str2)
	    self.SetStringItem( index, 0, str2)
	    self.SetStringItem( index, 1, str3)
	    self.SetStringItem( index, 2, str4)
	# -- Формирование массива из идентификаторов записей ---
	    self.ps_rec_id.append(row[0])
    
	    
	db.Destroy()
	
	self.currentItem=0






class WorkerServ(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0),
                 size=(380,190), style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)


        self.InsertColumn(0, "Компетенция/специализация")

    	self.SetColumnWidth(0, 400)

#        self.Populate()


    def Populate(self,wk_kod):

	self.DeleteAllItems()

#### --- Получение данных по специализациям бригад ---	
	db=DBTools.DBTools()
	self.sc_rec_id = [] # массив идентификаторв строк записей 
#### --- Отображение данных в форме ---
	for row in db.GetListServiceWorker(wk_kod):
	    str0=row[0]
	    str1=row[1]	    
	    str2=row[2]
	    index=self.InsertStringItem(sys.maxint, str0)
	    self.SetStringItem( index, 0, str2)
	# -- Формирование массива из идентификаторов записей ---
	    self.sc_rec_id.append(row[0])
    
	    
	db.Destroy()
	
	self.currentItem=0




class Task(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0),
                 size=(450,190), style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)


        self.InsertColumn(0, "Дата")
        self.InsertColumn(1, "Время")
        self.InsertColumn(2, "Статус")
        self.InsertColumn(3, "Заявка")
        self.InsertColumn(4, "Улица")
        self.InsertColumn(5, "Дом")
        self.InsertColumn(6, "Квартира")
        self.InsertColumn(7, "Бригада")

    	self.SetColumnWidth(0, 100)
    	self.SetColumnWidth(1, 70)
    	self.SetColumnWidth(2, 100)
    	self.SetColumnWidth(3, 200)
    	self.SetColumnWidth(4, 150)
    	self.SetColumnWidth(5, 70)
    	self.SetColumnWidth(6, 70)
    	self.SetColumnWidth(7, 150)

#        self.Populate()


    def Populate(self,ts_shotdate):

	self.DeleteAllItems()

#### --- Получение данных по специализациям бригад ---	
	db=DBTools.DBTools()
	self.sc_rec_id = [] # массив идентификаторв строк записей 
#### --- Отображение данных в форме ---
	for row in db.GetListTask(ts_shotdate):
	    str0=row[1]	    
	    str1=row[2]
	    str2=row[3]
	    str3=row[4]
	    str4=row[5]
	    str5=row[6]
	    str6=row[7]
	    str7=row[8]

	    index=self.InsertStringItem(sys.maxint, str0)
	    self.SetStringItem( index, 0, str0)
	    self.SetStringItem( index, 1, str1)
	    self.SetStringItem( index, 2, str6)
	    self.SetStringItem( index, 3, str2)
	    self.SetStringItem( index, 4, str3)
	    self.SetStringItem( index, 5, str4)
	    self.SetStringItem( index, 6, str5)
	    self.SetStringItem( index, 7, str7)

	# -- Формирование массива из идентификаторов записей ---
	    self.sc_rec_id.append(row[0])
    
	    
	db.Destroy()
	
	self.currentItem=0



#### ---- Установка стоимоти по услуге в тарифном плане ---
class SetCostService(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition,
            style=wx.DEFAULT_DIALOG_STYLE
            ):



        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)

        sizer = wx.BoxSizer(wx.VERTICAL)

        label = wx.StaticText(self, -1, "Введите сумму")
        sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

 

#### --- Сумма , стоимость ---
        self.sc = wx.SpinCtrl(self, -1, "", size=(100,-1))
        self.sc.SetRange(0,1000)
        self.sc.SetValue(0)
        sizer.Add(self.sc, 0, wx.ALIGN_CENTRE|wx.ALL, 5)


	sizer.Add(wx.StaticLine(pre), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)


        self.btnsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.btn = wx.Button(self, wx.ID_OK)
        self.btn.SetDefault()
        self.btnsizer.Add(self.btn, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.btn2 = wx.Button(self, wx.ID_CANCEL)
        self.btnsizer.Add(self.btn2, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(self.btnsizer, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)


