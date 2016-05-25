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


from	abonent.RunSQL	import	GetAbonentData2
from	report.RunSQL	import	ShowAbonentAll
from	report.RunSQL	import	ShowAbonentContact
from	report.RunSQL	import	ShowServiceBalans
from	report.RunSQL	import	GetListBalans
from	report.RunSQL	import	ShowAbonentPart
from	report.RunSQL	import	ShowAbonentPartService
from	report.RunSQL	import	ShowAbonentPartServiceSum
from	report.RunSQL	import	ShowDomServiceSum
from	report.RunSQL	import	ShowServiceSum
from	report.RunSQL	import	ShowAbonentPartOb
from	report.RunSQL	import	ShowAbonentPartObService
from	report.RunSQL	import	ShowAbonentPartObU
from	report.RunSQL	import	ShowAbonentPartObServiceData
#from	report.RunSQL	import	ShowAbonentPart2
from	report.RunSQL	import	ShowAbonentPart3
from	report.RunSQL	import	ShowAbonentOff
from	report.RunSQL	import	RepPayAll	as	GetRepPayAll
from	report.RunSQL	import	RepPayAllService	as	GetRepPayAllService
from	report.RunSQL	import	RepPayAllSum	as	GetRepPayAllSum
from	report.RunSQL	import	RepPayOtherAll	as	GetRepPayOtherAll
from	report.RunSQL	import	RepPayOtherAllSum	as	GetRepPayOtherAllSum
from	report.RunSQL	import	RepPayKassa	as	GetRepPayKassa
from	report.RunSQL	import	RepPayKassaService	as	GetRepPayKassaService
from	report.RunSQL	import	RepPayKassaSum	as	GetRepPayKassaSum
from	report.RunSQL	import	GetNow
from	report.RunSQL	import	GetData4Check1
from	report.RunSQL	import	GetData4Check2
from	report.RunSQL	import	CheckIntLogin
from	report.RunSQL	import	ServiceBalans
from	report.RunSQL	import	GetListMac
from	report.RunSQL	import	GetListNoCloseTask2
from	report.RunSQL	import	GetListPaySystem
from	report.RunSQL	import	GetListPaySystemSum
from	report.RunSQL	import	GetListPaySystem2
from	report.RunSQL	import	GetListPaySystemSum2
from	report.RunSQL	import	GetListPaySystem3
from	report.RunSQL	import	GetListPaySystemSum3
from	report.RunSQL	import	GetListPaySystem4
from	report.RunSQL	import	GetListPaySystemSum4
from	report.RunSQL	import	GetDataAct


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



### --- Текст с информацией , где можно оплатить и когда (для объявлений должникам) ---
str2 = "Оплатить можно по адресу: ул.Молокова 17, отдельная дверь справа от 1-го подъезда. Мы работаем: Понедельник 9.00-19.00; Вторник-Четверг 9.00-18.00; Пятница 9.00-17.00. Администрация т.214-33-48 В случае задолженности 3 месяца и более предоставление услуг прекращается."





#### --- Подготовка данных для печатной формы списка абонентов ---
def AbonentList(UlDom):



    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'
    c = canvas.Canvas(FILE_NAME)

    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)

    NewFont2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)


    uldom = string.split(UlDom,':')


    ### Первоначальные координаты 
    y = 280
    ### Шаг ###
    s = 5

    c.setFont("ArialBD", 14)
    c.drawCentredString(105*mm,y*mm, 'Список абонентов '+uldom[0]+' '+uldom[1])
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, 'на '+GetNow() ) 
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
	    (60*mm,y*mm,60*mm,(y-s)*mm),
	    (90*mm,y*mm,90*mm,(y-s)*mm),
	    (160*mm,y*mm,160*mm,(y-s)*mm)
	    ])

    #### --- Заголовок таблицы ---
    c.drawCentredString(20*mm,(y-4)*mm, "№пп") 
    c.drawCentredString(45*mm,(y-4)*mm, "Подъезд") 
    c.drawCentredString(75*mm,(y-4)*mm, "Квартира") 
    c.drawCentredString(125*mm,(y-4)*mm, "Тарифный план") 
    c.drawCentredString(180*mm,(y-4)*mm, "Баланс") 
    y = y - s 


    ### --- Нумерация ---
    n = 1

    ### --- Общий баланс ---
    total = 0

	
    for row in ShowAbonentAll(UlDom):
	p = row[10]
	kv = row[3]
	tp = row[7]
	balans = row[4]
	c.setFont("Arial", 10)
	c.drawCentredString(20*mm,(y-4)*mm, str(n)) 
	c.drawCentredString(45*mm,(y-4)*mm, p) 
	c.drawCentredString(75*mm,(y-4)*mm, kv) 
	c.drawString(95*mm,(y-4)*mm, tp) 
	c.drawRightString(195*mm,(y-4)*mm, balans) 
	c.setLineWidth(1)
	c.lines([
		(10*mm,y*mm,200*mm,y*mm),
		(30*mm,y*mm,30*mm,(y-s)*mm),
		(60*mm,y*mm,60*mm,(y-s)*mm),
		(90*mm,y*mm,90*mm,(y-s)*mm),
		(160*mm,y*mm,160*mm,(y-s)*mm)
		])
	y = y -s
	n = n + 1

	total = total + eval(row[4])

	if y <= 10:
	    c.showPage()
	    y = 280



    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])
	    
    c.setFont("Arial", 10)
    c.drawRightString(195*mm,(y-4)*mm, "Общий баланс по дому: "+str(total)) 
    

    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")








#### --- Подготовка данных для печатной формы остатков по услугам ---
def AbonentServiceBalans(UlDom):


    db = DBTools.DBTools()



    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'
    c = canvas.Canvas(FILE_NAME)

    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)

    NewFont2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)


    uldom = string.split(UlDom,':')


    ### Первоначальные координаты 
    y = 280
    ### Шаг ###
    s = 5

    c.setFont("ArialBD", 14)
    c.drawCentredString(105*mm,y*mm, 'Остатки по услугам '+uldom[0]+' '+uldom[1])
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, 'на '+GetNow() ) 
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
	    (20*mm,y*mm,20*mm,(y-s)*mm),
	    (40*mm,y*mm,40*mm,(y-s)*mm),
	    (130*mm,y*mm,130*mm,(y-s)*mm),
	    (180*mm,y*mm,180*mm,(y-s)*mm)
	    ])

    #### --- Заголовок таблицы ---
    c.drawCentredString(15*mm,(y-4)*mm, "№пп") 
    c.drawCentredString(30*mm,(y-4)*mm, "Квартира") 
    c.drawCentredString(85*mm,(y-4)*mm, "Контакт") 
    c.drawCentredString(155*mm,(y-4)*mm, "Услуга") 
    c.drawCentredString(190*mm,(y-4)*mm, "Остаток") 
    y = y - s 


    ### --- Нумерация ---
    n = 1
	
    for row in ShowAbonentContact(db,UlDom):
	c.setFont("Arial", 10)
	c.drawCentredString(15*mm,(y-4)*mm, str(n)) 
	c.drawCentredString(30*mm,(y-4)*mm, row[1]) 
	c.drawString(41*mm,(y-4)*mm, row[2])

	service_l = ShowServiceBalans(db,row[0])

	if len(service_l) != 0:

	    for item in service_l:

		c.setFont("Arial", 10)
		c.drawString(131*mm,(y-4)*mm, item[0]) 
		c.drawRightString(200*mm,(y-4)*mm, item[1]) 
	    
		c.setLineWidth(1)
		c.lines([
			(20*mm,y*mm,20*mm,(y-s)*mm),
			(40*mm,y*mm,40*mm,(y-s)*mm),
			(130*mm,y*mm,130*mm,(y-s)*mm),
			(180*mm,y*mm,180*mm,(y-s)*mm),
			(130*mm,y*mm,200*mm,y*mm),
			])
	    
		y = y - s


	    c.setLineWidth(1)
	    c.lines([
		    (10*mm,y*mm,200*mm,y*mm),
		    ])

	else:

		c.setLineWidth(1)
		c.lines([
			(20*mm,y*mm,20*mm,(y-s)*mm),
			(40*mm,y*mm,40*mm,(y-s)*mm),
			(130*mm,y*mm,130*mm,(y-s)*mm),
			(180*mm,y*mm,180*mm,(y-s)*mm),
			(10*mm,(y-s)*mm,200*mm,(y-s)*mm),
			])

		y = y - s
	

	n = n + 1

	if y <= 30:
	    c.showPage()
	    y = 280



    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])


    db.Destroy()    

    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")










#### --- Подготовка данных для печатной формы баланс по дому ---
def BalansList():



    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'
    c = canvas.Canvas(FILE_NAME)

    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)

    NewFont2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)


    ### Первоначальные координаты 
    y = 280
    ### Шаг ###
    s = 5

    c.setFont("ArialBD", 14)
    c.drawCentredString(105*mm,y*mm, 'Баланс по дому')
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, 'на '+GetNow() ) 
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
	    (125*mm,y*mm,125*mm,(y-s)*mm),
	    (160*mm,y*mm,160*mm,(y-s)*mm)
	    ])

    #### --- Заголовок таблицы ---
    c.drawCentredString(20*mm,(y-4)*mm, "№пп") 
    c.drawCentredString(75*mm,(y-4)*mm, "Улица") 
    c.drawCentredString(143*mm,(y-4)*mm, "Дом") 
    c.drawCentredString(180*mm,(y-4)*mm, "Баланс") 
    y = y - s 


    ### --- Нумерация ---
    n = 1

    ### --- Общий баланс ---
    total = 0

	
    for row in GetListBalans():
	c.setFont("Arial", 10)
	c.drawCentredString(20*mm,(y-4)*mm, str(n)) 
	c.drawString(32*mm,(y-4)*mm, row[0]) 
	c.drawCentredString(143*mm,(y-4)*mm, row[1]) 
	c.drawRightString(195*mm,(y-4)*mm, str(row[2])) 
	c.setLineWidth(1)
	c.lines([
		(10*mm,y*mm,200*mm,y*mm),
		(30*mm,y*mm,30*mm,(y-s)*mm),
		(125*mm,y*mm,125*mm,(y-s)*mm),
		(160*mm,y*mm,160*mm,(y-s)*mm)
		])
	y = y -s
	n = n + 1

	total = total + row[2]

	if y <= 15:
	    c.showPage()
	    y = 280



    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])

    c.drawRightString(195*mm,(y-4)*mm, "Общий баланс: "+str(total)) 
    

    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")











