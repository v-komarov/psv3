#coding:utf-8

import	wx
import	DBTools
import	string
import	ReadSpr
import	RWCfg
import	os
import	time
from	tools.StrHelpers	import	StrLimit


from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import ttfonts
from reportlab.lib import colors


from	task.RunSQL	import	GetListTaskRem
from	task.RunSQL	import	GetListTaskMon
from	task.RunSQL	import	GetListTaskDom



from	reportlab.platypus.tables	import	Table, TableStyle
from	reportlab.platypus.doctemplate	import	SimpleDocTemplate
from	reportlab.platypus.paragraph	import	Paragraph
from	reportlab.platypus		import	Frame, Spacer
from	reportlab.lib.styles		import	ParagraphStyle,getSampleStyleSheet




"""
    Для различных систем существуют различные просмотровщики PDF файлов
    универсального решения для этого пока не найдено,
    поэтому чтобы не привязвать исходные файлы к конкретному просмотровщику 
    храним вид/тип просмотровщика в cfg файле - название поля 'pdfview'
"""



### --- Просмотровщик PDF файлов ---
PDFVIEW = RWCfg.ReadValue('pdfview')





#### --- Подготовка данных для печатной формы списка заявок ремонт  ---
def RemList(date):



    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'
    c = canvas.Canvas(FILE_NAME)

    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)

    NewFont2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)


    date_str = string.split(date,'-')


    ### Первоначальные координаты 
    y = 280
    ### Шаг ###
    s = 5

    c.setFont("ArialBD", 14)
    c.drawCentredString(105*mm,y*mm, 'Заявки на ремонт')
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, 'на '+date_str[2]+'.'+date_str[1]+'.'+date_str[0]) 
    y = y - s*2 
    

    #### --- Линии более толстые ---
    c.setLineWidth(2)
    c.lines([
	    (10*mm,y*mm,200*mm,y*mm),
	    (10*mm,(y-s)*mm,200*mm,(y-s)*mm)
	    ])

    #### --- Линии обычной толщины ---
    c.setLineWidth(1)
    c.lines([
	    (30*mm,y*mm,30*mm,(y-s)*mm),
	    (60*mm,y*mm,60*mm,(y-s)*mm)
	    ])

    #### --- Заголовок таблицы ---
    c.drawCentredString(20*mm,(y-4)*mm, "Время") 
    c.drawCentredString(45*mm,(y-4)*mm, "Статус") 
    c.drawCentredString(125*mm,(y-4)*mm, "Адрес,Заявка") 
    y = y - s 


	
    for row in GetListTaskRem(date):
	t = row[3]
	status = row[7]
	address = row[10]+"  "+row[11]+"  "+row[12]+"  под. "+row[13]
	task = row[9]
	tel = row[14]
	person = str(row[16])
	c.setFont("Arial", 10)
	c.drawCentredString(20*mm,(y-4)*mm, t) 
	c.drawCentredString(45*mm,(y-4)*mm, status) 
	c.setFont("ArialBD", 10)
	### --- Адрес ---
	c.drawString(62*mm,(y-4)*mm, address) 
	y = y - s
	### --- Название заявки ---
	c.drawString(62*mm,(y-4)*mm, task) 
	y = y - s

	### --- Многострочное поле ---
	for row2 in StrLimit(row[18],70):
	    c.setFont("Arial", 10)
	    c.drawString(62*mm,(y-4)*mm, row2)
	    y = y - s
	    if y <= 10:
		c.showPage()
		y = 280


	c.setFont("Arial", 10)
	### --- Телефон ---
	c.drawString(62*mm,(y-4)*mm, "Телефон: "+tel) 
	y = y - s
	if y <= 10:
	    c.showPage()
	    y = 280


	c.setFont("Arial", 10)
	### --- Количество исполнителей ---
	c.drawString(62*mm,(y-4)*mm, "Количество исполнителей: "+person) 
	y = y - s
	if y <= 10:
	    c.showPage()
	    y = 280
	
#	c.setLineWidth(1)
#	c.lines([
#		(10*mm,y*mm,200*mm,y*mm),
#		(30*mm,y*mm,30*mm,(y-s)*mm),
#		(60*mm,y*mm,60*mm,(y-s)*mm)
#		])
	y = y - s


	if y <= 10:
	    c.showPage()
	    y = 280



    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])

    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")















