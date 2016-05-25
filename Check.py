#coding:utf-8

""" Проверки """

import	wx
import	RWCfg
import	DBTools


#### --- Перепроверка пароля для критических операций ---
def ReCheckPass(self):
    dlg = wx.TextEntryDialog(self, 'Критические операции требуют\nпарольного подтверждения.','Ввод пароля', '', style=wx.TE_PASSWORD|wx.OK|wx.CANCEL)

    if dlg.ShowModal() == wx.ID_OK:
	if dlg.GetValue() == RWCfg.ReadValue('PassDb'):
	    return 'OK'

	else:
	    return ''
	    						
    dlg.Destroy()


    
#### --- Проверка связи с сервером, правильности пароля --- 
def CheckServer(self):
    db = DBTools.DBTools()
    if db.CheckConnectServer() != 'OK':
	dlg = wx.MessageDialog(self,'Не правильный пароль\nлибо нет связи с сервером.', 'Сообщение', style = wx.OK)
	dlg.ShowModal()
	dlg.Destroy()
    db.Destroy()
    