#### --- Подготовка данных для печатной формы списка должников ---
def DolList(UlDom):



    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'
    c = canvas.Canvas(FILE_NAME)

    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)

    NewFont2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)


    uldom = string.split(UlDom,':')


    ### Первоначальные координаты 
    y = 280
    ### Шаг ###
    s = 5

    c.setFont("ArialBD", 14)
    c.drawCentredString(105*mm,y*mm, 'Список должников '+uldom[0]+' '+uldom[1])
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, 'на '+GetNow() ) 
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
	    (60*mm,y*mm,60*mm,(y-s)*mm),
	    (90*mm,y*mm,90*mm,(y-s)*mm),
	    (160*mm,y*mm,160*mm,(y-s)*mm),
	    (180*mm,y*mm,180*mm,(y-s)*mm)
	    ])

    #### --- Заголовок таблицы ---
    c.drawCentredString(20*mm,(y-4)*mm, "№пп") 
    c.drawCentredString(45*mm,(y-4)*mm, "Подъезд") 
    c.drawCentredString(75*mm,(y-4)*mm, "Квартира") 
    c.drawCentredString(125*mm,(y-4)*mm, "Услуга") 
    c.drawCentredString(170*mm,(y-4)*mm, "Долг") 
    c.drawCentredString(190*mm,(y-4)*mm, "Мес.") 
    y = y - s 


    ### --- Нумерация ---
    n = 1

    ### --- Общая сумма долга ---
    d = 0

	
    for row in ShowAbonentPart(UlDom):
	c.setFont("Arial", 10)
	c.drawCentredString(20*mm,(y-4)*mm, str(n)) 
	c.drawCentredString(45*mm,(y-4)*mm, row[15]) 
	c.drawCentredString(75*mm,(y-4)*mm, row[3]) 
	c.drawString(95*mm,(y-4)*mm, row[7]) 
	c.drawRightString(175*mm,(y-4)*mm, row[12]) 
	c.drawRightString(190*mm,(y-4)*mm, row[14]) 
	c.setLineWidth(1)
	c.lines([
		(10*mm,y*mm,200*mm,y*mm),
		(30*mm,y*mm,30*mm,(y-s)*mm),
		(60*mm,y*mm,60*mm,(y-s)*mm),
		(90*mm,y*mm,90*mm,(y-s)*mm),
		(160*mm,y*mm,160*mm,(y-s)*mm),
		(180*mm,y*mm,180*mm,(y-s)*mm)
		])
	y = y - s
	n = n + 1
	d = d + row[10]

	if y <= 10:
	    c.showPage()
	    y = 280


    c.setFont("Arial", 10)
    c.drawRightString(175*mm,(y-4)*mm, "Общий долг по дому: "+str(abs(d))) 
	

    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])

    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")








#### --- Подготовка данных для печатной формы списка должников с выбором услуги ---
def DolListService(UlDom,service):



    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'
    c = canvas.Canvas(FILE_NAME)

    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)

    NewFont2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)


    uldom = string.split(UlDom,':')


    ### Первоначальные координаты 
    y = 280
    ### Шаг ###
    s = 5

    c.setFont("ArialBD", 14)
    c.drawCentredString(105*mm,y*mm, 'Список должников '+uldom[0]+' '+uldom[1])
    y = y - s 

    if service != '':
    ### --- Если выбрана услуга ---
    
	c.drawCentredString(105*mm,y*mm, 'Услуга : '+service.encode("utf-8"))
	y = y - s 
	c.setFont("ArialBD", 10)
	c.drawCentredString(105*mm,y*mm, 'на '+GetNow() )
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
		(60*mm,y*mm,60*mm,(y-s)*mm),
		(90*mm,y*mm,90*mm,(y-s)*mm),
		(160*mm,y*mm,160*mm,(y-s)*mm)
		])

	#### --- Заголовок таблицы ---
	c.drawCentredString(20*mm,(y-4)*mm, "№") 
	c.drawCentredString(45*mm,(y-4)*mm, "Подъезд") 
	c.drawCentredString(75*mm,(y-4)*mm, "Квартира") 
	c.drawCentredString(125*mm,(y-4)*mm, "Долг") 
	c.drawCentredString(180*mm,(y-4)*mm, "Месяцев") 
	y = y - s 


	### --- Нумерация ---
	n = 1

	### --- Общая сумма долга ---
	d = 0

	
	for row in ShowAbonentPartService(UlDom,service):
	    c.setFont("Arial", 10)
	    c.drawCentredString(20*mm,(y-4)*mm, str(n)) 
	    c.drawCentredString(45*mm,(y-4)*mm, row[15]) 
	    c.drawCentredString(75*mm,(y-4)*mm, row[3]) 
	    c.drawRightString(135*mm,(y-4)*mm, row[12]) 
	    c.drawRightString(185*mm,(y-4)*mm, row[14]) 
	    c.setLineWidth(1)
	    c.lines([
		    (10*mm,y*mm,200*mm,y*mm),
		    (30*mm,y*mm,30*mm,(y-s)*mm),
		    (60*mm,y*mm,60*mm,(y-s)*mm),
		    (90*mm,y*mm,90*mm,(y-s)*mm),
		    (160*mm,y*mm,160*mm,(y-s)*mm)
		    ])
	    y = y -s
	    n = n + 1
	    d = d + abs(row[10])

	    if y <= 10:
		c.showPage()
		y = 280


	c.setFont("ArialBD", 10)
	c.drawRightString(75*mm,(y-4)*mm, "Общий долг по дому:") 
	c.drawRightString(135*mm,(y-4)*mm, str(d)) 
	

	c.lines([
		(10*mm,y*mm,200*mm,y*mm)
		])

    ### --- Если услуга не выбрана, - делаем по всем услугам ---
    else:

	c.setFont("ArialBD", 10)
	c.drawCentredString(105*mm,y*mm, 'на '+GetNow() )
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
		(60*mm,y*mm,60*mm,(y-s)*mm),
		(90*mm,y*mm,90*mm,(y-s)*mm),
		(160*mm,y*mm,160*mm,(y-s)*mm),
		(180*mm,y*mm,180*mm,(y-s)*mm)
		])

	#### --- Заголовок таблицы ---
	c.drawCentredString(20*mm,(y-4)*mm, "№пп") 
	c.drawCentredString(45*mm,(y-4)*mm, "Подъезд") 
	c.drawCentredString(75*mm,(y-4)*mm, "Квартира") 
	c.drawCentredString(125*mm,(y-4)*mm, "Услуга") 
	c.drawCentredString(170*mm,(y-4)*mm, "Долг") 
	c.drawCentredString(190*mm,(y-4)*mm, "Мес.") 
	y = y - s 


	### --- Нумерация ---
	n = 1

	### --- Общая сумма долга ---
	d = 0

	
	for row in ShowAbonentPart(UlDom):
	    c.setFont("Arial", 10)
	    c.drawCentredString(20*mm,(y-4)*mm, str(n)) 
	    c.drawCentredString(45*mm,(y-4)*mm, row[15]) 
	    c.drawCentredString(75*mm,(y-4)*mm, row[3]) 
	    c.drawString(95*mm,(y-4)*mm, row[7]) 
	    c.drawRightString(175*mm,(y-4)*mm, row[12]) 
	    c.drawRightString(190*mm,(y-4)*mm, row[14]) 
	    c.setLineWidth(1)
	    c.lines([
		    (10*mm,y*mm,200*mm,y*mm),
		    (30*mm,y*mm,30*mm,(y-s)*mm),
		    (60*mm,y*mm,60*mm,(y-s)*mm),
		    (90*mm,y*mm,90*mm,(y-s)*mm),
		    (160*mm,y*mm,160*mm,(y-s)*mm),
		    (180*mm,y*mm,180*mm,(y-s)*mm)
		    ])
	    y = y -s
	    n = n + 1

	    if y <= 10:
		c.showPage()
		y = 280


	c.lines([
		(10*mm,y*mm,200*mm,y*mm)
		])



	for row in ShowAbonentPartServiceSum(UlDom):
	    c.setFont("ArialBD", 10)
	    c.drawString(95*mm,(y-4)*mm, row[0]) 
	    c.drawRightString(175*mm,(y-4)*mm, str(row[1])) 
	    y = y - s
	    d = d + row[1]

	    if y <= 10:
		c.showPage()
		y = 280


	

	c.lines([
		(10*mm,y*mm,200*mm,y*mm)
		])


	c.setFont("ArialBD", 10)
	c.drawString(95*mm,(y-4)*mm, "ВСЕГО :") 
	c.drawRightString(175*mm,(y-4)*mm, str(d)) 



    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")










