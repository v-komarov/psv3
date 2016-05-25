#!/usr/bin/env python
#coding:utf-8

import  wx
import	os
import	sys
import	time
import	string
import	wx.lib.dialogs
import	RWCfg
import	About
import	ReadSpr
import	Check
import	Internet
import	Admin
import	wx.lib.printout as printout
from	backup.Store	import	Backup
from	backup.Store	import	Restore
from	abonent.Abonent	import	Abonent
from	abonent.NewAbonent	import	AbonentAdd
from	abonent.RunSQL	import	FindAbonentDB
from	abonent.RunSQL	import	FindLsp
from	mr.Group	import	GroupList
from	mr.Mate		import	NewMate
from	mr.MainForm	import	MateForm
from	mr.Mate		import	ShowFindListMate
from	mr.Mate		import	ChMate
from	mr.RunSQLMate		import	AddMate
from	mr.RunSQLMate		import	FindMate
from	plat.AutoPlat	import	List2Txt
from	plat.AutoPlat	import	txt2Base
from	plat.Brig	import	Brig2Txt
from	plat.Brig	import	brig2Base
from	plat.KassPlat	import	kass2Txt
from	plat.KassPlat	import	kass2Base
from	plat.CityPay	import	CityPay2Txt
from	plat.CityPay	import	citypay2Base
from	tplan.TPlan	import	AddTarifPlan
from	tplan.TPlan	import	ServiceTarifPlan
from	tplan.TPlan	import	EditTarifPlanName
from	report.Reports	import	ChoiseUlDom
from	report.Reports	import	ChoiseUlDomSer
from	report.Reports	import	ChoiseUlDomSer2
from	report.Reports	import	ChoiseUlDomSer3
from	report.Reports	import	TarifPlanList
from	report.Reports	import	AbonentShowAll
from	report.Reports	import	AbonentShowPart
from	report.Reports	import	TaskListDom
from	report.Reports	import	TaskListNoClose
from	report.PeriodForm	import	GetPeriod
from	report.PeriodForm	import	GetPeriodKassa
from	report.PeriodForm	import	ChoiseUlDomP
from	report.PeriodForm	import	ChoiceStoreGroup
from	report.PeriodForm	import	ChoiseDateUlDom
from	report.PrintData	import	AbonentList	as	AbonentList2
from	report.PrintData	import	AbonentServiceBalans
from	report.PrintData	import	DolList
from	report.PrintData	import	DolListService
from	report.PrintData	import	DolDomService
from	report.PrintData	import	BalansList
from	report.PrintData	import	DolListOff
from	report.PrintData	import	Messages4Abonents
from	report.PrintData	import	Messages4Abonents2
from	report.PrintData	import	Messages4Abonents3
from	report.PrintData	import	RepPayAll
from	report.PrintData	import	RepPayKassa
from	report.PrintData	import	ListPaySystem
from	report.PrintData	import	ListPaySystem2
from	report.PrintData	import	ListPaySystem3
from	report.PrintData	import	ListPaySystem4
from	report.PrintData	import	ListMac
from	report.PrintData	import	ListNoCloseTask
from	report.PrintMr		import	RepMateStore
from	report.PrintMr		import	RepTaskP
from	report.PrintSourceNet	import	SourceNet
#from	report.RunSQL	import	GetListPayDay
from	task.Worker	import	ListPerson
from	task.MainListTask	import	MainListTask
from	task.PrintTask		import	Naryad_Zakaz_PrintForm
from	tools.Messages	import	FileSave
from	tools.Messages	import	ErrorValue
from	tools.Messages	import	LoadDone
from	tools.Messages	import	NotAccess
from	tools.Messages	import	ErrorData




#----------------------------------------------------------------------
ID_Find  = wx.NewId()
ID_FindLsp  = wx.NewId()
ID_Exit = wx.NewId()
ID_Close= wx.NewId()
ID_Db	= wx.NewId()
ID_Dbout= wx.NewId()
ID_Dbin	= wx.NewId()
ID_Tplan= wx.NewId()
ID_NewAb= wx.NewId()
ID_List	= wx.NewId()
ID_ListDol=wx.NewId()
ID_About = wx.NewId()
ID_Help = wx.NewId()
#ID_Chver = wx.NewId()
ID_ListTplan = wx.NewId()
ID_AddTPlan = wx.NewId()
ID_ReNameTPlan = wx.NewId()
ID_EditWorker = wx.NewId()
ID_ListTask = wx.NewId()
ID_TaskDom = wx.NewId()
ID_TaskNoClose = wx.NewId()
ID_IntNewCost = wx.NewId()
ID_IntEditCost = wx.NewId()
ID_ListLogin = wx.NewId()
ID_Abon2Txt = wx.NewId()
ID_Txt2Base = wx.NewId()
ID_Kass2Base = wx.NewId()
#ID_RunSQL = wx.NewId()
ID_PrintAbonentList = wx.NewId()
ID_PrintAbonentService = wx.NewId()
ID_PrintBalansList = wx.NewId()
ID_PrintDol = wx.NewId()
ID_PrintDolSer = wx.NewId()
ID_PrintDolAll = wx.NewId()
ID_PrintDolOff = wx.NewId()
ID_PrintDolTxt = wx.NewId()
ID_PrintDolTxtSer = wx.NewId()
ID_PrintDolTxtSerN = wx.NewId()
ID_PrintTaskP = wx.NewId()
ID_KassaInto = wx.NewId()
ID_PaySystem = wx.NewId()
ID_PaySystem2 = wx.NewId()
ID_PaySystem3 = wx.NewId()
ID_PaySystem4 = wx.NewId()
ID_ListMAC = wx.NewId()
ID_Abon2Brig = wx.NewId()
ID_Brig2Base = wx.NewId()
ID_Abon2Kass = wx.NewId()
ID_Abon2CityPay = wx.NewId()
ID_CityPay2Base = wx.NewId()
ID_PrintTaskNoClose = wx.NewId()
ID_PrintSourceNet = wx.NewId()
ID_MrFind = wx.NewId()
ID_MrNew = wx.NewId()
ID_MrGroup = wx.NewId()
ID_ChoiceMate = wx.NewId()
ID_PrintMrStore = wx.NewId()
ID_Naryad_Zakaz = wx.NewId()


### --- Запомнить родной каталог ---
psdir = os.getcwd()



### --- Предварительное удаление временных файлов ---
for f in os.listdir(psdir+'/tmp'):
    os.remove(psdir+'/tmp/'+f)


#----------------------------------------------------------------------

