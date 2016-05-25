#coding:utf-8

""" Упражняемся с изменением кодировок """


def win2utf(Value):
    return unicode(Value, "cp1251").encode("utf-8")
    
    
def win(Value):
    return Value.encode("cp1251")