#### --- Подготовка данных для печатной формы долгов (по услугам) ---
def DolDomService():



    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'
    c = canvas.Canvas(FILE_NAME)

    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)

    NewFont2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)


    ### Первоначальные координаты 
    y = 280
    ### Шаг ###
    s = 5

    c.setFont("ArialBD", 14)
    c.drawCentredString(105*mm,y*mm, 'Долги по домам и услугам')
    y = y - s 

    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, 'на '+GetNow() )
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
	    (90*mm,y*mm,90*mm,(y-s)*mm),
	    (110*mm,y*mm,110*mm,(y-s)*mm),
	    (170*mm,y*mm,170*mm,(y-s)*mm)
	    ])

    #### --- Заголовок таблицы ---
    c.drawCentredString(50*mm,(y-4)*mm, "Улица") 
    c.drawCentredString(100*mm,(y-4)*mm, "Дом") 
    c.drawCentredString(140*mm,(y-4)*mm, "Услуга") 
    c.drawCentredString(185*mm,(y-4)*mm, "Долг") 
    y = y - s 


    ### --- Общая сумма долга ---
    d = 0

	
    for row in ShowDomServiceSum():
	c.setFont("Arial", 10)
	c.drawString(20*mm,(y-4)*mm, row[0]) 
	c.drawCentredString(100*mm,(y-4)*mm, row[1]) 
	c.drawString(115*mm,(y-4)*mm, row[2]) 
	c.drawRightString(195*mm,(y-4)*mm, str(row[3])) 
	c.setLineWidth(1)
	c.lines([
		(10*mm,y*mm,200*mm,y*mm),
		(90*mm,y*mm,90*mm,(y-s)*mm),
		(110*mm,y*mm,110*mm,(y-s)*mm),
		(170*mm,y*mm,170*mm,(y-s)*mm)
		])
	y = y - s

	if y <= 10:
	    c.showPage()
	    y = 280


    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])



    for row in ShowServiceSum():
	c.setFont("ArialBD", 10)
	c.drawCentredString(100*mm,(y-4)*mm, "ИТОГО") 
	c.drawString(115*mm,(y-4)*mm, row[0]) 
	c.drawRightString(195*mm,(y-4)*mm, str(row[1])) 
	y = y - s
	d = d + row[1]

	if y <= 10:
	    c.showPage()
	    y = 280


	

    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])


    c.setFont("ArialBD", 10)
    c.drawString(115*mm,(y-4)*mm, "ВСЕГО :") 
    c.drawRightString(195*mm,(y-4)*mm, str(d)) 



    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")









#### --- Подготовка данных для печатной формы списка _отключенных_ должников ---
def DolListOff():


    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'
    c = canvas.Canvas(FILE_NAME)

    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)

    NewFont2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)




    ### Первоначальные координаты 
    y = 280
    ### Шаг ###
    s = 5

    c.setFont("ArialBD", 14)
    c.drawCentredString(105*mm,y*mm, 'Отключенные абоненты')
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, 'на ' +GetNow()) 
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
	    (120*mm,y*mm,120*mm,(y-s)*mm),
	    (180*mm,y*mm,180*mm,(y-s)*mm)
	    ])

    #### --- Заголовок таблицы ---
    c.drawCentredString(20*mm,(y-4)*mm, "№пп") 
    c.drawCentredString(75*mm,(y-4)*mm, "Адрес") 
    c.drawCentredString(150*mm,(y-4)*mm, "Услуга") 
    c.drawCentredString(190*mm,(y-4)*mm, "Остаток") 
    y = y - s 


    ### --- Нумерация ---
    n = 1

	
    for row in ShowAbonentOff():
	ul = row[0]
	dom = row[1]
	kv = row[2]
	ser = row[3]
	dolg = str(row[4])
	c.setFont("Arial", 10)
	c.drawCentredString(20*mm,(y-4)*mm, str(n)) 
	c.drawString(35*mm,(y-4)*mm, ul+' '+dom+'-'+kv) 
	c.drawString(125*mm,(y-4)*mm, ser) 
	c.drawRightString(195*mm,(y-4)*mm, dolg) 
	c.setLineWidth(1)
	c.lines([
		(10*mm,y*mm,200*mm,y*mm),
		(30*mm,y*mm,30*mm,(y-s)*mm),
		(120*mm,y*mm,120*mm,(y-s)*mm),
		(180*mm,y*mm,180*mm,(y-s)*mm)
		])
	y = y - s
	n = n + 1

	if y <= 10:
	    c.showPage()
	    y = 280
	



    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])
	

    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")








#### --- Подготовка данных для печатной формы "Поступления" ---
def RepPayAll(date0,date1,periodstr):


    db = DBTools.DBTools()


    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'
    c = canvas.Canvas(FILE_NAME)

    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)

    NewFont2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)




    ### Первоначальные координаты 
    y = 280
    ### Шаг ###
    s = 5

    c.setFont("ArialBD", 14)
    c.drawCentredString(105*mm,y*mm, 'Поступления')
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, 'за период '+str(periodstr)) 
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
	    (70*mm,y*mm,70*mm,(y-s)*mm),
	    (90*mm,y*mm,90*mm,(y-s)*mm),
	    (110*mm,y*mm,110*mm,(y-s)*mm),
	    (150*mm,y*mm,150*mm,(y-s)*mm),
	    (180*mm,y*mm,180*mm,(y-s)*mm)
	    ])

    #### --- Заголовок таблицы ---
    c.drawCentredString(20*mm,(y-4)*mm, "Дата") 
    c.drawCentredString(50*mm,(y-4)*mm, "Улица") 
    c.drawCentredString(80*mm,(y-4)*mm, "Дом") 
    c.drawCentredString(100*mm,(y-4)*mm, "Квартира") 
    c.drawCentredString(130*mm,(y-4)*mm, "Услуга") 
    c.drawCentredString(165*mm,(y-4)*mm, "Касса") 
    c.drawCentredString(190*mm,(y-4)*mm, "Сумма") 
    y = y - s 


    ### --- Итоги ---
    itog = 0
    itog2 = 0


    result = GetRepPayAll(db,date0,date1)
	
    for row in result:
	c.setFont("Arial", 10)
	c.drawCentredString(20*mm,(y-4)*mm, row[4]) 
	c.drawString(31*mm,(y-4)*mm, row[0]) 
	c.drawCentredString(80*mm,(y-4)*mm, row[1]) 
	c.drawCentredString(100*mm,(y-4)*mm, row[2]) 
	c.drawString(111*mm,(y-4)*mm, row[5]) 
	c.drawString(151*mm,(y-4)*mm, row[6]) 
	c.drawRightString(195*mm,(y-4)*mm, row[8]) 
	c.setLineWidth(1)
	c.lines([
		(10*mm,y*mm,200*mm,y*mm),
		(30*mm,y*mm,30*mm,(y-s)*mm),
		(70*mm,y*mm,70*mm,(y-s)*mm),
		(90*mm,y*mm,90*mm,(y-s)*mm),
		(110*mm,y*mm,110*mm,(y-s)*mm),
		(150*mm,y*mm,150*mm,(y-s)*mm),
		(180*mm,y*mm,180*mm,(y-s)*mm)
		])
	y = y - s

	if y <= 10:
	    c.showPage()
	    y = 280

    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])

    y = y - s

    ### --- Итоги по услугам ---
    for row in GetRepPayAllService(db,date0,date1):
	c.setFont("ArialBD", 10)
	c.drawString(111*mm,y*mm, row[0]) 
	c.drawRightString(195*mm,y*mm, row[1]) 
	y = y - s
	if y <= 10:
	    c.showPage()
	    y = 280
    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])




### --- Общие Итоги ---
    if len(result) != 0:
	itog_str = GetRepPayAllSum(db,date0,date1)
	itog = eval(itog_str)
	y = y - s
	c.setFont("ArialBD", 10)
	c.drawString(111*mm,(y)*mm, 'ИТОГО') 
	c.drawRightString(195*mm,(y)*mm, itog_str) 

	y = y - s*2
	

    if y <= 70:
	c.showPage()
	y = 280
	
	

    result2 = GetRepPayOtherAll(db,date0,date1)

    if len(result2) != 0:

	c.setFont("ArialBD", 14)
	c.drawCentredString(105*mm,y*mm, 'Поступления прочих платежей')
	y = y - s 
	c.setFont("ArialBD", 10)
	c.drawCentredString(105*mm,y*mm, 'за период '+str(periodstr)) 
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
		(70*mm,y*mm,70*mm,(y-s)*mm),
		(90*mm,y*mm,90*mm,(y-s)*mm),
		(110*mm,y*mm,110*mm,(y-s)*mm),
		(150*mm,y*mm,150*mm,(y-s)*mm),
		(180*mm,y*mm,180*mm,(y-s)*mm)
		])

	#### --- Заголовок таблицы ---
	c.drawCentredString(20*mm,(y-4)*mm, "Дата") 
	c.drawCentredString(50*mm,(y-4)*mm, "Улица") 
	c.drawCentredString(80*mm,(y-4)*mm, "Дом") 
	c.drawCentredString(100*mm,(y-4)*mm, "Квартира") 
	c.drawCentredString(130*mm,(y-4)*mm, "Назначение") 
	c.drawCentredString(165*mm,(y-4)*mm, "Касса") 
	c.drawCentredString(190*mm,(y-4)*mm, "Сумма") 
	y = y - s 





	#### --- Для дополнительных платежей ---
	for row in result2:
	    c.setFont("Arial", 10)
	    c.drawCentredString(20*mm,(y-4)*mm, row[4]) 
	    c.drawString(31*mm,(y-4)*mm, row[0]) 
	    c.drawCentredString(80*mm,(y-4)*mm, row[1]) 
	    c.drawCentredString(100*mm,(y-4)*mm, row[2]) 
	    c.drawString(111*mm,(y-4)*mm, row[5]) 
	    c.drawString(151*mm,(y-4)*mm, u"КАССА") 
	    c.drawRightString(195*mm,(y-4)*mm, row[7]) 
	    c.setLineWidth(1)
	    c.lines([
		    (10*mm,y*mm,200*mm,y*mm),
		    (30*mm,y*mm,30*mm,(y-s)*mm),
		    (70*mm,y*mm,70*mm,(y-s)*mm),
		    (90*mm,y*mm,90*mm,(y-s)*mm),
		    (110*mm,y*mm,110*mm,(y-s)*mm),
		    (150*mm,y*mm,150*mm,(y-s)*mm),
		    (180*mm,y*mm,180*mm,(y-s)*mm)
		    ])
	    y = y - s

	    if y <= 10:
		c.showPage()
		y = 280

	c.lines([
		(10*mm,y*mm,200*mm,y*mm)
		])

    ### --- Общие Итоги ---
	if len(result2) != 0:
	    itog2_str = GetRepPayOtherAllSum(db,date0,date1)
	    itog2 = eval(itog2_str)
	    y = y - s
	    c.setFont("ArialBD", 10)
	    c.drawString(111*mm,(y)*mm, 'ИТОГО') 
	    c.drawRightString(195*mm,(y)*mm, itog2_str) 

	y = y - s

	c.drawString(111*mm,(y)*mm, 'ВСЕГО') 
	c.drawRightString(195*mm,(y)*mm, str(itog+itog2)) 
	






    db.Destroy()

    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")