class MyParentFrame(wx.MDIParentFrame):
    def __init__(self):
        wx.MDIParentFrame.__init__(self, None, 1, "PS", size=(700,500))

    	self.MId=wx.NewId()
	
        self.winCount = 0
        menu = wx.Menu()
        menu.Append(ID_Find, "Поиск абонента")
        menu.Append(ID_FindLsp, "Поиск по номеру счета")
        menu.Append(ID_NewAb, "Новый абонент")
        menu.AppendSeparator()
        menu.Append(ID_AddTPlan, "Новый тарифный план")
        menu.Append(ID_Tplan, "Состав тарифного плана")
        menu.Append(ID_ReNameTPlan, "Переименовать тарифный план")
        menu.AppendSeparator()
        menu.Append(ID_Close, "Закрыть")
        menu.AppendSeparator()
        menu.Append(ID_Exit, "Выход")
        menubar = wx.MenuBar()
        menubar.Append(menu, "Абонент")


        menu1 = wx.Menu()
        menu1.Append(ID_ListTask, "Управление заявками")
        menu1.Append(ID_Naryad_Zakaz, "Наряд-Заказ")
        menu1.AppendSeparator()
        menu1.Append(ID_EditWorker, "Исполнители")
        menubar.Append(menu1, "Заявки")


        menu2 = wx.Menu()
        menu2.Append(ID_MrFind, "Поиск материала")
        menu2.Append(ID_ChoiceMate, "Выбор материала по списку")
        menu2.Append(ID_MrNew, "Новый материал")
        menu2.AppendSeparator()
        menu2.Append(ID_MrGroup, "Группы материала")
        menubar.Append(menu2, "Материалы")


        menu3 = wx.Menu()
        menu3.Append(ID_List, "Список абонентов")
        menu3.Append(ID_ListDol, "Должники")
        menu3.AppendSeparator()
        menu3.Append(ID_ListTplan, "Тарифные планы")
        menu3.AppendSeparator()
        menu3.Append(ID_TaskDom, "Заявки по домам")
        menu3.Append(ID_TaskNoClose, "Незавершенные заявки")
        menu3.AppendSeparator()
	submenu = wx.Menu()
	submenu.Append(ID_PrintAbonentList, "Список абонентов")
	submenu.Append(ID_PrintAbonentService, "Остатки по услугам")
	submenu.Append(ID_PrintBalansList, "Баланс (по дому)")
	submenu.Append(ID_PrintDol, "Должники")
	submenu.Append(ID_PrintDolSer, "Должники (по услугам)")
	submenu.Append(ID_PrintDolAll, "Общие долги по домам (по услугам)")
	submenu.Append(ID_PrintDolOff, "Отключенные должники")
	submenu.Append(ID_PrintDolTxt, "Объявления должникам")
	submenu.Append(ID_PrintDolTxtSer, "Объявления должникам (по услугам)")
	submenu.Append(ID_PrintDolTxtSerN, "Объявления должникам (список услуг)")
        submenu.AppendSeparator()
	submenu.Append(ID_KassaInto, "Поступления")
	submenu.Append(ID_PaySystem, "Журнал загрузок платежей (ПЛАТЁЖКА)")
	submenu.Append(ID_PaySystem2, "Журнал загрузок платежей (БРИГАНТИНА)")
	submenu.Append(ID_PaySystem3, "Журнал загрузок платежей (КАСС)")
	submenu.Append(ID_PaySystem4, "Журнал загрузок платежей (CityPay)")
        submenu.AppendSeparator()
	submenu.Append(ID_ListMAC, "Список MAC адресов")
        submenu.AppendSeparator()
	submenu.Append(ID_PrintTaskNoClose, "Не завершенные заявки")
	submenu.Append(ID_PrintTaskP, "Заявки по подъездам")
        submenu.AppendSeparator()
	submenu.Append(ID_PrintMrStore, "Остатки на складе")
        submenu.AppendSeparator()
	submenu.Append(ID_PrintSourceNet, "Ресурсы сети")
	menu3.AppendMenu(203, "Печатные формы", submenu)
        menubar.Append(menu3, "Отчеты")


#        menu4 = wx.Menu()
#        menu4.Append(ID_ListLogin, "Учетные записи")
#        menu4.AppendSeparator()
#        menu4.Append(ID_IntEditCost, "Тарифы трафика")
#        menu4.Append(ID_IntNewCost, "Новый тариф")
#        menubar.Append(menu4, "Internet")


        menu5 = wx.Menu()
        menu5.Append(ID_Db, "Сервер данных")
        menu5.AppendSeparator()
        menu5.Append(ID_Dbout, "Резервирование данных")
        menu5.Append(ID_Dbin, "Восстановление данных")
        menu5.AppendSeparator()
        menu5.Append(ID_Abon2Txt, "Выгрузить внешние коды")
        menu5.Append(ID_Txt2Base, "Загрузить внешние платежи")
        menu5.AppendSeparator()
        menu5.Append(ID_Abon2Brig, "Выгрузить коды для Бригантины")
        menu5.Append(ID_Brig2Base, "Загрузить платежи от Бригантины")
        menu5.AppendSeparator()
        menu5.Append(ID_Abon2Kass, "Выгрузить внешние коды КАСС")
        menu5.Append(ID_Kass2Base, "Загрузить внешние платежи КАСС")        
        menu5.AppendSeparator()
        menu5.Append(ID_Abon2CityPay, "Выгрузить внешние коды CityPay")
        menu5.Append(ID_CityPay2Base, "Загрузить внешние платежи CityPay")        
	menubar.Append(menu5, "Данные")


#        menu5 = wx.Menu()
#        menu5.Append(ID_RunSQL, "Выполнить скрипт SQL")
#        menubar.Append(menu5, "Администрирование")



        menu6 = wx.Menu()
#        menu6.Append(ID_Chver, "Изменения версий")
#        menu6.AppendSeparator()
        menu6.Append(ID_About, "О программе")
        menubar.Append(menu6, "Помощь")

        
	self.SetMenuBar(menubar)

        self.CreateStatusBar()

        self.Bind(wx.EVT_MENU, self.FindAbonent, id=ID_Find)
        self.Bind(wx.EVT_MENU, self.FindLsp, id=ID_FindLsp)
        self.Bind(wx.EVT_MENU, self.NewAbonent, id=ID_NewAb)
        self.Bind(wx.EVT_MENU, self.TarifPlan, id=ID_Tplan)
        self.Bind(wx.EVT_MENU, self.ServerDb, id=ID_Db)
        self.Bind(wx.EVT_MENU, self.ServerDbOut, id=ID_Dbout)
        self.Bind(wx.EVT_MENU, self.ServerDbIn, id=ID_Dbin)
        self.Bind(wx.EVT_MENU, self.OnExit, id=ID_Exit)
        self.Bind(wx.EVT_MENU, self.AbonentList, id=ID_List)
        self.Bind(wx.EVT_MENU, self.DolList, id=ID_ListDol)
        self.Bind(wx.EVT_MENU, self.TplanList, id=ID_ListTplan)
        self.Bind(wx.EVT_MENU, self.About, id=ID_About)
