#coding:utf-8
import  wx
import	RWCfg


class DialogBD(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, 
            style=wx.DEFAULT_DIALOG_STYLE
            ):


        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)

        sizer = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, -1, "Сервер базы данных")
        sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)


        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)


        box = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self, -1, "IP адрес:")
        box.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.text0 = wx.TextCtrl(self, -1, "", size=(80,-1))
        box.Add(self.text0, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
	self.text0.SetValue(RWCfg.ReadValue('ServerDb'))
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)


        box = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self, -1, "База данных:")
        box.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.text1 = wx.TextCtrl(self, -1, "", size=(80,-1))
        box.Add(self.text1, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
	self.text1.SetValue(RWCfg.ReadValue('NameDb'))
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)


        box = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self, -1, "Имя (логин):")
        box.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.text2 = wx.TextCtrl(self, -1, "", size=(80,-1))
        box.Add(self.text2, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
	self.text2.SetValue(RWCfg.ReadValue('UserDb'))
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

        btnsizer = wx.StdDialogButtonSizer()
        
#        if wx.Platform != "__WXMSW__":
#            btn = wx.ContextHelpButton(self)
#            btnsizer.AddButton(btn)


        btn = wx.Button(self, wx.ID_OK)
        
        btn.SetHelpText("Сохранить и завершить")
        btn.SetDefault()
        btnsizer.AddButton(btn)

        btn2 = wx.Button(self, wx.ID_CANCEL)
        btn2.SetHelpText("Выход без сохранения")
        btnsizer.AddButton(btn2)
        btnsizer.Realize()

        sizer.Add(btnsizer, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)


	    




