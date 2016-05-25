#coding:utf-8

""" Читаем и пишем в конфигурационный файл """

import	anydbm


CFGFILE = 'ps.cfg'


def ReadValue(KeyValue):
    f = anydbm.open(CFGFILE, 'c')
    a = f[KeyValue]
    f.close()
    return a
    
    
def WriteValue(KeyValue, Value):
    f = anydbm.open(CFGFILE, 'c')
    f[KeyValue] = Value
    f.close()