#        self.Bind(wx.EVT_MENU, self.Chver, id=ID_Chver)
        self.Bind(wx.EVT_MENU, self.AddTPlan, id=ID_AddTPlan)
        self.Bind(wx.EVT_MENU, self.ReNameTPlan, id=ID_ReNameTPlan)
        self.Bind(wx.EVT_MENU, self.EditWorker, id=ID_EditWorker)
        self.Bind(wx.EVT_MENU, self.ListTask, id=ID_ListTask)
        self.Bind(wx.EVT_MENU, self.TaskDom, id=ID_TaskDom)
        self.Bind(wx.EVT_MENU, self.TaskNoClose, id=ID_TaskNoClose)
        self.Bind(wx.EVT_MENU, self.IntNewCost, id=ID_IntNewCost)
        self.Bind(wx.EVT_MENU, self.IntEditCost, id=ID_IntEditCost)
        self.Bind(wx.EVT_MENU, self.ListLogin, id=ID_ListLogin)
        self.Bind(wx.EVT_MENU, self.Abon2Txt, id=ID_Abon2Txt)
        self.Bind(wx.EVT_MENU, self.Abon2Brig, id=ID_Abon2Brig)
        self.Bind(wx.EVT_MENU, self.Abon2Kass, id=ID_Abon2Kass)
        self.Bind(wx.EVT_MENU, self.Abon2CityPay, id=ID_Abon2CityPay)
        self.Bind(wx.EVT_MENU, self.Txt2Base, id=ID_Txt2Base)
        self.Bind(wx.EVT_MENU, self.Brig2Base, id=ID_Brig2Base)
        self.Bind(wx.EVT_MENU, self.Kass2Base, id=ID_Kass2Base)
        self.Bind(wx.EVT_MENU, self.CityPay2Base, id=ID_CityPay2Base)

#        self.Bind(wx.EVT_MENU, self.RunSQL, id=ID_RunSQL)
        self.Bind(wx.EVT_MENU, self.PrintAbonentList, id=ID_PrintAbonentList)
        self.Bind(wx.EVT_MENU, self.PrintAbonentService, id=ID_PrintAbonentService)
        self.Bind(wx.EVT_MENU, self.PrintBalansList, id=ID_PrintBalansList)
        self.Bind(wx.EVT_MENU, self.PrintDol, id=ID_PrintDol)
        self.Bind(wx.EVT_MENU, self.PrintDolSer, id=ID_PrintDolSer)
        self.Bind(wx.EVT_MENU, self.PrintDolAll, id=ID_PrintDolAll)
        self.Bind(wx.EVT_MENU, self.PrintDolOff, id=ID_PrintDolOff)
        self.Bind(wx.EVT_MENU, self.PrintDolTxt, id=ID_PrintDolTxt)
        self.Bind(wx.EVT_MENU, self.PrintDolTxtSer, id=ID_PrintDolTxtSer)
        self.Bind(wx.EVT_MENU, self.PrintDolTxtSerN, id=ID_PrintDolTxtSerN)
        self.Bind(wx.EVT_MENU, self.KassaInto, id=ID_KassaInto)
        self.Bind(wx.EVT_MENU, self.PaySystem, id=ID_PaySystem)
        self.Bind(wx.EVT_MENU, self.PaySystem2, id=ID_PaySystem2)
	self.Bind(wx.EVT_MENU, self.PaySystem3, id=ID_PaySystem3)
	self.Bind(wx.EVT_MENU, self.PaySystem4, id=ID_PaySystem4)
        self.Bind(wx.EVT_MENU, self.ListMAC, id=ID_ListMAC)
        self.Bind(wx.EVT_MENU, self.OnClose, id=ID_Close)
        self.Bind(wx.EVT_MENU, self.TaskNoClosePrint, id=ID_PrintTaskNoClose)
        self.Bind(wx.EVT_MENU, self.PrintTaskP, id=ID_PrintTaskP)
        self.Bind(wx.EVT_MENU, self.PrintSourceNet, id=ID_PrintSourceNet)
        self.Bind(wx.EVT_MENU, self.Naryad_Zakaz, id=ID_Naryad_Zakaz)

        self.Bind(wx.EVT_MENU, self.MateGroup, id=ID_MrGroup)
        self.Bind(wx.EVT_MENU, self.MateNew, id=ID_MrNew)
        self.Bind(wx.EVT_MENU, self.MateFind, id=ID_MrFind)
        self.Bind(wx.EVT_MENU, self.ChoiceMate, id=ID_ChoiceMate)

        self.Bind(wx.EVT_MENU, self.PrintMrStore, id=ID_PrintMrStore)



#### --- Список исполнителей ---
    def EditWorker(self, evt):
	wk = ListPerson(self,-1,"Исполнители",
        size=(400,250), style=wx.DEFAULT_DIALOG_STYLE)
	wk.ShowModal()
	wk.Destroy()



#### --- Управление заявками ---
    def ListTask(self, evt):
	wk = MainListTask(self,-1,"Заявки", size=(400,250), style=wx.DEFAULT_FRAME_STYLE)
	wk.Centre()
	wk.Show(True)




    def AddTPlan(self, evt):
	AddTarifPlan(self)



    def ReNameTPlan(self, evt):
	EditTarifPlanName(self)



    def OnExit(self, evt):
        self.Close(True)



    def OnClose(self, evt):
        win = self.GetActiveChild()
	if win:
	    win.Destroy()




    def FindAbonent(self, evt):
        dlg = wx.TextEntryDialog(
                self, 'Введите первые буквы улицы,\n через пробел номер дома и квартиры',
                'Поиск','')
        if dlg.ShowModal() == wx.ID_OK:
            qarray=string.split(dlg.GetValue())
	    re_find=FindAbonentDB(qarray[0],qarray[1],qarray[2])

		    

	    if re_find == 'NORESULT':

		dlg2=wx.MessageDialog(self,'Адрес не найден,\nлибо выборка слишком большая','Результат поиска',wx.OK)		
		dlg2.ShowModal()
		dlg2.Destroy()
	    
	    else :
		RWCfg.WriteValue('FoundRecord', re_find)
    		self.EditAbonent()
        
	dlg.Destroy()



