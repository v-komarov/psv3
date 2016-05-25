#!/usr/bin/env python
#coding:utf-8


import	os
import	string



### --- Открытие файла на запись ---
fsql = open('banks.sql','w')
fsql.write('')
fsql.close()


### --- Открытие файла на добавление ---    
fsql = open('banks.sql','a')


### --- Открытие исходного файла на чтение ---
fcsv = open('bnkseek.csv','r')


### --- Построчное считывание ---
for line in fcsv.readlines():
    qarray = string.split(line,'\t')
    if len(qarray[7])==0: 
	qarray[7]='\'\''
    if len(qarray[8])==0: 
	qarray[8]='\'\''
    if len(qarray[10])==0: 
	qarray[10]='\'\''
    if len(qarray[18])==0: 
	qarray[18]='\'\''
    if len(qarray[23])==0: 
	qarray[23]='\'\''
    fsql.write('INSERT INTO sa_banks(sa_bik,sa_bankname,sa_city,sa_address,sa_phone,sa_bank,sa_corschet) VALUES('+qarray[12]+','+qarray[10]+','+qarray[7]+','+qarray[8]+','+qarray[18]+','+qarray[11]+','+qarray[23]+');\n')


fsql.close()
fcsv.close()
