#coding:utf-8
import	string


#### --- Разбивает длинную строку из слов на подстроки не более указанной длинны в символах. ---
def StrLimit(LongStr,n):

    
    ## --- Результирующий набор ---
    result = []

    ## -- Слова ---
    words = []

    #### --- Разбивка всей строки на отдельные "слова" ---
    words = string.split(LongStr)
    if len(words)==1:
	result.append(words)
	return words
    elif len(words)==0:
	result.append('')
	return result
    
    # --- Промежуточная строка ---
    list = ''
    
    ## --- Формируем вспомогательную строку, пока это допустипо по числу символов ---
    for w in words:
	# - Если формируемая строка не превышает допустимое значение символов ---
	a = list+' '+string.strip(w)
	
	if len(a)<=n:
	    list = string.lstrip(a)
	else:
	    result.append(list)
	    list = w

    result.append(list)

    return result


