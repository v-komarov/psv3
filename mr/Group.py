#coding:utf-8



import  wx
import	sys


from	RunSQLGroup	import	GetListGroup
from	RunSQLGroup	import	GetGroup
from	RunSQLGroup	import	AddGroup	as	AddGroupBD
from	RunSQLGroup	import	EditGroup	as	EditGroupBD
from	tools.Messages	import	ErrorData
from	tools.Messages	import	NotAccess




#*************************************************************************
# Форма справочника групп материала
#*************************************************************************


class GroupList(wx.Dialog):
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
        self.ctrl0 = ListGroup(pre, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
	self.ctrl0.Populate()
	self.ctrl0.SetItemState(0,wx.LIST_STATE_SELECTED,wx.LIST_STATE_SELECTED)
        box.Add(self.ctrl0, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER|wx.TOP, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)

        btn = wx.Button(self, wx.ID_ADD)        
#        btn1 = wx.Button(self, wx.ID_EDIT)
        btn1 = wx.Button(self,-1,"Переим.")
        btn2 = wx.Button(self, wx.ID_CLOSE)


        btn2.SetDefault()
        box.Add(btn, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL|wx.TOP, 5)
        box.Add(btn1, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL|wx.TOP, 5)
        box.Add(btn2, 0, wx.GROW|wx.ALIGN_CENTRE|wx.ALL|wx.TOP, 5)
        sizer.Add(box, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)


	self.Bind(wx.EVT_BUTTON, self.AddGroup,btn)
	self.Bind(wx.EVT_BUTTON, self.EditGroup, btn1)
	self.Bind(wx.EVT_BUTTON, self.Cancel, btn2)
	self.ctrl0.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem, self.ctrl0)




#### --- Добавление новой группы ---
    def	AddGroup(self,event):
	dlg = wx.TextEntryDialog(self, 'Введите название','Новая группа','', style=wx.OK|wx.CANCEL)
	if dlg.ShowModal() == wx.ID_OK:
	    result = AddGroupBD(dlg.GetValue())
	    if result == 'ERRORDATA':
		ErrorData(self)
	    elif result == 'NOTACCESS':
		NotAccess(self)
	    elif result == 'OK':
		self.ctrl0.Populate()
		self.ctrl0.SetItemState(0,wx.LIST_STATE_SELECTED,wx.LIST_STATE_SELECTED)		

	dlg.Destroy()	


	
	
#### --- Изменение названия группы ---
    def	EditGroup(self,event):
	row_id = self.ctrl0.kod_record[self.ctrl0.currentItem]
	select_id = self.ctrl0.currentItem
	dlg = wx.TextEntryDialog(self, 'Редактирование','Группа',GetGroup(row_id), style=wx.OK|wx.CANCEL)
	if dlg.ShowModal() == wx.ID_OK:
	    result = EditGroupBD(row_id,dlg.GetValue())
	    if result == 'ERRORDATA':
		ErrorData(self)
	    elif result == 'NOTACCESS':
		NotAccess(self)
	    elif result == 'OK':
		self.ctrl0.SetStringItem(select_id,0,GetGroup(row_id))
	dlg.Destroy()	




#### --- Закрытие формы ---
    def	Cancel(self,event):
	self.Destroy()



#### --- Присвоение значения по выбранной строке ---
    def ReadItem(self,event):
	self.ctrl0.currentItem = event.m_itemIndex








class ListGroup(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0),size=(300,300), style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)


        self.InsertColumn(0, "Название группы")

    	self.SetColumnWidth(0, 300)



    def Populate(self):

	self.DeleteAllItems()


#### --- Отображение данных в форме ---
	self.kod_record=[] # массив идентификаторов записей
	for row in GetListGroup():
	    index=self.InsertStringItem(sys.maxint, row[0])
	    self.SetStringItem( index, 0, row[1])
	# -- Заполнение массива идентификаторов записей ---
	    self.kod_record.append(row[0])    
	    
	self.currentItem=0