#### --- Подготовка данных для печатной формы "Поступления" с выбором по кассе ---
def RepPayKassa(date0,date1,periodstr,kassa):



    db = DBTools.DBTools()


    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'
    c = canvas.Canvas(FILE_NAME)

    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)

    NewFont2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)




    ### Первоначальные координаты 
    y = 280
    ### Шаг ###
    s = 5

    c.setFont("ArialBD", 14)
    c.drawCentredString(105*mm,y*mm, 'Поступления')
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, 'за период '+str(periodstr)) 
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, u'Касса: '+kassa) 
    y = y - s 
    c.setFont("ArialBD", 8)
    if kassa == u'КАССА':
	c.drawCentredString(105*mm,y*mm, '(с учётом прочих платежей)') 
    else:
	c.drawCentredString(105*mm,y*mm, '(без учёта прочих платежей)') 
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
	    (70*mm,y*mm,70*mm,(y-s)*mm),
	    (90*mm,y*mm,90*mm,(y-s)*mm),
	    (110*mm,y*mm,110*mm,(y-s)*mm),
	    (150*mm,y*mm,150*mm,(y-s)*mm),
	    (180*mm,y*mm,180*mm,(y-s)*mm)
	    ])

    #### --- Заголовок таблицы ---
    c.setFont("ArialBD", 10)
    c.drawCentredString(20*mm,(y-4)*mm, "Дата") 
    c.drawCentredString(50*mm,(y-4)*mm, "Улица") 
    c.drawCentredString(80*mm,(y-4)*mm, "Дом") 
    c.drawCentredString(100*mm,(y-4)*mm, "Квартира") 
    c.drawCentredString(130*mm,(y-4)*mm, "Услуга") 
    c.drawCentredString(165*mm,(y-4)*mm, "Касса") 
    c.drawCentredString(190*mm,(y-4)*mm, "Сумма") 
    y = y - s 


    ### --- Итоги ---
    itog = 0
    itog2 = 0

    result = GetRepPayKassa(db,date0,date1,kassa)
	
    for row in result:
	c.setFont("Arial", 10)
	c.drawCentredString(20*mm,(y-4)*mm, row[4]) 
	c.drawString(31*mm,(y-4)*mm, row[0]) 
	c.drawCentredString(80*mm,(y-4)*mm, row[1]) 
	c.drawCentredString(100*mm,(y-4)*mm, row[2]) 
	c.drawString(111*mm,(y-4)*mm, row[5]) 
	c.drawString(151*mm,(y-4)*mm, row[6]) 
	c.drawRightString(195*mm,(y-4)*mm, row[8]) 
	c.setLineWidth(1)
	c.lines([
		(10*mm,y*mm,200*mm,y*mm),
		(30*mm,y*mm,30*mm,(y-s)*mm),
		(70*mm,y*mm,70*mm,(y-s)*mm),
		(90*mm,y*mm,90*mm,(y-s)*mm),
		(110*mm,y*mm,110*mm,(y-s)*mm),
		(150*mm,y*mm,150*mm,(y-s)*mm),
		(180*mm,y*mm,180*mm,(y-s)*mm)
		])
	y = y - s

	if y <= 10:
	    c.showPage()
	    y = 280

    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])
    y = y - s

### --- Итоги по услугам ---
    for row in GetRepPayKassaService(db,date0,date1,kassa):
	c.setFont("ArialBD", 10)
	c.drawString(111*mm,y*mm, row[0]) 
	c.drawRightString(195*mm,y*mm, row[1]) 
	y = y - s
	if y <= 10:
	    c.showPage()
	    y = 280
    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])


### --- Общие итоги ---
    if len(result) != 0:
	itog_str = GetRepPayKassaSum(db,date0,date1,kassa)
	itog = eval(itog_str)
	y = y - s
	c.setFont("ArialBD", 10)
	c.drawString(111*mm,(y)*mm, 'ИТОГО') 
	c.drawRightString(195*mm,(y)*mm, itog_str) 


	y = y - s*2
	

    if y <= 70:
	c.showPage()
	y = 280



    result2 = GetRepPayOtherAll(db,date0,date1)

    if len(result2) != 0 and kassa == u'КАССА':

	c.setFont("ArialBD", 14)
	c.drawCentredString(105*mm,y*mm, 'Поступления прочих платежей')
	y = y - s 
	c.setFont("ArialBD", 10)
	c.drawCentredString(105*mm,y*mm, 'за период '+str(periodstr)) 
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
		(70*mm,y*mm,70*mm,(y-s)*mm),
		(90*mm,y*mm,90*mm,(y-s)*mm),
		(110*mm,y*mm,110*mm,(y-s)*mm),
		(150*mm,y*mm,150*mm,(y-s)*mm),
		(180*mm,y*mm,180*mm,(y-s)*mm)
		])

	#### --- Заголовок таблицы ---
	c.drawCentredString(20*mm,(y-4)*mm, "Дата") 
	c.drawCentredString(50*mm,(y-4)*mm, "Улица") 
	c.drawCentredString(80*mm,(y-4)*mm, "Дом") 
	c.drawCentredString(100*mm,(y-4)*mm, "Квартира") 
	c.drawCentredString(130*mm,(y-4)*mm, "Назначение") 
	c.drawCentredString(165*mm,(y-4)*mm, "Касса") 
	c.drawCentredString(190*mm,(y-4)*mm, "Сумма") 
	y = y - s 





	#### --- Для дополнительных платежей ---
	for row in result2:
	    c.setFont("Arial", 10)
	    c.drawCentredString(20*mm,(y-4)*mm, row[4]) 
	    c.drawString(31*mm,(y-4)*mm, row[0]) 
	    c.drawCentredString(80*mm,(y-4)*mm, row[1]) 
	    c.drawCentredString(100*mm,(y-4)*mm, row[2]) 
	    c.drawString(111*mm,(y-4)*mm, row[5]) 
	    c.drawString(151*mm,(y-4)*mm, u"КАССА") 
	    c.drawRightString(195*mm,(y-4)*mm, row[7]) 
	    c.setLineWidth(1)
	    c.lines([
		    (10*mm,y*mm,200*mm,y*mm),
		    (30*mm,y*mm,30*mm,(y-s)*mm),
		    (70*mm,y*mm,70*mm,(y-s)*mm),
		    (90*mm,y*mm,90*mm,(y-s)*mm),
		    (110*mm,y*mm,110*mm,(y-s)*mm),
		    (150*mm,y*mm,150*mm,(y-s)*mm),
		    (180*mm,y*mm,180*mm,(y-s)*mm)
		    ])
	    y = y - s

	    if y <= 10:
		c.showPage()
		y = 280

	c.lines([
		(10*mm,y*mm,200*mm,y*mm)
		])

    ### --- Общие Итоги ---
	if len(result2) != 0:
	    itog2_str = GetRepPayOtherAllSum(db,date0,date1)
	    itog2 = eval(itog2_str)
	    y = y - s
	    c.setFont("ArialBD", 10)
	    c.drawString(111*mm,(y)*mm, 'ИТОГО') 
	    c.drawRightString(195*mm,(y)*mm, itog2_str) 

	y = y - s

	c.drawString(111*mm,(y)*mm, 'ВСЕГО') 
	c.drawRightString(195*mm,(y)*mm, "%.2f" % (itog+itog2)) 
	




    db.Destroy()

    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")








#### --- Подготовка данных для печатной формы Карточки абонента ---
def CartAbonent(rec):


    date=str(wx.DateTime.Today().GetDay())+'.'+str(wx.DateTime.Today().GetMonth()+1)+'.'+str(wx.DateTime.Today().GetYear())



    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)


    NewFont2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)



    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'


    ### --- Флаг присутствия INTERNET услуги ---
    internet_ok = CheckIntLogin(rec)

    r = GetAbonentData2(rec)    

    c = canvas.Canvas(FILE_NAME)
    c.setFont("Arial", 40)
    c.drawString(30*mm,270*mm,"Карточка абонента")
    c.setFont("Arial", 20)
    c.drawString(30*mm,255*mm,"Адрес: "+r[1]+' '+r[2]+'-'+r[3])
    c.drawString(30*mm,245*mm,"Телефон: "+r[5])
    c.setFont("ArialBD", 10)
    c.drawString(30*mm,235*mm,"По состоянию на "+date)
    c.drawString(33*mm,225*mm,"Услуги")
    c.drawString(103*mm,225*mm,"Баланс (руб.)")

    c.drawString(30*mm,185*mm, "Номер лицевого счета")
    c.drawString(100*mm,185*mm, r[9])
    

    c.setFont("Arial", 10)
    c.drawString(30*mm,180*mm, "Оплата принимается по адресу:")
    c.drawString(30*mm,175*mm, "1. ул.Молокова 17, отдельная дверь справа от 1-го подъезда")
    c.drawString(30*mm,170*mm, "2. В пунктах автоматизированного приема платежей ПЛАТЕЖКА")
    c.drawString(30*mm,165*mm, "Информация о ваших платежах на сайте http://www.telesputnik.net")

