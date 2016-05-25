#!/usr/bin/env python
#coding:utf-8


import	shelve



### --- Запись значения в CFG файл ---
f = shelve.open('../ps.cfg')
f['pdfview']='evince'
f.close()


