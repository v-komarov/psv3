#!/usr/bin/env python
#coding:utf-8
import	wx
import	mainwin





if __name__ == '__main__':
    class MyApp(wx.App):
        def OnInit(self):
            wx.InitAllImageHandlers()
            MainFrame = mainwin.MyParentFrame()
            MainFrame.Show(True)
	    MainFrame.ChPass()
            self.SetTopWindow(MainFrame)
            return True


    app = MyApp(False)
    app.MainLoop()



