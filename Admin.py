#coding:utf-8
import  wx
import	psycopg
import	RWCfg
import	os




class DBA(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, 
            style=wx.DEFAULT_DIALOG_STYLE
            ):


        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)

        sizer = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, -1, "Административный доступ")
        sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)


        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)


        box = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self, -1, "Имя (Login):")
        box.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.text0 = wx.TextCtrl(self, -1, "", size=(80,-1))
        box.Add(self.text0, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)


        box = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self, -1, "Пароль:")
        box.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.text1 = wx.TextCtrl(self, -1, "", size=(80,-1), style=wx.TE_PASSWORD)
        box.Add(self.text1, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)



        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)        
        btn = wx.Button(self, wx.ID_OK)        
        btn.SetDefault()
        box.Add(btn, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        btn2 = wx.Button(self, wx.ID_CANCEL)
        box.Add(btn2, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)


### --- Подключение к базе данных ----
class RUN:
    def __init__(self,userdb,passwd):
	host_=RWCfg.ReadValue('ServerDb')
	port_=5432
	base_=RWCfg.ReadValue('NameDb')
	user_=userdb
	pass_=passwd


	self.cnx=psycopg.connect("host='%s' dbname='%s' user='%s' password='%s'" % (host_,base_,user_,pass_))



    def Destroy(self):
	self.cnx.close()
	

#### --- Выполнение скрипта ---
    def RunScript(self,path):
	f = open(path,'r')
	script = f.read()
	f.close()
   	cr=self.cnx.cursor()
	cr.execute(script)
	self.cnx.commit()
	result=cr.fetchone()
	cr.close()
	return str(result[0])

