#coding:utf-8

import	os
import	wx
import	DBTools
import	time
import	string
from	plat.RunSQL	import	ShowAbonentBrig
from	plat.RunSQL	import	LoadPay
from	plat.RunSQL	import	LoadPay2
from	plat.RunSQL	import	GetDateName
from	tools.Messages	import	FileSave




brig = [
'БАТУРИНА 5',
'БАТУРИНА 5А',
'БАТУРИНА 5Г',
'БАТУРИНА 5Д',
'БАТУРИНА 7',
'БАТУРИНА 9',
'БАТУРИНА 10',
'БАТУРИНА 15',
'ВЕСНЫ 2А',
'ВЕСНЫ 7Б',
'ВЗЛЕТНАЯ 30',
'ВЗЛЕТНАЯ 34',
'ВЗЛЕТНАЯ 36',
'ВЗЛЕТНАЯ 38',
'МОЛОКОВА 5',
'МОЛОКОВА 5А',
'МОЛОКОВА 5Б',
'МОЛОКОВА 5В',
'МОЛОКОВА 5Г',
'МОЛОКОВА 13',
'МОЛОКОВА 15',
'МОЛОКОВА 17',
'МОЛОКОВА 19',
'МОЛОКОВА 27',
'МОЛОКОВА 29',
'МОЛОКОВА 31',
'МОЛОКОВА 31В',
'МОЛОКОВА 31Д',
'МОЛОКОВА 33'
]





#### --- Выгрузка данных из базы в текстовый файл ---
def	Brig2Txt(self):
	
    db = DBTools.DBTools()

    #### --- Общее количество строк ---
    nn = 0


    result = []
    for item in brig:
	address = item.split(' ')
	res = ShowAbonentBrig(db,address[0],address[1])
	n = len(res)
	nn =+ n
	result.append(res)

    filename = 'br-out/'+GetDateName(db)

	
	
    # --- Открытие файла на запись ---
    file=open(filename,'w')
    file.write('') # для того чтобы очистить содержимое файла если файл уже существовал
    file.close()

    file=open(filename,'a')


    #### --- Индикатор выгрузки данных ---
    dlg = wx.ProgressDialog("Выгрузка...","Сохранение данных в файл.", maximum=nn, style=wx.PD_APP_MODAL|wx.PD_AUTO_HIDE|wx.PD_SMOOTH)
    keepGoing=True
    con = 0

    #### --- Обработка построчно ---
    for row in result:
	for row2 in row:
	
	    file.write(row2[0]+"\r\n")

	    keepGoing = dlg.Update(con,"Сохранение данных...")
	    con = con + 1

    file.close()

    dlg.Destroy()

    db.Destroy()

    FileSave(self,'Данные сохранены в файле\n'+filename)

    







#### ---- Загрузка внешних платежей в базу ---
def brig2Base(self,path):
    
    ### --- Имя файла ---
    shotname = str(time.time())
    
    ### --- Флаг наличия ошибок ---
    err_exists = 'NO'
    

    ### --- Файл с данными ---
    data = os.path.split(path)[1]
    fname = data.split('.')[0]


    ### --- Подключение к базе ---	
    db=DBTools.DBTools()

    ### --- Результат первоначально ---
    result = 'ERROR'


    ### --- Лог файл ---
    log = 'br-log/'+shotname+'.log'

    ### --- Файл ошибок ---
    err = 'br-err/'+shotname+'.err'
    
    ### --- Определение общего количества строк в файле ---
    nn	= 0
    file = open(path,'r')
    for line in file.readlines():
	nn = nn + 1
    file.close()
	


#### --- Индикатор выгрузки данных ---
    dlg = wx.ProgressDialog("Загрузка...","Сохранение данных в базу.", maximum=nn, style=wx.PD_APP_MODAL|wx.PD_AUTO_HIDE|wx.PD_SMOOTH)
    keepGoing=True
    con = 0
	

### --- Открытие файлов ---	
    log_file = open(log,'a')
    err_file = open(err,'a')
    data_file = open(path,'r')
    

    for line in data_file.readlines():
	data = string.split(line,'#')

	keepGoing = dlg.Update(con,"Загрузка данных...")
	con = con + 1

	uldom = data[0]+' '+data[1]


	#### --- Проверка данных на совпадения спсика домов ---
	try:
	    x = brig.index(uldom)
	    if brig[x] == uldom:
		#### --- Загрузка в базу ---
		datetime = data[4].split(' ')
		newdate = datetime[0].split('.')[2]+'-'+datetime[0].split('.')[1]+'-'+datetime[0].split('.')[0]
		p = data[5].replace(',','.',1)
		p2 = eval(p.replace('\r\n','',1))
		if p2 != 0 and data[3] == 'ДОМОФОН':
		    

		    result = LoadPay2(db,data[0],data[1],data[2],data[3],newdate+' '+datetime[1],p2)

		    if result != 'OK':
			### --- Регистрация в файле ошибок ---
	    		err_file.write(data[0]+'\t'+data[1]+'\t'+data[2]+'\t'+data[3]+'\t'+data[4]+'\t'+data[5].replace('\r\n','',1)+'\t'+result+'\n')
	    		err_exists = 'YES'

		
		    ### --- Регистрация в лог файле ---
		    log_file.write(data[0]+'\t'+data[1]+'\t'+data[2]+'\t'+data[3]+'\t'+data[4]+'\t'+data[5].replace('\r\n','',1)+'\t'+result+'\n')

	except:
	    pass
	    


    data_file.close()
    log_file.close()
    err_file.close()
    dlg.Destroy()


    ### --- Удаление файла с данными ---
    os.remove(path)


    db.Destroy()

    ### --- Возврат значений --
    if err_exists == 'YES':
	return err
    else:
	return 'OK'