#### --- Поиск абонента по номеру его лицевого счета ---
    def FindLsp(self, evt):
        dlg = wx.TextEntryDialog(
                self, 'Введите номер лицевого счета',
                'Поиск','')
        if dlg.ShowModal() == wx.ID_OK:
	    re_find=FindLsp(dlg.GetValue())
		    

	    if re_find == 'NORESULT':

		dlg2=wx.MessageDialog(self,'Лицевой счет не найден','Результат поиска',wx.OK)		
		dlg2.ShowModal()
		dlg2.Destroy()
	    
	    else :
		RWCfg.WriteValue('FoundRecord', re_find)
    		self.EditAbonent()
        
	dlg.Destroy()





####--- Редактирование абонента, платежи и удержания ----
    def EditAbonent(self):
	    ab = Abonent(self,-1,"Абонент", pos=wx.DefaultPosition,
	    size=(600,490), style=wx.MINIMIZE_BOX|wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.FRAME_FLOAT_ON_PARENT)
	    ab.Centre()
	    ab.Show(True)

	


####--- Ввод новых абонентов ---
    def NewAbonent(self, evt):
	    nab = AbonentAdd(self,self.MId,"Новый абонент", pos=wx.DefaultPosition,
            size=(600,150), style=wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.FRAME_FLOAT_ON_PARENT)
	    nab.Centre()
	    nab.Show(True)
	    





    def TarifPlan(self, evt):
	    tp = ServiceTarifPlan(self,-1,"Тарифные планы", pos=wx.DefaultPosition,
            size=(400,250), style=wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.FRAME_FLOAT_ON_PARENT)
	    tp.Centre()
	    tp.Show(True)




    ### --- Ввод нового материала ---
    def	MateNew(self,evt):
	dlg = NewMate(self,-1,"Новый материал",size=(400,250), style=wx.DEFAULT_DIALOG_STYLE)
	if dlg.ShowModal() == wx.ID_OK:
	    result = AddMate(dlg.field_0.GetValue(),dlg.field_1.GetValue(),dlg.field_2.GetValue())
	    if result[0:2] == 'OK':
		mate_id = result.split('#')[1]
		a = MateForm(self,-1,"Материал",size=(400,250), style=wx.MINIMIZE_BOX|wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.FRAME_FLOAT_ON_PARENT,rec_id=mate_id)
		a.Centre()
		a.Show(True)

	    elif result == 'ERRORDATA':
		ErrorData(self)
	    elif result == 'NOTACCESS':
		NotAccess(self)
	dlg.Destroy()


    ### --- Поиск материала ---
    def MateFind(self,evt):
        dlg = wx.TextEntryDialog(self, 'Введите первые буквы названия','Поиск материала','')
	if dlg.ShowModal() == wx.ID_OK:
	    find_str = dlg.GetValue()
	    if find_str == '':
		ErrorValue(self)
	    else:
		r = FindMate(find_str)
		if r == 'NOT':
		    ErrorData(self)
		elif r[0:3] == 'ONE':
		    mate_id = r.split('#')[1]
		    a = MateForm(self,-1,"Материал",size=(400,250), style=wx.MINIMIZE_BOX|wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.FRAME_FLOAT_ON_PARENT,rec_id=mate_id)
		    a.Centre()
		    a.Show(True)
		else:
		    dlg2 = ShowFindListMate(self,-1,"Список найденного",size=(400,250), style=wx.DEFAULT_DIALOG_STYLE,mate_list=r)
		    if dlg2.ShowModal() == wx.ID_OK:
			mate_id = dlg2.ctrl0.kod_record[dlg2.ctrl0.currentItem]
			a = MateForm(self,-1,"Материал",size=(400,250), style=wx.MINIMIZE_BOX|wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.FRAME_FLOAT_ON_PARENT,rec_id=mate_id)
			a.Centre()
			a.Show(True)
		    dlg2.Destroy()
	dlg.Destroy()	




    ### --- Выбор материала из списка ---
    def	ChoiceMate(self,evt):
	dlg = ChMate(self,-1,"Список по группам",size=(400,250), style=wx.DEFAULT_DIALOG_STYLE)
	if dlg.ShowModal() == wx.ID_OK:
	    mate_id = dlg.ctrl0.kod_record[dlg.ctrl0.currentItem]
	    a = MateForm(self,-1,"Материал",size=(400,250), style=wx.MINIMIZE_BOX|wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.FRAME_FLOAT_ON_PARENT,rec_id=mate_id)
	    a.Centre()
	    a.Show(True)
	dlg.Destroy()



    ### --- Справочник групп материала ---
    def	MateGroup(self,evt):
	dlg = GroupList(self,-1,"Группы материалов",size=(400,250), style=wx.DEFAULT_DIALOG_STYLE)
	dlg.ShowModal()
	dlg.Destroy()
	



#### --- Отчет: Вывод всего списка абонентов ---
    def AbonentList(self,event):
        dlg = ChoiseUlDom(self, -1, "Выбор улицы и дома", size=(350, 200),
                         style = wx.DEFAULT_DIALOG_STYLE
                         )
        dlg.Centre()

        val = dlg.ShowModal()
   
        if val == wx.ID_OK:
	    item = dlg.ctrl1.currentItem
	    UlDom = dlg.ctrl1.kod_record[item]
	    win = wx.MDIChildFrame(self, -1, 'Список абонентов')
	    canvas = AbonentShowAll(win, UlDom)
	    win.Show(True)
        dlg.Destroy()




#### --- Печатная форма: Вывод списка всех абонентов ---
    def PrintAbonentList(self,event):
        dlg = ChoiseUlDom(self, -1, "Выбор улицы и дома", size=(350, 200),
                         style = wx.DEFAULT_DIALOG_STYLE
                         )
        dlg.Centre()

        val = dlg.ShowModal()
   
        if val == wx.ID_OK:
	    item = dlg.ctrl1.currentItem
	    UlDom = dlg.ctrl1.kod_record[item]
	    
	    AbonentList2(UlDom)

        dlg.Destroy()





#### --- Печатная форма: Вывод списка абонентов с остатками по услугам ---
    def PrintAbonentService(self,event):
        dlg = ChoiseUlDom(self, -1, "Выбор улицы и дома", size=(350, 200),
                         style = wx.DEFAULT_DIALOG_STYLE
                         )
        dlg.Centre()

        val = dlg.ShowModal()
   
        if val == wx.ID_OK:
	    item = dlg.ctrl1.currentItem
	    UlDom = dlg.ctrl1.kod_record[item]
	    
	    AbonentServiceBalans(UlDom)

        dlg.Destroy()




#### --- Печатная форма: Вывод баланс по дому ---
    def PrintBalansList(self,event):
	BalansList()




