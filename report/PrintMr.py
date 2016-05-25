#coding:utf-8

import	wx
import	RWCfg
import	os
import	time


from	reportlab.pdfgen	import	canvas
from	reportlab.lib.units	import	mm
from	reportlab.pdfbase	import	pdfmetrics
from	reportlab.pdfbase	import	ttfonts
from	reportlab.lib		import	colors
from	reportlab.lib.pagesizes	import	letter, A4, landscape



from	DBTools			import	DBTools
from	tools.StrHelpers	import	StrLimit
from	RunSQL			import	GetNow
from	RunSQLMr		import	GetStoreGroup
from	RunSQLMr		import	GetMateInfo
from	RunSQLMr		import	GetMate
from	RunSQLMr		import	GetTaskP
from	RunSQLMr		import	GetTaskWorker
from	RunSQLMr		import	GetTaskMate



"""
    Для различных систем существуют различные просмотровщики PDF файлов
    универсального решения для этого пока не найдено,
    поэтому чтобы не привязвать исходные файлы к конкретному просмотровщику 
    храним вид/тип просмотровщика в cfg файле - название поля 'pdfview'
"""

### --- Просмотровщик PDF файлов ---
PDFVIEW = RWCfg.ReadValue('pdfview')





#### --- Подготовка данных для печатной формы остатков на складе ---
def RepMateStore(store,group):



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
    c.drawCentredString(105*mm,y*mm, 'Остатки на складе')
    y = y - s 
    c.drawCentredString(105*mm,y*mm, u'Склад: '+store+u'  Группа: '+group)
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
	    (140*mm,y*mm,140*mm,(y-s)*mm),
	    (170*mm,y*mm,170*mm,(y-s)*mm),
	    ])

    #### --- Заголовок таблицы ---
    c.drawCentredString(15*mm,(y-4)*mm, "№") 
    c.drawCentredString(80*mm,(y-4)*mm, "Материал") 
    c.drawCentredString(155*mm,(y-4)*mm, "Ед.изм.") 
    c.drawCentredString(185*mm,(y-4)*mm, "Остаток") 
    y -= s 


    ### --- Нумерация ---
    n = 1


	
    for row in GetStoreGroup(store,group):
	c.setFont("Arial", 10)
	c.drawCentredString(15*mm,(y-4)*mm, str(n)) 
	c.drawString(21*mm,(y-4)*mm, row[0]) 
	c.drawCentredString(155*mm,(y-4)*mm, row[1]) 
	c.drawCentredString(185*mm,(y-4)*mm, row[3]) 
	c.setLineWidth(1)
	c.lines([
		(10*mm,y*mm,200*mm,y*mm),
		(20*mm,y*mm,20*mm,(y-s)*mm),
		(140*mm,y*mm,140*mm,(y-s)*mm),
		(170*mm,y*mm,170*mm,(y-s)*mm),
		])
	y -= s
	n += 1

	if y <= 10:
	    c.showPage()
	    y = 280



    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])

    

    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")









