#coding:utf-8

""" 
    Основной интерфейс отображения данных материала

"""


import  wx
from	DBTools		import	DBTools
from	RunSQLMainForm	import	GetListGroup
from	RunSQLMainForm	import	GetListEds
from	RunSQLMainForm	import	GetMate
from	RunSQLMainForm	import	EditMate
from	RunSQLPage1	import	AddMateIn	as	AddMateInDB
from	RunSQLPage1	import	DelMateIn	as	DelMateInDB
from	RunSQLPage3	import	NewCostMate
from	RunSQLPage3	import	DelCostMate
from	RunSQLPage4	import	SetMateStore
from	report.PeriodForm	import	GetPeriodStore
from	tools.Messages	import	ErrorData
from	tools.Messages	import	NotAccess
from	tools.Messages	import	SaveDone
from	tools.Messages	import	ErrorValue
from	Page1		import	Page1
from	Page1		import	AddMateIn
from	Page2		import	Page2
from	Page3		import	Page3
from	Page3		import	AddNewCost
from	Page4		import	Page4
from	Page5		import	Page5
from	report.PrintMr	import	RepMateInfo




#### --- Основная форма  ----
class MateForm(wx.Frame):
    def __init__(self,parent,ID,title, pos=wx.DefaultPosition,
            size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, rec_id=''):


        wx.Frame.__init__(self,parent,ID, title, pos, size, style)
        panel = wx.Panel(self, -1)
	
	mainsizer = wx.BoxSizer(wx.VERTICAL)

	tID = wx.NewId()


	#### --- Подключение к базе ---
	db = DBTools()


	#### --- Идентификатор записи ---
	self.rec_kod = rec_id

#### --- Заголовок ---
	sizer = wx.BoxSizer(wx.HORIZONTAL)
#	topLbl = wx.StaticText(panel, -1, "Материал")
#	topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
#	sizer.Add(topLbl, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
#	mainsizer.Add(sizer, 0, wx.ALIGN_LEFT|wx.ALL, 5)
#	mainsizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)


#### --- Кнопи управления ---
	btn = wx.Button(panel, wx.ID_SAVE)
	btn0 = wx.Button(panel, wx.ID_CLOSE)
	btn1 = wx.Button(panel, wx.ID_PRINT)
	

#### --- Поля заполнения и отображения информации ---

	sizer = wx.BoxSizer(wx.HORIZONTAL)
	fsizer = wx.BoxSizer(wx.VERTICAL)


	empty = wx.StaticText(panel,-1,"")



	label0 = wx.StaticText(panel,-1,"Название")
	label1 = wx.StaticText(panel,-1,"Ед. изм.")
	label2 = wx.StaticText(panel,-1,"Группа")

	self.field_0 = wx.TextCtrl(panel, -1, "", size=(300,-1))
        self.field_1 = wx.ComboBox(panel, -1, "", size=(200,-1), choices=GetListEds(db),style=wx.CB_DROPDOWN|wx.CB_READONLY)
        self.field_2 = wx.ComboBox(panel, -1, "", size=(300,-1), choices=GetListGroup(db),style=wx.CB_DROPDOWN|wx.CB_READONLY)


	fgsizer2 = wx.FlexGridSizer( rows = 3, cols = 2, hgap = 10, vgap = 10 )	
	fgsizer2.Add(label0,0,0)
	fgsizer2.Add(self.field_0,0,0)
	fgsizer2.Add(label1,0,0)
	fgsizer2.Add(self.field_1,0,0)
	fgsizer2.Add(label2,0,0)
	fgsizer2.Add(self.field_2,0,0)
	fsizer.Add(fgsizer2,0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5)
	fsizer.Add(empty,0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5)

	sizer.Add(fsizer,0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5)

#### --- Пустой разделитель ----
	esizer = wx.BoxSizer(wx.VERTICAL)
	labelx = wx.StaticText(panel,-1,"      ")
	esizer.Add(labelx,0, wx.GROW|wx.ALIGN_RIGHT, 5)
	sizer.Add(esizer,0, wx.GROW|wx.ALIGN_RIGHT, 5)
	