#### --- Отчет: Вывод списка должников ---
    def DolList(self,event):
        dlg = ChoiseUlDom(self, -1, "Выбор улицы и дома", size=(350, 200),
                         style = wx.DEFAULT_DIALOG_STYLE
                         )
        dlg.Centre()

        val = dlg.ShowModal()
   
        if val == wx.ID_OK:
	    item = dlg.ctrl1.currentItem
	    UlDom = dlg.ctrl1.kod_record[item]
	    win = wx.MDIChildFrame(self, -1, 'Список должников')
	    canvas = AbonentShowPart(win, UlDom)
	    win.Show(True)
        dlg.Destroy()




#### --- Печатная форма: Вывод списка должников ---
    def PrintDol(self,event):
        dlg = ChoiseUlDom(self, -1, "Выбор улицы и дома", size=(350, 200),
                         style = wx.DEFAULT_DIALOG_STYLE
                         )
        dlg.Centre()

        val = dlg.ShowModal()
   
        if val == wx.ID_OK:
	    item = dlg.ctrl1.currentItem
	    UlDom = dlg.ctrl1.kod_record[item]
	    
	    DolList(UlDom)

        dlg.Destroy()





#### --- Печатная форма: Вывод списка должников (с выбором по услугам) ---
    def PrintDolSer(self,event):
        dlg = ChoiseUlDomSer(self, -1, "Выбор улицы, дома, услуги", size=(350, 200),
                         style = wx.DEFAULT_DIALOG_STYLE
                         )
        dlg.Centre()

        val = dlg.ShowModal()
   
        if val == wx.ID_OK:
	    item = dlg.ctrl1.currentItem
	    UlDom = dlg.ctrl1.kod_record[item]
	    service = dlg.field_0.GetValue()
	    
	    DolListService(UlDom,service)

        dlg.Destroy()




#### --- Печатная форма: Вывод долгов по домам (по услугам) ---
    def PrintDolAll(self,event):
	DolDomService()




#### --- Печатная форма: Вывод списка _отключенных_ должников ---
    def PrintDolOff(self,event):
	DolListOff()



#### --- Печатная форма: печать объявлений должникам ---
    def PrintDolTxt(self,event):
        dlg = ChoiseUlDom(self, -1, "Выбор улицы и дома", size=(350, 200),
                         style = wx.DEFAULT_DIALOG_STYLE
                         )
        dlg.Centre()

        val = dlg.ShowModal()
   
        if val == wx.ID_OK:
	    item = dlg.ctrl1.currentItem
	    UlDom = dlg.ctrl1.kod_record[item]

	    Messages4Abonents(UlDom)
	    
        dlg.Destroy()





#### --- Печатная форма: печать объявлений должникам (с выбором по услугам, месяцам, минимальной сумме долга) ---
    def PrintDolTxtSer(self,event):
        dlg = ChoiseUlDomSer2(self, -1, "Выбор улицы и дома", size=(350, 200),
                         style = wx.DEFAULT_DIALOG_STYLE
                         )
        dlg.Centre()

        val = dlg.ShowModal()
   
        if val == wx.ID_OK:
	    item = dlg.ctrl1.currentItem
	    UlDom = dlg.ctrl1.kod_record[item]
	    ser = dlg.field_0.GetValue()
	    month = dlg.field_1.GetValue()
	    min_sum = dlg.field_2.GetValue()

	    if len(ser) == 0 or len(month) == 0 or len(min_sum) == 0:
		ErrorData(self)

	    else:
		Messages4Abonents2(UlDom,ser,month,min_sum)
	    
        dlg.Destroy()





#### --- Печатная форма: печать объявлений должникам (с выбором по нескольким услугам, месяцам, минимальной сумме долга) ---
    def PrintDolTxtSerN(self,event):
        dlg = ChoiseUlDomSer3(self, -1, "Выбор улицы и дома", size=(350, 200),
                         style = wx.DEFAULT_DIALOG_STYLE
                         )
        dlg.Centre()

        val = dlg.ShowModal()
   
        if val == wx.ID_OK:
	    item = dlg.ctrl1.currentItem
	    UlDom = dlg.ctrl1.kod_record[item]

	    Messages4Abonents3(UlDom,dlg.item)
	    
        dlg.Destroy()





#### --- Печатная форма Отчет "Поступления" ----
    def	KassaInto(self,event):
	dlg = GetPeriodKassa(self,-1,"Период", size=(350,200), style = wx.DEFAULT_DIALOG_STYLE)
	if dlg.ShowModal() == wx.ID_OK:
	    date0 = str(dlg.field_0.GetValue().GetYear())+'-' + str(dlg.field_0.GetValue().GetMonth()+1) +'-'+ str(dlg.field_0.GetValue().GetDay())
	    date1 = str(dlg.field_1.GetValue().GetYear())+'-' + str(dlg.field_1.GetValue().GetMonth()+1) +'-'+ str(dlg.field_1.GetValue().GetDay())
	    periodstr = str(str(dlg.field_0.GetValue().GetDay())+'.'+str(dlg.field_0.GetValue().GetMonth()+1)+'.'+str(dlg.field_0.GetValue().GetYear())+' - '+str(dlg.field_1.GetValue().GetDay())+'.'+str(dlg.field_1.GetValue().GetMonth()+1)+'.'+str(dlg.field_1.GetValue().GetYear()))
	    kassa = dlg.field_2.GetValue()
	    if kassa == '':
		ErrorValue(self)
	    elif kassa == 'BCE':
	    	RepPayAll(date0,date1,periodstr)
	    else:
		RepPayKassa(date0,date1,periodstr,kassa)
	dlg.Destroy()
	





#### --- Печатная форма Отчет "Журнал загрузок" ---
    def PaySystem(self, evt):
	dlg = GetPeriod(self,-1,"Период", size=(350,200), style = wx.DEFAULT_DIALOG_STYLE)
	if dlg.ShowModal() == wx.ID_OK:
	    date0 = str(dlg.field_0.GetValue().GetYear())+'-' + str(dlg.field_0.GetValue().GetMonth()+1) +'-'+ str(dlg.field_0.GetValue().GetDay())
	    date1 = str(dlg.field_1.GetValue().GetYear())+'-' + str(dlg.field_1.GetValue().GetMonth()+1) +'-'+ str(dlg.field_1.GetValue().GetDay())
	    periodstr = str(str(dlg.field_0.GetValue().GetDay())+'.'+str(dlg.field_0.GetValue().GetMonth()+1)+'.'+str(dlg.field_0.GetValue().GetYear())+' - '+str(dlg.field_1.GetValue().GetDay())+'.'+str(dlg.field_1.GetValue().GetMonth()+1)+'.'+str(dlg.field_1.GetValue().GetYear()))
	    ListPaySystem(date0,date1,periodstr)
	dlg.Destroy()