#    c.drawString(30*mm,165*mm, "Мы работаем: Понедельник-Пятница 9.00-18.00 перерыв 13.00-14.00,")
#    c.drawString(30*mm,160*mm, "Суббота 10.00-13.00. Администрация т.54-02-61")


#    #### --- линии ----
#    c.lines([
#    	(30*mm,265*mm,195*mm,265*mm),
#    	(30*mm,266*mm,195*mm,266*mm),
#    	(30*mm,230*mm,150*mm,230*mm),
#    	(30*mm,220*mm,150*mm,220*mm),
#    	(30*mm,215*mm,150*mm,215*mm),
#    	(30*mm,210*mm,150*mm,210*mm),
#    	(30*mm,205*mm,150*mm,205*mm),
#    	(30*mm,200*mm,150*mm,200*mm),
#    	(30*mm,230*mm,30*mm,200*mm),
#    	(150*mm,230*mm,150*mm,200*mm),
#    	(100*mm,230*mm,100*mm,200*mm)
#    	])

    #### --- Более широкие линии ---
#    c.setLineWidth(2)    
#    c.lines([
#    	(30*mm,230*mm,150*mm,230*mm),
#    	(30*mm,220*mm,150*mm,220*mm),
#    	(30*mm,205*mm,150*mm,205*mm),
#    	(30*mm,200*mm,150*mm,200*mm),
#    	(30*mm,230*mm,30*mm,200*mm),
#    	(150*mm,230*mm,150*mm,200*mm),
#    	(100*mm,230*mm,100*mm,200*mm)
#    	])



#### --- Информация по балансам лицевых счетов ---
    y = 220 ## Начальное занчение по вертикали
    c.setFont("Arial", 10)
    for b in ServiceBalans(rec):
	c.drawString(33*mm,y*mm,b[7])
	c.drawString(103*mm,y*mm,str(b[11]))
	y = y - 5

    c.setFont("ArialBD", 10)
    c.drawString(33*mm,y*mm,"Общий баланс")
    c.drawString(103*mm,y*mm,r[4])    





#### --- Вывод параметров доступа к Internet (логин и пароль) ---
    if internet_ok==1:

	#### --- Горизонтальные линии ----
	c.setLineWidth(1)    
	c.lines([
    	(30*mm,135*mm,195*mm,135*mm),
    	(30*mm,134*mm,195*mm,134*mm)
    	])

	#### --- Получение логина и пароля активной учетной записи Internet ---
	lp = ReadSpr.GetIntLoginPasswd(rec)


	#### --- Раздел Internet ---
	c.setFont("Arial", 35)
	c.drawString(30*mm,140*mm, "Internet")
	c.setFont("Arial", 14)
	c.drawString(30*mm,125*mm, "VPN Серверы 172.17.204.21, 172.17.204.49")
	c.drawString(30*mm,120*mm, "Имя пользователя: "+lp[0])
	c.drawString(30*mm,115*mm, "Пароль: "+lp[1])
	c.drawString(30*mm,105*mm, "Техническая поддержка (офис) : т.214-33-48")
	c.drawString(30*mm,95*mm, "Доступные ресурсы сети")
	c.setFont("Arial", 12)

	y = 85
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







