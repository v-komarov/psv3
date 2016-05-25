#!/usr/bin/env python
#coding:utf-8

""" Диалог о программе """

import	wx
import	wx.html



class PS(wx.Dialog):
    
    text = """
<html>
<body bgcolor="#ACAA60">
<center><table bgcolor="#45581" width="100%" cellspacing="0" cellpadding="0" border="1">
<tr>
    <td align="center"><h3>PS ver 3.0</h3></td>
</tr>
</table>
</center>        
<p>Основное назначение программы - учет приема платежей за оказанные услуги населению и автоматизация технической поддержки.
Программа <b>PS</b> как интерфейс к базе данных создана на языке <b>Python v2.4</b> с использованием библиотеки <b>wxPython v2.6.1.0</b>. Серверная часть выполнена на основе хранимых функций <b>PL/pgSQL</b> сервера баз данных <b>PostgreSQL</b>.

<p>Автор: <b>Vladimir Komarov</b> <a href=mailto:vak_200566@mail.ru>vak_200566@mail.ru</a></p>

<p>Вопросы технической поддержки по телефону: 8-905-972-24-26   
</p>
</body>
</html>
"""

    def __init__(self, parent):
	wx.Dialog.__init__(self, parent, -1, "О программе", size=(440,400))
	
	html = wx.html.HtmlWindow(self)
	html.SetPage(self.text)
	button = wx.Button(self, wx.ID_OK, "Закрыть")
	
	sizer = wx.BoxSizer(wx.VERTICAL)
	sizer.Add(html, 1, wx.EXPAND|wx.ALL, 5)
	sizer.Add(button, 0, wx.ALIGN_CENTER|wx.ALL, 5)
	
	self.SetSizer(sizer)
	self.Layout()
	
	