#### --- Печатная форма Отчет "Журнал загрузок" (по Бригантине)  ---
    def PaySystem2(self, evt):
	dlg = GetPeriod(self,-1,"Период", size=(350,200), style = wx.DEFAULT_DIALOG_STYLE)
	if dlg.ShowModal() == wx.ID_OK:
	    date0 = str(dlg.field_0.GetValue().GetYear())+'-' + str(dlg.field_0.GetValue().GetMonth()+1) +'-'+ str(dlg.field_0.GetValue().GetDay())
	    date1 = str(dlg.field_1.GetValue().GetYear())+'-' + str(dlg.field_1.GetValue().GetMonth()+1) +'-'+ str(dlg.field_1.GetValue().GetDay())
	    periodstr = str(str(dlg.field_0.GetValue().GetDay())+'.'+str(dlg.field_0.GetValue().GetMonth()+1)+'.'+str(dlg.field_0.GetValue().GetYear())+' - '+str(dlg.field_1.GetValue().GetDay())+'.'+str(dlg.field_1.GetValue().GetMonth()+1)+'.'+str(dlg.field_1.GetValue().GetYear()))
	    ListPaySystem2(date0,date1,periodstr)
	dlg.Destroy()



#### --- Печатная форма Отчет "Журнал загрузок" (по Касс)  ---
    def PaySystem3(self, evt):
	dlg = GetPeriod(self,-1,"Период", size=(350,200), style = wx.DEFAULT_DIALOG_STYLE)
	if dlg.ShowModal() == wx.ID_OK:
	    date0 = str(dlg.field_0.GetValue().GetYear())+'-' + str(dlg.field_0.GetValue().GetMonth()+1) +'-'+ str(dlg.field_0.GetValue().GetDay())
	    date1 = str(dlg.field_1.GetValue().GetYear())+'-' + str(dlg.field_1.GetValue().GetMonth()+1) +'-'+ str(dlg.field_1.GetValue().GetDay())
	    periodstr = str(str(dlg.field_0.GetValue().GetDay())+'.'+str(dlg.field_0.GetValue().GetMonth()+1)+'.'+str(dlg.field_0.GetValue().GetYear())+' - '+str(dlg.field_1.GetValue().GetDay())+'.'+str(dlg.field_1.GetValue().GetMonth()+1)+'.'+str(dlg.field_1.GetValue().GetYear()))
	    ListPaySystem3(date0,date1,periodstr)
	dlg.Destroy()




#### --- Печатная форма Отчет "Журнал загрузок" (по CityPay)  ---
    def PaySystem4(self, evt):
	dlg = GetPeriod(self,-1,"Период", size=(350,200), style = wx.DEFAULT_DIALOG_STYLE)
	if dlg.ShowModal() == wx.ID_OK:
	    date0 = str(dlg.field_0.GetValue().GetYear())+'-' + str(dlg.field_0.GetValue().GetMonth()+1) +'-'+ str(dlg.field_0.GetValue().GetDay())
	    date1 = str(dlg.field_1.GetValue().GetYear())+'-' + str(dlg.field_1.GetValue().GetMonth()+1) +'-'+ str(dlg.field_1.GetValue().GetDay())
	    periodstr = str(str(dlg.field_0.GetValue().GetDay())+'.'+str(dlg.field_0.GetValue().GetMonth()+1)+'.'+str(dlg.field_0.GetValue().GetYear())+' - '+str(dlg.field_1.GetValue().GetDay())+'.'+str(dlg.field_1.GetValue().GetMonth()+1)+'.'+str(dlg.field_1.GetValue().GetYear()))
	    ListPaySystem4(date0,date1,periodstr)
	dlg.Destroy()




#### --- Печатная форма Отчет "Список MAC адресов" ----
    def	ListMAC(self,event):
	ListMac()




#### --- Печатная форма ресурсов сети ----
    def	PrintSourceNet(self,event):
	SourceNet()





#### --- Отчет: Список тарифных планов и услуг ---
    def TplanList(self,event):
	win = wx.MDIChildFrame(self, -1, 'Тарифные планы')
	canvas = TarifPlanList(win)
	win.Show(True)




#### --- Отчет: Вывод всего списка заявок по дому ---
    def TaskDom(self,event):
        dlg = ChoiseUlDom(self, -1, "Выбор улицы и дома", size=(350, 200),
                         style = wx.DEFAULT_DIALOG_STYLE
                         )
        dlg.Centre()

        val = dlg.ShowModal()
   
        if val == wx.ID_OK:
	    item = dlg.ctrl1.currentItem
	    UlDom = dlg.ctrl1.kod_record[item]
	    win = wx.MDIChildFrame(self, -1, 'Заявки по дому')
	    canvas = TaskListDom(win, UlDom)
	    win.Show(True)
        dlg.Destroy()



#### --- Отчет: Вывод списка незавершенных заявок  ---
    def TaskNoClose(self,event):
	win = wx.MDIChildFrame(self, -1, 'Незавершенные заявки')
	canvas = TaskListNoClose(win)
	win.Show(True)



#### --- Отчет: печатная форма незавершенных заявок ---
    def TaskNoClosePrint(self, evt):
	dlg = GetPeriod(self,-1,"Период", size=(350,200), style = wx.DEFAULT_DIALOG_STYLE)
	if dlg.ShowModal() == wx.ID_OK:
	    date0 = str(dlg.field_0.GetValue().GetYear())+'-' + str(dlg.field_0.GetValue().GetMonth()+1) +'-'+ str(dlg.field_0.GetValue().GetDay())
	    date1 = str(dlg.field_1.GetValue().GetYear())+'-' + str(dlg.field_1.GetValue().GetMonth()+1) +'-'+ str(dlg.field_1.GetValue().GetDay())
	    periodstr = str(str(dlg.field_0.GetValue().GetDay())+'.'+str(dlg.field_0.GetValue().GetMonth()+1)+'.'+str(dlg.field_0.GetValue().GetYear())+' - '+str(dlg.field_1.GetValue().GetDay())+'.'+str(dlg.field_1.GetValue().GetMonth()+1)+'.'+str(dlg.field_1.GetValue().GetYear()))
	    ListNoCloseTask(date0,date1,periodstr)
	dlg.Destroy()



