#coding:utf-8

import	os
import	os.path
import	wx
import	DBTools
import	re
import	string
from	plat.RunSQL	import	ShowAbonentTotal
from	plat.RunSQL	import	LoadPay
from	tools.Messages	import	FileSave





#### --- Выгрузка данных из базы в текстовый файл ---
def	List2Txt(self):

    ### --- Файл выгрузки данных ---
    textfile = 'pl-out/abonent.txt'


    result = ShowAbonentTotal()
	
#### --- Общее количество строк ---
    nn = len(result)



	
    # --- Открытие файла на запись ---
    file=open(textfile,'w')
    file.write('') # для того чтобы очистить содержимое файла если файл уже существовал
    file.close()

    file=open(textfile,'a')


#### --- Индикатор выгрузки данных ---
    dlg = wx.ProgressDialog("Выгрузка...","Сохранение данных в файл.", maximum=nn, style=wx.PD_APP_MODAL|wx.PD_AUTO_HIDE|wx.PD_SMOOTH)
    keepGoing=True
    con = 0

#### --- Обработка построчно ---
    for row in result:

        wstr = str(row[9])+';'+str(row[1])+' '+str(row[2])+' - '+str(row[3])+';'

	file.write(wstr+'\n')



	keepGoing = dlg.Update(con,"Сохранение данных...")
	con = con + 1

    file.close()

    FileSave(self,"Данные сохранены в файле \n"+textfile)

    dlg.Destroy()







#### ---- Загрузка внешних платежей в базу ---
def	txt2Base(self,path):

    ### --- Флаг наличия ошибок ---
    err_exists = 'NO'
    

    ### --- Файл с данными ---
    data = os.path.split(path)[1]
    fname = data.split('.')[0]


    ### --- Подключение к базе ---	
    db=DBTools.DBTools()



    ### --- Лог файл ---
    log = 'pl-log/'+fname+'.log'

    ### --- Файл ошибок ---
    err = 'pl-err/'+fname+'.err'
    
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
	qarray = string.split(line,';')


	keepGoing = dlg.Update(con,"Загрузка данных...")
	con = con + 1

	### --- Загрузка в базу ---
	result = LoadPay(db,qarray[0],qarray[1],qarray[2],qarray[3])
	if result != 'OK':
	    ### --- Регистрация в файле ошибок ---
	    err_file.write(qarray[0]+'\t'+qarray[1]+'\t'+qarray[2]+'\t'+qarray[3]+'\t'+result+'\n')
	    err_exists = 'YES'
	    
	### --- Регистрация в лог файле ---
	log_file.write(qarray[0]+'\t'+qarray[1]+'\t'+qarray[2]+'\t'+qarray[3]+'\t'+result+'\n')


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