#### --- Расположение кнопок в другом вертикальном боксе ---	
	bsizer = wx.BoxSizer(wx.VERTICAL)
	bsizer.Add(btn,0, wx.GROW|wx.ALIGN_RIGHT, 5)
	bsizer.Add(btn0,0, wx.GROW|wx.ALIGN_RIGHT, 5)
	bsizer.Add(btn1,0, wx.GROW|wx.ALIGN_RIGHT, 5)
	sizer.Add(bsizer,0, wx.GROW|wx.ALIGN_RIGHT, 5)
	
	
	mainsizer.Add(sizer, 0, wx.ALIGN_CENTER|wx.ALL, 5)
	

#### --- Отображение данных ---
	self.ShowValue(db)


#### --- Форма с закладками ----
	sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.note = wx.Notebook(panel, -1)
	sizer.Add(self.note, 0, wx.ALIGN_CENTRE|wx.ALL|wx.GROW, 5)
	mainsizer.Add(sizer, 0, wx.ALIGN_CENTER|wx.ALL|wx.GROW, 5)


#### --- Закладки ---
	self.note.AddPage(Page1(self), "Поступления")
	self.note.AddPage(Page2(self), "Расход")
	self.note.AddPage(Page3(self), "Цены")
	self.note.AddPage(Page4(self), "Ввод остатков")
	self.note.AddPage(Page5(self), "Наличие")


	#### --- Отключение от базы ---
	db.Destroy()


	panel.SetSizer(mainsizer)
	mainsizer.Fit(self)

	self.Bind(wx.EVT_BUTTON, self.Save, btn)
	self.Bind(wx.EVT_BUTTON, self.Close, btn0)
	self.Bind(wx.EVT_BUTTON, self.MateInfo, btn1)






#### --- Заполнение формы (полей) значениями ---
    def	ShowValue(self,db):
	f = GetMate(db,self.rec_kod)
	self.field_0.SetValue(f[1])
	self.field_1.SetValue(f[2])
	self.field_2.SetValue(f[4])






#### --- Закрыть форму ----
    def	Close(self,event):
	self.Destroy()



#### --- Печатная движения по этому материалу ---
    def	MateInfo(self,event):
	dlg = GetPeriodStore(self, -1,"Период", size=(-1,-1), style=wx.DEFAULT_DIALOG_STYLE)
	if dlg.ShowModal() == wx.ID_OK:
	    store = dlg.field_2.GetValue()
	    date0 = str(dlg.field_0.GetValue().GetYear())+'-' + str(dlg.field_0.GetValue().GetMonth()+1) +'-'+ str(dlg.field_0.GetValue().GetDay())
	    date1 = str(dlg.field_1.GetValue().GetYear())+'-' + str(dlg.field_1.GetValue().GetMonth()+1) +'-'+ str(dlg.field_1.GetValue().GetDay())
	    periodstr = str(str(dlg.field_0.GetValue().GetDay())+'.'+str(dlg.field_0.GetValue().GetMonth()+1)+'.'+str(dlg.field_0.GetValue().GetYear())+' - '+str(dlg.field_1.GetValue().GetDay())+'.'+str(dlg.field_1.GetValue().GetMonth()+1)+'.'+str(dlg.field_1.GetValue().GetYear()))
	    if store == '':
		ErrorValue(self)
	    else:
		RepMateInfo(self.rec_kod,date0,date1,periodstr)

	dlg.Destroy()
	



#### --- Сохранение данных ---
    def	Save(self,event):
	db = DBTools()
	result = EditMate(db,self.rec_kod,self.field_0.GetValue(),self.field_1.GetValue(),self.field_2.GetValue())
	if result == 'OK':
	    self.ShowValue(db)
	    SaveDone(self)
	elif result == 'NOTACCESS':
	    NotAccess(self)
	elif result == 'ERRORDATA':
	    ErrorData(self)	

	db.Destroy()
	
	




#### --- Страница закладки ---
    def	Page(self):
	return wx.Panel(self.note, -1)


	







#************************************************************************
#    Управление поступлениями
#************************************************************************