#### --- Подготовка данных для печатной формы по движению материала ---
def RepMateInfo(mate_kod,date0,date1,periodstr):


    ### --- Подключение к базе ---
    db = DBTools()

    ### --- Получение названия и ед. измерения ---
    mate = GetMate(db,mate_kod)


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
    c.drawCentredString(105*mm,y*mm, 'Движение (операции)')
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, 'Материал: '+mate[1]+'  Ед.из: '+mate[2])
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(105*mm,y*mm, periodstr ) 
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
	    (90*mm,y*mm,90*mm,(y-s)*mm),
	    (110*mm,y*mm,110*mm,(y-s)*mm),
	    (160*mm,y*mm,160*mm,(y-s)*mm),
	    (170*mm,y*mm,170*mm,(y-s)*mm),
	    (185*mm,y*mm,185*mm,(y-s)*mm),
	    ])

    #### --- Заголовок таблицы ---
    c.drawCentredString(20*mm,(y-4)*mm, "Дата") 
    c.drawCentredString(60*mm,(y-4)*mm, "Операция") 
    c.drawCentredString(100*mm,(y-4)*mm, "Остаток") 
    c.drawCentredString(135*mm,(y-4)*mm, "Улица") 
    c.drawCentredString(165*mm,(y-4)*mm, "Дом") 
    c.drawCentredString(178*mm,(y-4)*mm, "Кв.") 
    c.drawCentredString(193*mm,(y-4)*mm, "Подъезд") 
    y -= s 



	
    for row in GetMateInfo(db,mate_kod,date0,date1):
	c.setFont("Arial", 10)
	c.drawCentredString(20*mm,(y-4)*mm, row[0]) 
	c.drawString(31*mm,(y-4)*mm, row[1]) 
	c.drawCentredString(100*mm,(y-4)*mm, row[3]) 
	c.drawString(111*mm,(y-4)*mm, row[8]) 
	c.drawCentredString(165*mm,(y-4)*mm, row[9]) 
	c.drawCentredString(178*mm,(y-4)*mm, row[10]) 
	c.drawCentredString(193*mm,(y-4)*mm, row[11]) 
	c.setLineWidth(1)
	c.lines([
		(10*mm,y*mm,200*mm,y*mm),
		(30*mm,y*mm,30*mm,(y-s)*mm),
		(90*mm,y*mm,90*mm,(y-s)*mm),
		(110*mm,y*mm,110*mm,(y-s)*mm),
		(160*mm,y*mm,160*mm,(y-s)*mm),
		(170*mm,y*mm,170*mm,(y-s)*mm),
		(185*mm,y*mm,185*mm,(y-s)*mm),
		])
	y -= s

	if y <= 10:
	    c.showPage()
	    y = 280



    c.lines([
	    (10*mm,y*mm,200*mm,y*mm)
	    ])



    ### --- Отключение ---
    db.Destroy()
        

    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")