#### --- Подготовка данных для печатной формы копии чека ---
def CheckAbonent(rec,address,lsp,adv=0):

    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'


    date = str(wx.DateTime.Today().GetDay())+'.'+str(wx.DateTime.Today().GetMonth()+1)+'.'+str(wx.DateTime.Today().GetYear())



    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)

    NewFont2 = ttfonts.TTFont('ArialB','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)



    c = canvas.Canvas(FILE_NAME)

    ### --- Всю картинку сдвигаем вверх на 2мм---
    c.translate(0*mm,57*mm)


    #### --- Линии нормальной толщины ----
    c.lines([
	    (7*mm,220*mm,205*mm,220*mm),
	    (7*mm,150*mm,205*mm,150*mm),
	    (40*mm,220*mm,40*mm,150*mm),
	    (205*mm,235*mm,205*mm,150*mm),
	    (7*mm,231*mm,205*mm,231*mm),
	    (7*mm,235*mm,205*mm,235*mm),
	    (40*mm,200*mm,205*mm,200*mm),
	    (40*mm,195*mm,205*mm,195*mm),
	    (40*mm,190*mm,205*mm,190*mm),
	    (70*mm,195*mm,70*mm,150*mm),
	    (70*mm,185*mm,205*mm,185*mm),
	    (70*mm,180*mm,205*mm,180*mm),
	    (70*mm,175*mm,205*mm,175*mm),
	    (70*mm,170*mm,205*mm,170*mm),
	    (70*mm,165*mm,205*mm,165*mm),
	    (70*mm,160*mm,205*mm,160*mm),
	    (70*mm,155*mm,205*mm,155*mm),
	    (150*mm,195*mm,150*mm,155*mm),
	    (175*mm,195*mm,175*mm,150*mm)	
	    ])


    #### --- Линии более толстые ---
    c.setLineWidth(4)
    c.lines([
	    (7*mm,220*mm,205*mm,220*mm),
	    (7*mm,150*mm,205*mm,150*mm)
	    ])

    c.setLineWidth(2)
    c.lines([
	    (40*mm,195*mm,205*mm,195*mm),
	    (40*mm,190*mm,205*mm,190*mm),
	    (70*mm,155*mm,205*mm,155*mm)		
	    ])


    #### --- Заголовки  (основная форма) ---
    c.setFont("Arial", 12)
    c.drawString(43*mm,196*mm,"Адрес:")
    c.drawString(43*mm,191*mm,"Дата")
    c.drawString(43*mm,180*mm,date)
    c.drawString(73*mm,191*mm,"Вид услуги")
    c.drawString(153*mm,191*mm,"Тариф")
    c.drawString(178*mm,191*mm,"Всего")
    c.drawString(153*mm,151*mm,"Итого")


    #### --- Надписи (основная форма) ---
    c.setFont("Arial", 14)
    c.drawRightString(200*mm,215*mm,"Копия чека")
    c.drawString(45*mm,215*mm,"Лицевой счет N "+lsp+" Телеспутник")


    c.setFont("Arial", 10)
    c.drawCentredString(90*mm,210*mm,"Оплачивать в платежных системах:")
    c.setFont("ArialB", 10)
    c.drawCentredString(150*mm,210*mm,"'ПЛАТЁЖКА' и 'КАССервис'")

    c.setFont("Arial", 10)
    c.drawCentredString(122*mm,207*mm,"кабельное ТВ через клавишу 'Кабельное TV Телеспутник' или 'Цифровое TV Телеспутник'")
    c.drawCentredString(122*mm,204*mm,"после ввода лицевого счета сверяйте свой адрес. Проценты не удерживаются.")
    c.drawCentredString(122*mm,201*mm,"ул.Молокова 17, отдельная дверь справа от 1-го подъезда. телефон 214-33-48")


    c.drawCentredString(23*mm,210*mm,"Часы работы")
    c.drawCentredString(23*mm,205*mm,"Понедельник:")
    c.drawCentredString(23*mm,202*mm,"9:00 - 19:00")
#    c.drawCentredString(23*mm,199*mm,"14:00 - 19:00")
    c.drawCentredString(23*mm,194*mm,"Вторник-Четверг:")
    c.drawCentredString(23*mm,191*mm,"9:00 - 18:00")
#    c.drawCentredString(23*mm,188*mm,"14:00 - 18:00")
    c.drawCentredString(23*mm,183*mm,"Пятница:")
    c.drawCentredString(23*mm,180*mm,"9:00 - 17:00")
#    c.drawCentredString(23*mm,177*mm,"14:00 - 17:00")
#    c.drawCentredString(23*mm,172*mm,"Суббота:")
#    c.drawCentredString(23*mm,169*mm,"10:00 - 13:00")

    c.drawCentredString(23*mm,170*mm,"ООО Артэкс")

    c.drawCentredString(23*mm,160*mm,"Кассир:")

    ## --- Отрывная часть ---
    c.setFont("ArialB", 8)
    c.drawString(10*mm,232*mm,"л.счёт: "+lsp)
    c.drawString(40*mm,232*mm,"адрес: "+address)
    c.drawRightString(200*mm,232*mm,date)
    
    ## --- Многострочная часть по платежам отрывной части ---
    str_info = ''


    c.setFont("ArialB", 10)
    #### --- Вставка данных ---
    c.drawString(60*mm,196*mm,address)
    c.drawRightString(203*mm,196*mm,"")
    c.setFont("Arial", 10)

    
    #### --- Итого первоначально ---
    itogo = 0.00

    y2 = 186
    ### -- Платежи по услугам обслуживания (которые есть в тарифном плане) ---
    for row in GetData4Check1(rec):
	c.drawString(73*mm,y2*mm, row[1])
	c.drawString(153*mm,y2*mm, str(row[2]))
	c.drawString(178*mm,y2*mm, str(row[3]))

	### --- Строка для отрывной части ---
	str_info = str_info + row[1]+":("+str(row[2])+")"+str(row[3])+"; "
	
	itogo = itogo + row[3]
	
	y2 = y2 - 5

    ### -- Платежи по прочим услугам (которых нет в тарифном плане) ---
    for row in GetData4Check2(rec):
	c.drawString(73*mm,y2*mm, row[1])
	c.drawString(153*mm,y2*mm, '-')
	c.drawString(178*mm,y2*mm, str(row[2]))
	
	itogo = itogo + row[2]

	### --- Строка для отрывной части ---
	str_info = str_info + row[1]+":"+str(row[2])+"; "

	y2 = y2 - 5

	
    
    c.drawString(178*mm,151*mm,str(itogo)+' руб.')

    ### --- Строка для отрывной части ---
    str_info = str_info + "Итого:"+str(itogo)+' руб.'

    ### --- Вставка многострочной отрывной части ---
    y = 227
    c.setFont("Arial", 8)
    for row in StrLimit(str_info, 130):
	c.drawString(10*mm,y*mm, row)
	y = y - 3



    #### --- Если есть признак добавить объявление - добавляем новый лист ---
    if adv == 1:
	c.showPage()
	c.setFont("ArialB", 10)
#	c.drawString(20*mm,210*mm,"ООО ИТ-Сервис занимается разработкой и внедрением программ для Linux")
#	c.drawString(20*mm,207*mm,"на основе составляющих с открытым исходным кодом по следующим направлениям:")
#	c.drawString(25*mm,204*mm,"- Системы учёта платежей и оказания услуг;")
#	c.drawString(25*mm,201*mm,"- Системы учёта товара;")
#	c.drawString(25*mm,198*mm,"- Системы управления отношениями с клиентами.")
#	c.drawString(20*mm,195*mm,"Телефон: 8-905-972-24-26")
	c.drawString(20*mm,185*mm,"Телеспутник информирует:")
	c.drawString(25*mm,182*mm,"- Работает система платежей через 'Платежка'")
	c.drawString(25*mm,179*mm,"- Кабельное через клавишу 'кабельное'->'Телеспутник'")
	c.drawString(25*mm,176*mm,"- Домофоны через клавишу 'ЖКХ'->'Телеспутник-домофоны'")
	c.drawString(20*mm,173*mm,"Тарифы:")
	c.drawString(25*mm,170*mm,"- Домофоны 25 руб.")
	c.drawString(25*mm,167*mm,"- Кабельное TV 90 руб.")
	c.drawString(25*mm,164*mm,"- Социальный пакет TV 50 руб.")




    c.showPage()
    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")





##### --- Вывод в печатную форму объявлений должникам ---
def Messages4Abonents(UlDom):

	elements = []

	### --- Имя файла для вывода ---
	FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'

	Font = ttfonts.TTFont('Arial','font/arial.ttf')
	Font2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
	
	pdfmetrics.registerFont(Font)
	pdfmetrics.registerFont(Font2)

	style = getSampleStyleSheet()
	style.add(ParagraphStyle(name='MyStyle',wordWrap=True,fontName='Arial',fontSize=12,spaceAfter=5*mm,spaceBefore=5*mm,alignment=4))


	doc = SimpleDocTemplate(FILE_NAME,topMargin=10*mm,bottomMargin=10*mm,leftMargin=10*mm,rightMargin=10*mm)



	### --- Сегодняшняя дата ---
	date = GetNow()
	
	db = DBTools.DBTools()
	
    	for row in ShowAbonentPartOb(db,UlDom):
	    str1 = '<font face="ArialBD">Адрес: улица '+row[1]+' номер дома '+row[2]+' квартира '+row[3]+' подъезд № '+row[5] + '</font> Ваш общий баланс на '+ date + ' составляет ' +row[4] + ' руб. в том числе по услугам : '

    	    for row1 in ShowAbonentPart3(db,row[0]):
		str1 = str1 + '  ' + row1[0] + ' : ' + str(row1[1]) + ' руб.; '


	    elements.append(Paragraph(str1+' '+str2,style["MyStyle"]))


					
	db.Destroy()


	doc.build(elements)
	os.system(PDFVIEW+" "+FILE_NAME+" &")










##### --- Вывод в печатную форму объявлений должникам (с выбором по услуге, кол-ву месяцев долга, минимальной сумме долга) ---
def Messages4Abonents2(UlDom,ser,month,min_sum):

	elements = []

	### --- Имя файла для вывода ---
	FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'

	Font = ttfonts.TTFont('Arial','font/arial.ttf')
	Font2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')

	pdfmetrics.registerFont(Font)
	pdfmetrics.registerFont(Font2)

	style = getSampleStyleSheet()
	style.add(ParagraphStyle(name='MyStyle',wordWrap=True,fontName='Arial',fontSize=12,spaceAfter=5*mm,spaceBefore=5*mm,alignment=4))


	doc = SimpleDocTemplate(FILE_NAME,topMargin=10*mm,bottomMargin=10*mm,leftMargin=10*mm,rightMargin=10*mm)


	### --- Сегодняшняя дата ---
	date = GetNow()
	
	db = DBTools.DBTools()
	
    	for row in ShowAbonentPartObService(db,UlDom,ser,month,min_sum):
	
	    str1 = '<font face="ArialBD">Адрес: улица '+row[0]+' номер дома '+row[1]+' квартира '+row[2]+' подъезд № '+row[3]+'</font> Ваш баланс по услуге '+row[4] +' на '+ date + ' составляет ' +row[5] + ' руб.'

	    elements.append(Paragraph(str1+' '+str2,style["MyStyle"]))


	db.Destroy()



	doc.build(elements)
	os.system(PDFVIEW+" "+FILE_NAME+" &")










##### --- Вывод в печатную форму объявлений должникам (с выбором по услуге, кол-ву месяцев долга, минимальной сумме долга) ---
def Messages4Abonents3(UlDom,list):

	elements = []

	### --- Имя файла для вывода ---
	FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'

	Font = ttfonts.TTFont('Arial','font/arial.ttf')
	Font2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')

	pdfmetrics.registerFont(Font)
	pdfmetrics.registerFont(Font2)

	style = getSampleStyleSheet()
	style.add(ParagraphStyle(name='MyStyle',wordWrap=True,fontName='Arial',fontSize=12,spaceAfter=5*mm,spaceBefore=5*mm,alignment=4))

	doc = SimpleDocTemplate(FILE_NAME,topMargin=10*mm,bottomMargin=10*mm,leftMargin=10*mm,rightMargin=10*mm)

	### --- Сегодняшняя дата ---
	date = GetNow()
	
	db = DBTools.DBTools()

	### --- Формирование списка должников по дому ---
	for row in ShowAbonentPartObU(db,UlDom):

	    ### --- Информация о долгах по услугам ---
	    service_data = []

	    ### --- Строка с данными по услугам первоначально ---
	    str_service_data = 'Долг по услугам: '

	    for item in list:

		t = ShowAbonentPartObServiceData(db,row[0],item[0],item[1],item[2])
    		if t!='None':
		    service_data.append(t)

	    if len(service_data)!=0:
	
		str1 = '<font face="ArialBD">Адрес: улица '+row[1]+' номер дома '+row[2]+' квартира '+row[3]+'</font>'

		### --- Информация по услугам ---
    		for sd in service_data:
		    str_service_data = str_service_data + sd[0] + ': ' + str(sd[1]) + ' руб.; '
		str1 = str1 + ' ' + str_service_data

		elements.append(Paragraph(str1+' '+str2,style["MyStyle"]))
		
					
	db.Destroy()


	doc.build(elements)
	os.system(PDFVIEW+" "+FILE_NAME+" &")









##### --- Вывод в печатную форму списка MAC адресов ---
def ListMac():

	
    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'
    c = canvas.Canvas(FILE_NAME)

    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)

    NewFont2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)




    ### Первоначальные координаты 
    y = 280
    ### Шаг ###
    s = 5

    c.setFont("ArialBD", 14)
    c.drawCentredString(105*mm,y*mm, 'Список MAC адресов')
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, 'на ' +GetNow()) 
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
	    (100*mm,y*mm,100*mm,(y-s)*mm),
	    (130*mm,y*mm,130*mm,(y-s)*mm)
	    ])

    #### --- Заголовок таблицы ---
    c.drawCentredString(20*mm,(y-4)*mm, "№пп") 
    c.drawCentredString(65*mm,(y-4)*mm, "Адрес") 
    c.drawCentredString(115*mm,(y-4)*mm, "Тип") 
    c.drawCentredString(165*mm,(y-4)*mm, "MAC") 
    y = y - s 


    ### --- Нумерация ---
    n = 1

	
    for row in GetListMac():
	address = row[0]
	if row[1] == 1:
	    tip = 'INTERNET'
	elif row[1] == 2:
	    tip = 'IPTV'
	mac = row[2]
	c.setFont("Arial", 10)
	c.drawCentredString(20*mm,(y-4)*mm, str(n)) 
	c.drawString(35*mm,(y-4)*mm, address) 
	c.drawString(105*mm,(y-4)*mm, tip) 
	c.drawString(135*mm,(y-4)*mm, mac) 
	c.setLineWidth(1)
	c.lines([
		(30*mm,y*mm,30*mm,(y-s)*mm),
		(100*mm,y*mm,100*mm,(y-s)*mm),
		(130*mm,y*mm,130*mm,(y-s)*mm),
		(10*mm,y*mm,200*mm,y*mm)
		])
	y = y - s
	n = n + 1

	if y <= 10:
	    c.showPage()
	    y = 280
	



    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])
	

    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")












