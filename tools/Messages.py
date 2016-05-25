#coding:utf-8
import  wx


def NotAccess(self):
    dlg = wx.MessageDialog(self, '    Нет доступа!     ','Сообщение', wx.OK)
    dlg.ShowModal()
    dlg.Destroy()
    


def SaveDone(self):
    dlg = wx.MessageDialog(self, '    Данные сохранены!     ','Сообщение', wx.OK)
    dlg.ShowModal()
    dlg.Destroy()
    


def ErrorData(self):
    dlg = wx.MessageDialog(self, '    Ошибка данных!     ','Сообщение', wx.OK)
    dlg.ShowModal()
    dlg.Destroy()
    
    
    
def FileSave(self,file):
    dlg = wx.MessageDialog(self, file,'Сообщение', wx.OK)
    dlg.ShowModal()
    dlg.Destroy()



def ErrorValue(self):
    dlg = wx.MessageDialog(self, '    Не задано значение!     ','Сообщение', wx.OK)
    dlg.ShowModal()
    dlg.Destroy()



def LoadDone(self):
    dlg = wx.MessageDialog(self, '    Данные загружены!     ','Сообщение', wx.OK)
    dlg.ShowModal()
    dlg.Destroy()
    