#### --- Подготовка данных для печатной формы списка заявок монтаж  ---
def MonList(date):



    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'
    c = canvas.Canvas(FILE_NAME)

    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)

    NewFont2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)


    date_str = string.split(date,'-')


    ### Первоначальные координаты 
    y = 280
    ### Шаг ###
    s = 5

    c.setFont("ArialBD", 14)
    c.drawCentredString(105*mm,y*mm, 'Заявки на монтаж')
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, 'на '+date_str[2]+'.'+date_str[1]+'.'+date_str[0]) 
    y = y - s*2 
    

    #### --- Линии более толстые ---
    c.setLineWidth(2)
    c.lines([
	    (10*mm,y*mm,200*mm,y*mm),
	    (10*mm,(y-s)*mm,200*mm,(y-s)*mm)
	    ])

    #### --- Линии обычной толщины ---
    c.setLineWidth(1)
    c.lines([
	    (30*mm,y*mm,30*mm,(y-s)*mm),
	    (60*mm,y*mm,60*mm,(y-s)*mm)
	    ])

    #### --- Заголовок таблицы ---
    c.drawCentredString(20*mm,(y-4)*mm, "Время") 
    c.drawCentredString(45*mm,(y-4)*mm, "Статус") 
    c.drawCentredString(125*mm,(y-4)*mm, "Адрес,Заявка") 
    y = y - s 


	
    for row in GetListTaskMon(date):
	t = row[3]
	status = row[7]
	address = row[10]+"  "+row[11]+"  "+row[12]+"  под. "+row[13]
	task = row[9]
	tel = row[14]
	person = str(row[16])
	c.setFont("Arial", 10)
	c.drawCentredString(20*mm,(y-4)*mm, t) 
	c.drawCentredString(45*mm,(y-4)*mm, status) 
	c.setFont("ArialBD", 10)
	### --- Адрес ---
	c.drawString(62*mm,(y-4)*mm, address) 
	y = y - s
	### --- Название заявки ---
	c.drawString(62*mm,(y-4)*mm, task) 
	y = y - s

	### --- Многострочное поле ---
	for row2 in StrLimit(row[18],70):
	    c.setFont("Arial", 10)
	    c.drawString(62*mm,(y-4)*mm, row2)
	    y = y - s
	    if y <= 10:
		c.showPage()
		y = 280


	c.setFont("Arial", 10)
	### --- Телефон ---
	c.drawString(62*mm,(y-4)*mm, "Телефон: "+tel) 
	y = y - s
	if y <= 10:
	    c.showPage()
	    y = 280


	c.setFont("Arial", 10)
	### --- Количество исполнителей ---
	c.drawString(62*mm,(y-4)*mm, "Количество исполнителей: "+person) 
	y = y - s
	if y <= 10:
	    c.showPage()
	    y = 280
	
#	c.setLineWidth(1)
#	c.lines([
#		(10*mm,y*mm,200*mm,y*mm),
#		(30*mm,y*mm,30*mm,(y-s)*mm),
#		(60*mm,y*mm,60*mm,(y-s)*mm)
#		])
	y = y - s


	if y <= 10:
	    c.showPage()
	    y = 280



    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])

    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")




### --- Печатная форма для Наряд-Заказ ---
def Naryad_Zakaz_PrintForm(ul,dom,date,date_str):
	day_task = GetListTaskDom(ul,dom,date)

	data = [['№пп','Наименование\nработ','Подъезд','Квартира','Примечание'],
		]
	
	n = 1
	

	elements = []

	### --- Имя файла для вывода ---
	FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'

	Font = ttfonts.TTFont('Arial','font/arial.ttf')
	Font2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')

	pdfmetrics.registerFont(Font)
	pdfmetrics.registerFont(Font2)

	style = getSampleStyleSheet()
	style.add(ParagraphStyle(name='Disp',wordWrap=True,fontName='ArialBD',fontSize=12,spaceAfter=5*mm,spaceBefore=5*mm,alignment=2))
	style.add(ParagraphStyle(name='Naryad_Zakaz',wordWrap=True,fontName='ArialBD',fontSize=14,spaceAfter=5*mm,spaceBefore=5*mm,alignment=1))
	style.add(ParagraphStyle(name='DateDom',wordWrap=True,fontName='ArialBD',fontSize=12,spaceAfter=5*mm,spaceBefore=5*mm,alignment=1))
	style.add(ParagraphStyle(name='Table',wordWrap=True,fontName='Arial',fontSize=11,spaceAfter=1*mm,spaceBefore=1*mm,alignment=0))

	doc = SimpleDocTemplate(FILE_NAME,topMargin=10*mm,bottomMargin=10*mm,leftMargin=10*mm,rightMargin=10*mm)



	for item in day_task:
	    row = [n,Paragraph(item[9],style["Table"]),item[13],item[12],'']
	    n = n + 1
	    data.append(row)




	t=Table(data)
	t.setStyle([('FONTNAME',(0,0),(-1,0),'ArialBD'),
		    ('FONTSIZE',(0,0),(-1,0),11),
		    ('ALIGN',(0,0),(-1,0),'CENTER'),
		    ('VALIGN',(0,0),(-1,0),'MIDDLE'),
		    ('GRID',(0,0),(-1,-1),0.25,colors.black),
		    ('FONTNAME',(0,1),(-1,-1),'Arial'),
		    ('FONTSIZE',(0,1),(-1,-1),11),
		    ('ALIGN',(0,1),(0,-1),'CENTER'),
		    ('ALIGN',(1,1),(-1,-1),'LEFT'),
		    ('VALIGN',(0,1),(-1,-1),'TOP'),
		    ])


	elements.append(Paragraph('Наряд-Заказ',style["Naryad_Zakaz"]))
	elements.append(Paragraph('на выполнение работ по адресу: '+ul+' дом '+dom+' на '+date_str,style["DateDom"]))
	elements.append(t)
	elements.append(Paragraph('Диспетчер ООО "Артэкс"',style["Disp"]))

	doc.build(elements)
	os.system(PDFVIEW+" "+FILE_NAME+" &")