##### --- Вывод в печатную форму не завершенных заявок ---
def ListNoCloseTask(date0,date1,periodstr):

	
    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'
    c = canvas.Canvas(FILE_NAME)

    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)

    NewFont2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)




    ### Первоначальные координаты 
    y = 280
    ### Шаг ###
    s = 5

    c.setFont("ArialBD", 14)
    c.drawCentredString(105*mm,y*mm, 'Список не завершённых заявок')
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, 'за период ' +periodstr) 
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
	    (25*mm,y*mm,25*mm,(y-s)*mm),
	    (45*mm,y*mm,45*mm,(y-s)*mm),
	    (90*mm,y*mm,90*mm,(y-s)*mm),
	    (165*mm,y*mm,165*mm,(y-s)*mm),
	    (180*mm,y*mm,180*mm,(y-s)*mm)
	    ])

    #### --- Заголовок таблицы ---
    c.drawCentredString(17*mm,(y-4)*mm, "№пп") 
    c.drawCentredString(35*mm,(y-4)*mm, "Дата") 
    c.drawCentredString(68*mm,(y-4)*mm, "Адрес") 
    c.drawCentredString(128*mm,(y-4)*mm, "Заявка") 
    c.drawCentredString(172*mm,(y-4)*mm, "Тип") 
    c.drawCentredString(190*mm,(y-4)*mm, "Статус") 
    y = y - s 


    ### --- Нумерация ---
    n = 1

	
    for row in GetListNoCloseTask2(date0,date1):
	c.setFont("Arial", 8)
	c.drawCentredString(17*mm,(y-4)*mm, str(n)) 
	c.drawCentredString(35*mm,(y-4)*mm, row[2]) 
	c.drawString(46*mm,(y-4)*mm, row[10]+' '+row[11]+'-'+row[12] +' п' + row[13])
	c.drawString(91*mm,(y-4)*mm, row[9]) 
	if row[8]==1:
	    c.drawString(166*mm,(y-4)*mm, u'РЕМОНТ') 
	elif row[8]==2:    
	    c.drawString(166*mm,(y-4)*mm, u'МОНТАЖ')
	else: 
	    c.drawString(166*mm,(y-4)*mm, '')
	c.drawString(181*mm,(y-4)*mm, row[7]) 
	c.setLineWidth(1)
	c.lines([
		(25*mm,y*mm,25*mm,(y-s)*mm),
		(45*mm,y*mm,45*mm,(y-s)*mm),
		(90*mm,y*mm,90*mm,(y-s)*mm),
		(165*mm,y*mm,165*mm,(y-s)*mm),
		(180*mm,y*mm,180*mm,(y-s)*mm),
		(10*mm,y*mm,200*mm,y*mm)
		])
	y = y - s
	n = n + 1

	if y <= 10:
	    c.showPage()
	    y = 280
	



    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])
	

    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")








##### --- Вывод в печатную форму Внешних поступлений ---
def ListPaySystem(date0,date1,periodstr):

	
    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'
    c = canvas.Canvas(FILE_NAME)

    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)

    NewFont2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)




    ### Первоначальные координаты 
    y = 280
    ### Шаг ###
    s = 5

    c.setFont("ArialBD", 14)
    c.drawCentredString(105*mm,y*mm, 'Журнал загрузок платежей')
    y = y - s 
    c.drawCentredString(105*mm,y*mm, '\"ПЛАТЁЖКА\"')
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, 'за период ' +periodstr) 
    y = y - s*2 
    

    #### --- Линии более толстые ---
    c.setLineWidth(2)
    c.lines([
	    (10*mm,y*mm,200*mm,y*mm),
	    (10*mm,(y-s*2)*mm,200*mm,(y-s*2)*mm)
	    ])

    #### --- Линии обычной толщины ---
    c.setLineWidth(1)
    c.lines([
	    (30*mm,y*mm,30*mm,(y-s*2)*mm),
	    (50*mm,y*mm,50*mm,(y-s*2)*mm),
	    (70*mm,y*mm,70*mm,(y-s*2)*mm),
	    (110*mm,y*mm,110*mm,(y-s*2)*mm),
	    (130*mm,y*mm,130*mm,(y-s*2)*mm)
	    ])

    #### --- Заголовок таблицы ---
    c.drawCentredString(20*mm,(y-5)*mm, "Дата") 
    c.drawCentredString(20*mm,(y-8)*mm, "платежа") 
    c.drawCentredString(40*mm,(y-5)*mm, "Дата") 
    c.drawCentredString(40*mm,(y-8)*mm, "загрузки") 
    c.drawCentredString(60*mm,(y-5)*mm, "Номер") 
    c.drawCentredString(60*mm,(y-8)*mm, "лиц.счёта") 
    c.drawCentredString(90*mm,(y-5)*mm, "Название") 
    c.drawCentredString(90*mm,(y-8)*mm, "услуги") 
    c.drawCentredString(120*mm,(y-5)*mm, "Сумма") 
    c.drawCentredString(120*mm,(y-8)*mm, "платежа") 
    c.drawCentredString(165*mm,(y-5)*mm, "Ошибка") 
    c.drawCentredString(165*mm,(y-8)*mm, "(если есть)") 

    y = y - s*2

    result = GetListPaySystem(date0,date1)
	
    for row in result:
	c.setFont("Arial", 10)

	if row[9] == 1:
	    c.setFillColorRGB(0,0,0)
	else:
	    c.setFillColorRGB(1,0,0)
	    
	c.drawCentredString(20*mm,(y-4)*mm, row[2]) 
	c.drawCentredString(40*mm,(y-4)*mm, row[3]) 
	c.drawCentredString(60*mm,(y-4)*mm, row[4]) 
	c.drawString(71*mm,(y-4)*mm, row[5])
	c.drawCentredString(120*mm,(y-4)*mm, row[7]) 
	c.drawString(131*mm,(y-4)*mm, row[8])
	c.setLineWidth(1)
	c.lines([
		(30*mm,y*mm,30*mm,(y-s)*mm),
		(50*mm,y*mm,50*mm,(y-s)*mm),
		(70*mm,y*mm,70*mm,(y-s)*mm),
		(110*mm,y*mm,110*mm,(y-s)*mm),
		(130*mm,y*mm,130*mm,(y-s)*mm),
		(10*mm,y*mm,200*mm,y*mm)
		])
	y = y - s

	if y <= 10:
	    c.showPage()
	    y = 280
	



    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])

    c.setFillColorRGB(0,0,0)
    
    if len(result) != 0:	
	c.setFont("ArialBD", 10)
	c.drawString(71*mm,(y-4)*mm, 'ВСЕГО')
	c.drawCentredString(120*mm,(y-4)*mm, GetListPaySystemSum(date0,date1)) 

	

    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")







##### --- Вывод в печатную форму Внешних поступлений (по Бригантине) ---
def ListPaySystem2(date0,date1,periodstr):

	
    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'
    c = canvas.Canvas(FILE_NAME)

    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)

    NewFont2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)




    ### Первоначальные координаты 
    y = 280
    ### Шаг ###
    s = 5

    c.setFont("ArialBD", 14)
    c.drawCentredString(105*mm,y*mm, 'Журнал загрузок платежей')
    y = y - s 
    c.drawCentredString(105*mm,y*mm, '\"БРИГАНТИНА\"')
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, 'за период ' +periodstr) 
    y = y - s*2 
    

    #### --- Линии более толстые ---
    c.setLineWidth(2)
    c.lines([
	    (10*mm,y*mm,200*mm,y*mm),
	    (10*mm,(y-s*2)*mm,200*mm,(y-s*2)*mm)
	    ])

    #### --- Линии обычной толщины ---
    c.setLineWidth(1)
    c.lines([
	    (30*mm,y*mm,30*mm,(y-s*2)*mm),
	    (50*mm,y*mm,50*mm,(y-s*2)*mm),
	    (110*mm,y*mm,110*mm,(y-s*2)*mm),
	    (130*mm,y*mm,130*mm,(y-s*2)*mm)
	    ])

    #### --- Заголовок таблицы ---
    c.drawCentredString(20*mm,(y-5)*mm, "Дата") 
    c.drawCentredString(20*mm,(y-8)*mm, "платежа") 
    c.drawCentredString(40*mm,(y-5)*mm, "Дата") 
    c.drawCentredString(40*mm,(y-8)*mm, "загрузки") 
    c.drawCentredString(80*mm,(y-7)*mm, "Адрес") 
    c.drawCentredString(120*mm,(y-5)*mm, "Сумма") 
    c.drawCentredString(120*mm,(y-8)*mm, "платежа") 
    c.drawCentredString(165*mm,(y-5)*mm, "Ошибка") 
    c.drawCentredString(165*mm,(y-8)*mm, "(если есть)") 

    y = y - s*2

    result = GetListPaySystem2(date0,date1)
	
    for row in result:
	c.setFont("Arial", 10)

	if row[5] == 1:
	    c.setFillColorRGB(0,0,0)
	else:
	    c.setFillColorRGB(1,0,0)
	    
	c.drawCentredString(20*mm,(y-4)*mm, row[0]) 
	c.drawCentredString(40*mm,(y-4)*mm, row[1]) 
	c.drawString(51*mm,(y-4)*mm, row[2]) 
	c.drawCentredString(120*mm,(y-4)*mm, "%.2f" % row[3]) 
	c.drawString(131*mm,(y-4)*mm, row[4])
	c.setLineWidth(1)
	c.lines([
		(30*mm,y*mm,30*mm,(y-s)*mm),
		(50*mm,y*mm,50*mm,(y-s)*mm),
		(110*mm,y*mm,110*mm,(y-s)*mm),
		(130*mm,y*mm,130*mm,(y-s)*mm),
		(10*mm,y*mm,200*mm,y*mm)
		])
	y = y - s

	if y <= 10:
	    c.showPage()
	    y = 280
	



    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])

    c.setFillColorRGB(0,0,0)
    
    if len(result) != 0:	
	c.setFont("ArialBD", 10)
	c.drawString(51*mm,(y-4)*mm, 'ВСЕГО')
	c.drawCentredString(120*mm,(y-4)*mm, GetListPaySystemSum2(date0,date1)) 

	

    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")