#### --- Отчет: печатная форма заявок по подъезду ---
    def PrintTaskP(self, evt):
	dlg = ChoiseUlDomP(self,-1,"Период и подъезд", size=(350,200), style = wx.DEFAULT_DIALOG_STYLE)
	if dlg.ShowModal() == wx.ID_OK:

	    item = dlg.ctrl1.currentItem
	    UlDomP = dlg.ctrl1.kod_record[item]

	    date0 = str(dlg.field_0.GetValue().GetYear())+'-' + str(dlg.field_0.GetValue().GetMonth()+1) +'-'+ str(dlg.field_0.GetValue().GetDay())
	    date1 = str(dlg.field_1.GetValue().GetYear())+'-' + str(dlg.field_1.GetValue().GetMonth()+1) +'-'+ str(dlg.field_1.GetValue().GetDay())
	    periodstr = str(str(dlg.field_0.GetValue().GetDay())+'.'+str(dlg.field_0.GetValue().GetMonth()+1)+'.'+str(dlg.field_0.GetValue().GetYear())+' - '+str(dlg.field_1.GetValue().GetDay())+'.'+str(dlg.field_1.GetValue().GetMonth()+1)+'.'+str(dlg.field_1.GetValue().GetYear()))
	    RepTaskP(UlDomP,date0,date1,periodstr)

	dlg.Destroy()



##### --- Печатная форма Наряд-Заказ ---
    def Naryad_Zakaz(self,evt):
	dlg = ChoiseDateUlDom(self,-1,"Дата и дом", size=(350,200), style = wx.DEFAULT_DIALOG_STYLE)
	if dlg.ShowModal() == wx.ID_OK:
		item = dlg.ctrl1.currentItem
	    	UlDom = dlg.ctrl1.kod_record[item]
		date0 = str(dlg.field_0.GetValue().GetYear())+'-' + str(dlg.field_0.GetValue().GetMonth()+1) +'-'+ str(dlg.field_0.GetValue().GetDay())
		date_str = str(dlg.field_0.GetValue().GetDay())+'.'+ str(dlg.field_0.GetValue().GetMonth()+1) +'.'+ str(dlg.field_0.GetValue().GetYear())
		Naryad_Zakaz_PrintForm(UlDom.split(':')[0],UlDom.split(':')[1],date0,date_str)
	dlg.Destroy()




#### --- Отчет: печатная форма остатки на складе ---
    def PrintMrStore(self, evt):
	dlg = ChoiceStoreGroup(self,-1,"Остатки", size=(350,200), style = wx.DEFAULT_DIALOG_STYLE)
	if dlg.ShowModal() == wx.ID_OK:
	    store = dlg.field_0.GetValue()
	    group = dlg.field_1.GetValue()
	    if store == '' or group == '':
		ErrorValue(self)
	    else:
		RepMateStore(store,group)
	dlg.Destroy()


#### --- Учетные записи Internet доступа ---
    def ListLogin(self,event):
        dlg = Internet.LoginList(self, -1, "Учетные записи", size=(750, 400),
                         style = wx.DEFAULT_DIALOG_STYLE
                         )
        dlg.Centre()

        val = dlg.ShowModal()
   
        if val == wx.ID_OK:
	    item = dlg.ctrl1.currentItem
	    kodrec = dlg.ctrl1.kod_record[item]
	    ac = Internet.Account(self,-1,"INTERNET", pos=wx.DefaultPosition,
	    size=(600,490), style=wx.MINIMIZE_BOX|wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.FRAME_FLOAT_ON_PARENT, rec=kodrec)
	    ac.Centre()
	    ac.Show(True)
	    
        dlg.Destroy()



#### --- Новый тариф Internet трафик ---
    def	IntNewCost(self,event):
        dlg = Internet.NewTarif(self, -1, "Internet трафик", size=(350, 200),
                         style = wx.DEFAULT_DIALOG_STYLE
                         )
        dlg.Centre()


        val = dlg.ShowModal()
   
        if val == wx.ID_OK and Check.ReCheckPass(self) == 'OK':
	    if Internet.AddTarif(dlg.text0.GetValue(),dlg.text1.GetValue())!='OK':
		dlg2 = wx.MessageDialog(self,'Ошибка данных!','Ошибка',style=wx.OK)
		dlg2.ShowModal()
		dlg2.Destroy()
	    else :
		dlg3 = wx.MessageDialog(self,'Новый тариф добавлен','Сообщение',style=wx.OK)
		dlg3.ShowModal()
		dlg3.Destroy()

        dlg.Destroy()
	




#### --- Редактирование тарифов Internet трафика ---
    def	IntEditCost(self,event):
	dlg = wx.SingleChoiceDialog(self,'Internet тариф','Internet', ReadSpr.ReadIntTarif())    
	if dlg.ShowModal() == wx.ID_OK:
	    param = dlg.GetStringSelection()
    	    dlg2 = Internet.EditTarif(self, -1, "Internet трафик", size=(350, 200), style = wx.DEFAULT_DIALOG_STYLE, name_tarif=param)
    	    dlg2.Centre()
    	    val = dlg2.ShowModal()
	    if val == wx.ID_OK and Check.ReCheckPass(self) == 'OK':
		if Internet.UpdateTarif(dlg2.rec,dlg2.text0.GetValue(),dlg2.text1.GetValue())!='OK':
		    dlg3 = wx.MessageDialog(self,'Ошибка данных!','Ошибка',style=wx.OK)
		    dlg3.ShowModal()
		    dlg3.Destroy()
		else :
		    dlg4 = wx.MessageDialog(self,'Тариф изменен','Сообщение',style=wx.OK)
		    dlg4.ShowModal()
		    dlg4.Destroy()



	dlg.Destroy()    




#### --- Данные по серверу базы данных ---
    def ServerDb(self,evt):
	import ServerBD

        dlg = ServerBD.DialogBD(self, -1, "Сервер данных", size=(350, 200),
                         style = wx.DEFAULT_DIALOG_STYLE
                         )
        dlg.Centre()


        val = dlg.ShowModal()
   
        if val == wx.ID_OK:
		RWCfg.WriteValue('ServerDb', dlg.text0.GetValue())  
		RWCfg.WriteValue('NameDb', dlg.text1.GetValue())
		RWCfg.WriteValue('UserDb', dlg.text2.GetValue())


        dlg.Destroy()







#### --- Выгрузка данных из базы в файл --
    def ServerDbOut(self,event):
	dlg = wx.MessageDialog(self,"Создать резервную копию данных?","Резервирование",wx.YES_NO)
	if dlg.ShowModal() == wx.ID_YES:
	    d = time.localtime()
	    dd = str(d[0]) + str(d[1]) + str(d[2]) + str(d[3]) + str(d[4]) + str(d[5])
	    FILE_BACKUP = os.getcwd() + '/backup-data/backup' + dd + '.sql'
	    Backup(FILE_BACKUP)
	    FileSave(self,'Данные сохранены в файле:\nbackup-'+dd+'.sql')
	dlg.Destroy()




