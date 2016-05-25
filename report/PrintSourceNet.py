#coding:utf-8

import	wx
import	os
import	RWCfg
import	time


from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import ttfonts
from reportlab.lib import colors




"""
    Для различных систем существуют различные просмотровщики PDF файлов
    универсального решения для этого пока не найдено,
    поэтому чтобы не привязвать исходные файлы к конкретному просмотровщику 
    храним вид/тип просмотровщика в cfg файле - название поля 'pdfview'
"""

### --- Просмотровщик PDF файлов ---
PDFVIEW = RWCfg.ReadValue('pdfview')





#### --- Справка по ресурсам сети ---
def SourceNet():


    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)


    NewFont2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)



    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'
    c = canvas.Canvas(FILE_NAME)


    #### --- Раздел Internet ---
    c.setFont("Arial", 35)
    c.drawString(30*mm,270*mm, "Internet")
    c.setFont("Arial", 14)
    c.drawString(30*mm,265*mm, "VPN Серверы 172.17.204.21, 172.17.204.49")
    c.drawString(30*mm,255*mm, "Доступные ресурсы сети")
    c.setFont("Arial", 12)

    y = 250
    s = 5

    f = open('source_net.txt','r')
    for line in f.readlines():
	c.drawString(30*mm,y*mm, line[:-1])
	y = y - s	    

	if y <= 10:
	    c.showPage()
	    y = 280
	    c.setFont("Arial", 12)
	
    f.close()



    c.showPage()
    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")