##### --- Вывод в печатную форму Внешних поступлений (по Касс) ---
def ListPaySystem3(date0,date1,periodstr):

	
    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'
    c = canvas.Canvas(FILE_NAME)

    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)

    NewFont2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)




    ### Первоначальные координаты 
    y = 280
    ### Шаг ###
    s = 5

    c.setFont("ArialBD", 14)
    c.drawCentredString(105*mm,y*mm, 'Журнал загрузок платежей')
    y = y - s 
    c.drawCentredString(105*mm,y*mm, '\"КАСС\"')
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, 'за период ' +periodstr) 
    y = y - s*2 
    

    #### --- Линии более толстые ---
    c.setLineWidth(2)
    c.lines([
	    (10*mm,y*mm,200*mm,y*mm),
	    (10*mm,(y-s*2)*mm,200*mm,(y-s*2)*mm)
	    ])

    #### --- Линии обычной толщины ---
    c.setLineWidth(1)
    c.lines([
	    (30*mm,y*mm,30*mm,(y-s*2)*mm),
	    (50*mm,y*mm,50*mm,(y-s*2)*mm),
	    (70*mm,y*mm,70*mm,(y-s*2)*mm),
	    (110*mm,y*mm,110*mm,(y-s*2)*mm),
	    (130*mm,y*mm,130*mm,(y-s*2)*mm)
	    ])

    #### --- Заголовок таблицы ---
    c.drawCentredString(20*mm,(y-5)*mm, "Дата") 
    c.drawCentredString(20*mm,(y-8)*mm, "платежа") 
    c.drawCentredString(40*mm,(y-5)*mm, "Дата") 
    c.drawCentredString(40*mm,(y-8)*mm, "загрузки") 
    c.drawCentredString(60*mm,(y-5)*mm, "Номер") 
    c.drawCentredString(60*mm,(y-8)*mm, "лиц.счёта") 
    c.drawCentredString(90*mm,(y-5)*mm, "Название") 
    c.drawCentredString(90*mm,(y-8)*mm, "услуги") 
    c.drawCentredString(120*mm,(y-5)*mm, "Сумма") 
    c.drawCentredString(120*mm,(y-8)*mm, "платежа") 
    c.drawCentredString(165*mm,(y-5)*mm, "Ошибка") 
    c.drawCentredString(165*mm,(y-8)*mm, "(если есть)") 

    y = y - s*2

    result = GetListPaySystem3(date0,date1)
	
    for row in result:
	c.setFont("Arial", 10)

	if row[9] == 1:
	    c.setFillColorRGB(0,0,0)
	else:
	    c.setFillColorRGB(1,0,0)
	    
	c.drawCentredString(20*mm,(y-4)*mm, row[2]) 
	c.drawCentredString(40*mm,(y-4)*mm, row[3]) 
	c.drawCentredString(60*mm,(y-4)*mm, row[4]) 
	c.drawString(71*mm,(y-4)*mm, row[5])
	c.drawCentredString(120*mm,(y-4)*mm, row[7]) 
	c.drawString(131*mm,(y-4)*mm, row[8])
	c.setLineWidth(1)
	c.lines([
		(30*mm,y*mm,30*mm,(y-s)*mm),
		(50*mm,y*mm,50*mm,(y-s)*mm),
		(70*mm,y*mm,70*mm,(y-s)*mm),
		(110*mm,y*mm,110*mm,(y-s)*mm),
		(130*mm,y*mm,130*mm,(y-s)*mm),
		(10*mm,y*mm,200*mm,y*mm)
		])
	y = y - s

	if y <= 10:
	    c.showPage()
	    y = 280
	



    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])

    c.setFillColorRGB(0,0,0)
    
    if len(result) != 0:	
	c.setFont("ArialBD", 10)
	c.drawString(71*mm,(y-4)*mm, 'ВСЕГО')
	c.drawCentredString(120*mm,(y-4)*mm, GetListPaySystemSum3(date0,date1)) 

	

    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")





##### --- Вывод в печатную форму Внешних поступлений (по CityPay) ---
def ListPaySystem4(date0,date1,periodstr):

	
    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'
    c = canvas.Canvas(FILE_NAME)

    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)

    NewFont2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)




    ### Первоначальные координаты 
    y = 280
    ### Шаг ###
    s = 5

    c.setFont("ArialBD", 14)
    c.drawCentredString(105*mm,y*mm, 'Журнал загрузок платежей')
    y = y - s 
    c.drawCentredString(105*mm,y*mm, '\"CityPay\"')
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, 'за период ' +periodstr) 
    y = y - s*2 
    

    #### --- Линии более толстые ---
    c.setLineWidth(2)
    c.lines([
	    (10*mm,y*mm,200*mm,y*mm),
	    (10*mm,(y-s*2)*mm,200*mm,(y-s*2)*mm)
	    ])

    #### --- Линии обычной толщины ---
    c.setLineWidth(1)
    c.lines([
	    (30*mm,y*mm,30*mm,(y-s*2)*mm),
	    (50*mm,y*mm,50*mm,(y-s*2)*mm),
	    (70*mm,y*mm,70*mm,(y-s*2)*mm),
	    (110*mm,y*mm,110*mm,(y-s*2)*mm),
	    (130*mm,y*mm,130*mm,(y-s*2)*mm)
	    ])

    #### --- Заголовок таблицы ---
    c.drawCentredString(20*mm,(y-5)*mm, "Дата") 
    c.drawCentredString(20*mm,(y-8)*mm, "платежа") 
    c.drawCentredString(40*mm,(y-5)*mm, "Дата") 
    c.drawCentredString(40*mm,(y-8)*mm, "загрузки") 
    c.drawCentredString(60*mm,(y-5)*mm, "Номер") 
    c.drawCentredString(60*mm,(y-8)*mm, "лиц.счёта") 
    c.drawCentredString(90*mm,(y-5)*mm, "Название") 
    c.drawCentredString(90*mm,(y-8)*mm, "услуги") 
    c.drawCentredString(120*mm,(y-5)*mm, "Сумма") 
    c.drawCentredString(120*mm,(y-8)*mm, "платежа") 
    c.drawCentredString(165*mm,(y-5)*mm, "Ошибка") 
    c.drawCentredString(165*mm,(y-8)*mm, "(если есть)") 

    y = y - s*2

    result = GetListPaySystem4(date0,date1)
	
    for row in result:
	c.setFont("Arial", 10)

	if row[9] == 1:
	    c.setFillColorRGB(0,0,0)
	else:
	    c.setFillColorRGB(1,0,0)
	    
	c.drawCentredString(20*mm,(y-4)*mm, row[2]) 
	c.drawCentredString(40*mm,(y-4)*mm, row[3]) 
	c.drawCentredString(60*mm,(y-4)*mm, row[4]) 
	c.drawString(71*mm,(y-4)*mm, row[5])
	c.drawCentredString(120*mm,(y-4)*mm, row[7]) 
	c.drawString(131*mm,(y-4)*mm, row[8])
	c.setLineWidth(1)
	c.lines([
		(30*mm,y*mm,30*mm,(y-s)*mm),
		(50*mm,y*mm,50*mm,(y-s)*mm),
		(70*mm,y*mm,70*mm,(y-s)*mm),
		(110*mm,y*mm,110*mm,(y-s)*mm),
		(130*mm,y*mm,130*mm,(y-s)*mm),
		(10*mm,y*mm,200*mm,y*mm)
		])
	y = y - s

	if y <= 10:
	    c.showPage()
	    y = 280
	



    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])

    c.setFillColorRGB(0,0,0)
    
    if len(result) != 0:	
	c.setFont("ArialBD", 10)
	c.drawString(71*mm,(y-4)*mm, 'ВСЕГО')
	c.drawCentredString(120*mm,(y-4)*mm, GetListPaySystemSum4(date0,date1)) 

	

    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")









##### --- Вывод в печатную форму Акта сверки ---
def ListAct(abonent_id,date0,date1,periodstr,service,address_str):

	
    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'
    c = canvas.Canvas(FILE_NAME)

    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)

    NewFont2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)




    ### Первоначальные координаты 
    y = 280
    ### Шаг ###
    s = 5

    c.setFont("ArialBD", 14)
    c.drawCentredString(105*mm,y*mm, 'Акт сверки')
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, address_str) 
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, 'за период ' +periodstr) 
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, u'По услуге '+service)
    y = y - s 
    

    #### --- Линии более толстые ---
    c.setLineWidth(2)
    c.lines([
	    (10*mm,y*mm,200*mm,y*mm),
	    (10*mm,(y-s)*mm,200*mm,(y-s)*mm)
	    ])

    #### --- Линии обычной толщины ---
    c.setLineWidth(1)
    c.lines([
	    (40*mm,y*mm,40*mm,(y-s)*mm),
	    (90*mm,y*mm,90*mm,(y-s)*mm),
	    (120*mm,y*mm,120*mm,(y-s)*mm),
	    (150*mm,y*mm,150*mm,(y-s)*mm),
	    ])

    #### --- Заголовок таблицы ---
    c.drawCentredString(25*mm,(y-4)*mm, "Дата") 
    c.drawCentredString(65*mm,(y-4)*mm, "Операция") 
    c.drawCentredString(105*mm,(y-4)*mm, "Сумма (руб)") 
    c.drawCentredString(135*mm,(y-4)*mm, "Остаток (руб)")
    c.drawCentredString(175*mm,(y-4)*mm, "Касса(поступление)") 

    y = y - s

    result = GetDataAct(abonent_id,date0,date1,service)
	
    for row in result:
	c.setFont("Arial", 10)

	    
	c.drawCentredString(25*mm,(y-4)*mm, row[4]) 
	c.drawString(45*mm,(y-4)*mm, row[1]) 
	c.drawCentredString(105*mm,(y-4)*mm, "%.2f" % row[6]) 
	c.drawCentredString(135*mm,(y-4)*mm, "%.2f" % row[8])
	c.drawCentredString(175*mm,(y-4)*mm, row[7]) 
	c.setLineWidth(1)
	c.lines([
		(40*mm,y*mm,40*mm,(y-s)*mm),
		(90*mm,y*mm,90*mm,(y-s)*mm),
		(120*mm,y*mm,120*mm,(y-s)*mm),
		(150*mm,y*mm,150*mm,(y-s)*mm),
		(10*mm,y*mm,200*mm,y*mm)
		])
	y = y - s

	if y <= 10:
	    c.showPage()
	    y = 280
	



    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])


    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")