#### --- Загрузка данных в базу из резервной копии --
    def ServerDbIn(self,event):

	list_files = os.listdir('./backup-data')

	dlg = wx.SingleChoiceDialog(self,'Выбор файла с данными','Восстановление данных',list_files)
	if dlg.ShowModal() == wx.ID_OK and Check.ReCheckPass(self) == 'OK':
	    path = os.getcwd() + '/backup-data/' + dlg.GetStringSelection()
	    Restore(path)
	dlg.Destroy()




#### --- Выгрузить внешние коды (для платёжки) ----
    def Abon2Txt(self,event):
	dlg = wx.MessageDialog(self,"Выгрузить данные для \"Платёжки\"?","Выборка данных",wx.YES_NO)
	if dlg.ShowModal() == wx.ID_YES:
	    List2Txt(self)	    
        dlg.Destroy()
	
	
	
#### --- Загрузить внешние платежи ----
    def Txt2Base(self,event):

	list_files = os.listdir('pl-in')

	dlg = wx.SingleChoiceDialog(self,'Выбор файла с данными','Загрузка платежей',list_files)
	if dlg.ShowModal() == wx.ID_OK and Check.ReCheckPass(self) == 'OK':
	    path = 'pl-in/' + dlg.GetStringSelection()
	    res = txt2Base(self,path)
	    
	    if res == 'OK':
		LoadDone(self)
	    else:
	    
		### --- Вывод результата ---
	    	f = open(res,"r")
		msg = f.read()
		f.close()
	    	dlg2 = wx.lib.dialogs.ScrolledMessageDialog(self, msg, "Список ошибок загрузки")
		dlg2.ShowModal()
		dlg2.Destroy()

	dlg.Destroy()


	    
	    




#### --- Выгрузить данные для Бригантины ----
    def Abon2Brig(self,event):
	dlg = wx.MessageDialog(self,"Выгрузить данные для \"Бригантины\"?","Выборка данных",wx.YES_NO)
	if dlg.ShowModal() == wx.ID_YES:
	    Brig2Txt(self)	    
        dlg.Destroy()
	




#### --- Загрузить платежи от бригантины ----
    def Brig2Base(self,event):

	list_files = os.listdir('br-in')

	dlg = wx.SingleChoiceDialog(self,'Выбор файла с данными','Загрузка платежей',list_files)
	if dlg.ShowModal() == wx.ID_OK and Check.ReCheckPass(self) == 'OK':
	    path = 'br-in/' + dlg.GetStringSelection()
	    res = brig2Base(self,path)
	    
	    if res == 'OK':
		LoadDone(self)
	    else:
	    
		### --- Вывод результата ---
	    	f = open(res,"r")
		msg = f.read()
		f.close()
	    	dlg2 = wx.lib.dialogs.ScrolledMessageDialog(self, msg, "Список ошибок загрузки")
		dlg2.ShowModal()
		dlg2.Destroy()

	dlg.Destroy()



#### --- Выгрузить данные для Kass ----
    def Abon2Kass(self,event):
	dlg = wx.MessageDialog(self,"Выгрузить данные для \"КАСС\"?","Выборка данных",wx.YES_NO)
	if dlg.ShowModal() == wx.ID_YES:
	    Kass2Txt(self)	    
        dlg.Destroy()



#### --- Загрузить платежи от Касс ----
    def Kass2Base(self,event):

	list_files = os.listdir('kass-in')

	dlg = wx.SingleChoiceDialog(self,'Выбор файла с данными','Загрузка платежей',list_files)
	if dlg.ShowModal() == wx.ID_OK and Check.ReCheckPass(self) == 'OK':
	    path = 'kass-in/' + dlg.GetStringSelection()
	    res = kass2Base(self,path)
	    
	    if res == 'OK':
		LoadDone(self)
	    else:
	    
		### --- Вывод результата ---
	    	f = open(res,"r")
		msg = f.read()
		f.close()
	    	dlg2 = wx.lib.dialogs.ScrolledMessageDialog(self, msg, "Список ошибок загрузки")
		dlg2.ShowModal()
		dlg2.Destroy()

	dlg.Destroy()




#### --- Выгрузить данные для CityPay ----
    def Abon2CityPay(self,event):
	dlg = wx.MessageDialog(self,"Выгрузить данные для \"CityPay\"?","Выборка данных",wx.YES_NO)
	if dlg.ShowModal() == wx.ID_YES:
	    CityPay2Txt(self)	    
        dlg.Destroy()



#### --- Загрузить платежи от CityPay ----
    def CityPay2Base(self,event):

	list_files = os.listdir('cp-in')

	dlg = wx.SingleChoiceDialog(self,'Выбор файла с данными','Загрузка платежей',list_files)
	if dlg.ShowModal() == wx.ID_OK and Check.ReCheckPass(self) == 'OK':
	    path = 'cp-in/' + dlg.GetStringSelection()
	    res = citypay2Base(self,path)
	    
	    if res == 'OK':
		LoadDone(self)
	    else:
	    
		### --- Вывод результата ---
	    	f = open(res,"r")
		msg = f.read()
		f.close()
	    	dlg2 = wx.lib.dialogs.ScrolledMessageDialog(self, msg, "Список ошибок загрузки")
		dlg2.ShowModal()
		dlg2.Destroy()

	dlg.Destroy()




#### --- Вывод информации "О программе" ---
    def About(self,evt):
        dlg = About.PS(self)
	dlg.Centre()
	if dlg.ShowModal() == wx.ID_OK:
	    pass
	dlg.Destroy()





#### --- Вывод информации о изменениях версий ---
#    def Chver(self,evt):
#	f = open("chver.txt","r")
#	msg = f.read()
#	f.close()

#	dlg = wx.lib.dialogs.ScrolledMessageDialog(self, msg, "Изменения версий")
#	dlg.Centre()
#	dlg.ShowModal()




#### --- Ввод пароля ----
    def ChPass(self):


	RWCfg.WriteValue('PassDb', '')

		
        dlg = wx.TextEntryDialog(
                self, 'Введите пароль доступа',
                'Доступ','', style=wx.TE_PASSWORD|wx.OK|wx.CANCEL)

        if dlg.ShowModal() == wx.ID_OK:
	    RWCfg.WriteValue('PassDb', dlg.GetValue())
	    ### --- Проверка связи с сервером ---
	    Check.CheckServer(self)



#----------------------------------------------------------------------

if __name__ == '__main__':
    class MyApp(wx.App):
        def OnInit(self):
            wx.InitAllImageHandlers()
            MainFrame = MyParentFrame()
            MainFrame.Show(True)
	    MainFrame.ChPass()
            self.SetTopWindow(MainFrame)
            return True


    app = MyApp(False)
    app.MainLoop()



