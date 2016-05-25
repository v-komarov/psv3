#coding:utf-8

"""

 --- Резервирование и восстановление данных ---


"""


import	os
import	wx
import	DBTools
from	backup.TableStru	import	Stru
from	backup.RunSQL	import	CountTable
from	backup.RunSQL	import	GetTable
from	backup.RunSQL	import	RunSql



#### --- Резервирование данных ---    
def Backup(path):
    #### --- Считывание структуры данных ---
    data = Stru()

	
    #### --- Первоначальное определение количество строк во всех резервируемых таблицах ---
    sum_row = 0 # Общее количество строк первоначально
    for row in data:
	table = row[0]
	n = CountTable(table)
	sum_row = sum_row + n    

    #### --- Открытие файла резервной копии ---
    file = open(path, 'w')            
    file.write('')
    file.close()
    file = open(path, 'a')            


#### --- Индикатор выгрузки данных ---
    dlg = wx.ProgressDialog("Выгрузка...","Сохранение данных в файл.", maximum=sum_row, style=wx.PD_APP_MODAL|wx.PD_AUTO_HIDE|wx.PD_SMOOTH|wx.PD_ELAPSED_TIME|wx.PD_REMAINING_TIME)
    keepGoing=True
    con = 0



    #### --- Выборка данных ---
    for row in data:
	table = row[0]
	## первоначально строка со списком полей
	list_field = ''
	list_field_real = '' ### Список полей как есть - без изменений для запроса
	## массив типов полей
	list_type = []
	for partrow in row[1]:
	    ### Если поля timestamp - ограничиваем длинну 20-ю символами
	    if partrow[1] == 'timestamp':
		mod = "to_char("+partrow[0]+",'YYYY-MM-DD HH24:MI:SS')"
		list_field = list_field + mod + ','
	    ### Если поля date - ограничиваем длинну 10-ю символами
	    elif partrow[1] == 'date':
		mod = "to_char("+partrow[0]+",'YYYY-MM-DD')"
		list_field = list_field + mod + ','
	    else:
		list_field = list_field + partrow[0] + ','
	    list_field_real = list_field_real + partrow[0] + ','
	    list_type.append(partrow[1])
	#### строка для выполнения запроса
	str_sql = 'select '+list_field[0:-1]+' from '+row[0]+';'
	
	#### Запись в файл строки пердварительного удаления
	file.write('DELETE FROM '+table+';\n')


	#### Выборка данных
	for data in GetTable(str_sql):
	    list_data = '' # Первоначально список значений полей
	    i = 0 # Вспомогательная для определения типа поля
	    for element in data:
		if list_type[i]=='time' or list_type[i]=='date' or list_type[i]=='timestamp' or list_type[i]=='text':
		    element = '\''+str(element)+'\''
		list_data = list_data + str(element) + ','
		i = i+1 ## следующий элемент массива типов данных

	    ### Предварительно строка для записи в файл
	    str_data = 'INSERT INTO '+table+' ('+list_field_real[0:-1]+') VALUES('+list_data[0:-1]+')'



	    file.write(str_data+';\n')

	    #### --- индикатор выгрузки ---
	    keepGoing = dlg.Update(con, "Сохранение данных...")
	    con = con + 1
    

    #### --- Закрытие файла резервной копии ---
    file.close()
    dlg.Destroy()







#### --- Восстановление данных, т.е. загрузка в базу ---
def Restore(path):
    
    db = DBTools.DBTools()

    #### --- Подсчет строк в файле ---
    file = open(path,'r')
    sum_row = 0 # Первоначально количество строк
    for row in file.readlines():
	sum_row = sum_row + 1
    file.close()


#### --- Индикатор загрузки данных ---
    dlg = wx.ProgressDialog("Загрузка...","Загрузка данных в базу.", maximum=sum_row, style=wx.PD_APP_MODAL|wx.PD_AUTO_HIDE|wx.PD_SMOOTH|wx.PD_ELAPSED_TIME|wx.PD_REMAINING_TIME)
    keepGoing=True
    con = 0

    ### --- Строка команды выполнения первоначально ---
    runstr = ""

    #### --- Чтение файла и построчное выполнение команд ---
    file = open(path,'r')
    for row in file.readlines():
	
	runstr = runstr+row
	#### --- Индикатор загрузки ---
	keepGoing = dlg.Update(con, "Загрузка данных...")
	con = con + 1
	
	### --- Команда sql может быть и многострочной, например в случае text полей ---
	### --- Поэтому выпоняем команду если в конце строки символ точка с запятой
	if runstr[-2:-1]==';':
	    RunSql(db,runstr)
	    runstr = ""

    db.Destroy()
    file.close()
    dlg.Destroy()
    


    