#### --- Новое поступление ---
    def	Add1(self, evt):
	dlg = AddMateIn(self, -1,"Новое поступление", size=(-1,-1), style=wx.DEFAULT_DIALOG_STYLE)
	if dlg.ShowModal() == wx.ID_OK:
	    result = AddMateInDB(self.rec_kod, dlg.field_0.GetValue(),dlg.field_1.GetValue(),dlg.field_2.GetValue())
	    if result == 'ERRORDATA':
		ErrorData(self)
	    elif result == 'NOTACCESS':
		NotAccess(self)
	    elif result == 'OK':
		self.ctrl1.Populate(self.rec_kod)
		self.ctrl1.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
		self.ctrl5.Populate(self.rec_kod)
		self.ctrl5.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
	
	dlg.Destroy()




#### --- Удаление записи поступления ---
    def	Del1(self, evt):
	row_id = self.ctrl1.kod_record[self.ctrl1.currentItem]
	dlg = wx.MessageDialog(self, "Удалить поступление?", 'Удаление', wx.YES_NO)
	if dlg.ShowModal() == wx.ID_YES:
	    result = DelMateInDB(row_id)
	    if result == 'ERRORDATA':
		ErrorData(self)
	    elif result == 'NOTACCESS':
		NotAccess(self)
	    elif result == 'OK':
		self.ctrl1.Populate(self.rec_kod)
		self.ctrl1.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
		self.ctrl5.Populate(self.rec_kod)
		self.ctrl5.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
	
	dlg.Destroy()









#************************************************************************
#    Задание цен
#************************************************************************


#### --- Добавление новой цены ---
    def	Add3(self, evt):
	dlg = AddNewCost(self, -1,"Новая цена", size=(-1,-1), style=wx.DEFAULT_DIALOG_STYLE)
	if dlg.ShowModal() == wx.ID_OK:
	    db = DBTools()
	    date0 = str(dlg.field_0.GetValue().GetYear())+'-' + str(dlg.field_0.GetValue().GetMonth()+1) +'-'+ str(dlg.field_0.GetValue().GetDay())
	    result = NewCostMate(db,self.rec_kod, date0, dlg.field_1.GetValue())
	    if result == 'ERRORDATA':
		ErrorData(self)
	    elif result == 'NOTACCESS':
		NotAccess(self)
	    elif result == 'OK':
		self.ctrl3.Populate(self.rec_kod)    
		self.ctrl3.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
	    
	    db.Destroy()
	
	dlg.Destroy()




#### --- Удаление цены ---
    def	Del3(self, evt):
	row_id = self.ctrl3.kod_record[self.ctrl3.currentItem]
	dlg = wx.MessageDialog(self, "Удалить цену?", 'Удаление', wx.YES_NO)
	if dlg.ShowModal() == wx.ID_YES:
	    result = DelCostMate(row_id)
	    if result == 'ERRORDATA':
		ErrorData(self)
	    elif result == 'NOTACCESS':
		NotAccess(self)
	    elif result == 'OK':
		self.ctrl3.Populate(self.rec_kod)
		self.ctrl3.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
	
	dlg.Destroy()









#*************************************************************************
# 	Управление ввода начальных остатков
#*************************************************************************	


#### --- Ввод остатка ---
    def	Add4(self, evt):
	dlg = AddMateIn(self, -1,"Ввод остатка", size=(-1,-1), style=wx.DEFAULT_DIALOG_STYLE, abonent_kod=self.rec_kod)
	if dlg.ShowModal() == wx.ID_OK:
	    result = SetMateStore(self.rec_kod, dlg.field_0.GetValue(), dlg.field_1.GetValue(), dlg.field_2.GetValue())
	    if result == 'ERRORDATA':
		ErrorData(self)
	    elif result == 'NOTACCESS':
		NotAccess(self)
	    elif result == 'OK':
		self.ctrl4.Populate(self.rec_kod)
		self.ctrl4.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
		self.ctrl5.Populate(self.rec_kod)
		self.ctrl5.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)		
	
	dlg.Destroy()