#### --- Подготовка данных для печатной формы заявок по подъезду ---
def RepTaskP(UlDomP,date0,date1,periodstr):


    ### --- Улица, дом, подъезд ---
    ul = UlDomP.split('#')[0]
    dom = UlDomP.split('#')[1]
    p = UlDomP.split('#')[2]


    ### --- Подключение к базе ---
    db = DBTools()

    ### --- Имя файла для вывода ---
    FILE_NAME = os.getcwd()+'/tmp/'+str(time.time())+'.pdf'
    c = canvas.Canvas(FILE_NAME, pagesize=landscape(A4))

    NewFont = ttfonts.TTFont('Arial','font/arial.ttf')
    pdfmetrics.registerFont(NewFont)

    NewFont2 = ttfonts.TTFont('ArialBD','font/arialbd.ttf')
    pdfmetrics.registerFont(NewFont2)



    ### Первоначальные координаты 
    y = 200
    ### Шаг ###
    s = 5

    c.setFont("ArialBD", 14)
    c.drawCentredString(145*mm,y*mm, 'Заявки по подъезду')
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(145*mm,y*mm, 'Улица: '+ul+'  Дом: '+dom+' Подъезд: '+p)
    y = y - s 
    c.setFont("ArialBD", 10)
    c.drawCentredString(145*mm,y*mm, periodstr ) 
    y = y - s*2 
    

    #### --- Линии более толстые ---
    c.setLineWidth(2)
    c.lines([
	    (10*mm,y*mm,290*mm,y*mm),
	    (10*mm,(y-s)*mm,290*mm,(y-s)*mm)
	    ])

    #### --- Линии обычной толщины ---
    c.setLineWidth(1)
    c.lines([
	    (30*mm,y*mm,30*mm,(y-s)*mm),
	    (90*mm,y*mm,90*mm,(y-s)*mm),
	    (145*mm,y*mm,145*mm,(y-s)*mm),
	    (180*mm,y*mm,180*mm,(y-s)*mm),
	    ])

    #### --- Заголовок таблицы ---
    c.drawCentredString(20*mm,(y-4)*mm, "Дата") 
    c.drawCentredString(60*mm,(y-4)*mm, "Заявка") 
    c.drawCentredString(118*mm,(y-4)*mm, "Информация") 
    c.drawCentredString(163*mm,(y-4)*mm, "Исполнители") 
    c.drawCentredString(232*mm,(y-4)*mm, "Материалы") 
    y -= s 


	
    for row in GetTaskP(db,date0,date1,ul,dom,p):

	### --- Высота строки ---
	h = 2

	y2 = y
	y3 = y
	y4 = y
	y5 = y

	### --- Получение многострочного текста заявки ---
	tt = StrLimit(row[9],20)
	t = len(tt)

	if h < t: h = t	

	### --- Получение многострочного примечания к заявке ---
	ii = StrLimit(row[18],20)
	i = len(ii)

	if h < i: h = i	

	### --- Получение списка исполнителей ---
	ww = GetTaskWorker(db,row[0])
	w = len(ww)
	
	if h < w: h = w	
	

	### --- Получение списка материалов ---
	ma = GetTaskMate(db,row[0])
	m = len(ma)
	
	if h < m: h = m	



	c.setFont("Arial", 10)
	c.drawCentredString(20*mm,(y-4)*mm, row[2]) 
	c.drawCentredString(20*mm,(y-9)*mm, row[7]) 
	### --- Вставка текста заявки ---
	for item in tt:
	    c.drawString(31*mm,(y2-4)*mm, item) 
	    y2 -= s
	    c.setLineWidth(1)
	    c.lines([
		    (30*mm,y*mm,30*mm,y2*mm),
		    (90*mm,y*mm,90*mm,y2*mm),
		    (145*mm,y*mm,145*mm,y2*mm),
		    (180*mm,y*mm,180*mm,y2*mm),
		    ])

	### --- Вставка информации заявки ---
	for item in ii:
	    c.drawString(91*mm,(y3-4)*mm, item) 
	    y3 -= s
	    c.setLineWidth(1)
	    c.lines([
		    (30*mm,y*mm,30*mm,y3*mm),
		    (90*mm,y*mm,90*mm,y3*mm),
		    (145*mm,y*mm,145*mm,y3*mm),
		    (180*mm,y*mm,180*mm,y3*mm),
		    ])
	    
	### --- Вставка информации по исполнителям ---
	for item in ww:
	    c.drawString(146*mm,(y4-4)*mm, item[0]) 
	    y4 -= s
	    c.setLineWidth(1)
	    c.lines([
		    (30*mm,y*mm,30*mm,y4*mm),
		    (90*mm,y*mm,90*mm,y4*mm),
		    (145*mm,y*mm,145*mm,y4*mm),
		    (180*mm,y*mm,180*mm,y4*mm),
		    ])


	### --- Вставка информации по материалам ---
	for item in ma:
	    c.drawString(181*mm,(y5-4)*mm, item[0]+u'- '+item[2]+item[1]+u', Сумма: '+item[3]) 
	    y5 -= s
	    c.setLineWidth(1)
	    c.lines([
		    (30*mm,y*mm,30*mm,y5*mm),
		    (90*mm,y*mm,90*mm,y5*mm),
		    (145*mm,y*mm,145*mm,y5*mm),
		    (180*mm,y*mm,180*mm,y5*mm),
		    ])



	y -= s*h


	c.setLineWidth(1)
	c.lines([
		(30*mm,y*mm,30*mm,(y+s)*mm),
		(90*mm,y*mm,90*mm,(y+s)*mm),
		(145*mm,y*mm,145*mm,(y+s)*mm),
		(180*mm,y*mm,180*mm,(y+s)*mm),
		])



	c.setLineWidth(1)
	c.lines([
		(10*mm,y*mm,290*mm,y*mm),
		])


	if y <= 50:
	    c.showPage()
	    y = 200



#    c.lines([
#	    (10*mm,y*mm,200*mm,y*mm)
#	    ])



    ### --- Отключение ---
    db.Destroy()
        

    c.save()
    os.system(PDFVIEW+" "+FILE_NAME+" &")


