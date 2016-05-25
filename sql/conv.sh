#!/bin/sh

FILENAME=${1}

tr -d "\r" < ${FILENAME}.sql > tmp

iconv -f CP1251 -t UTF-8 tmp > ${FILENAME}_utf8.sql

rm -f tmp
