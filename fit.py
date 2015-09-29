# -*- coding: utf-8 -*-                                      
from random import randint
print u"тебе надо угадать число, которое я загадаю"
print u"введи предел чисел"
n = int(raw_input(">"))
x= randint(0,n)
print u"введите число"
inp = int (raw_input('>'))
if x==inp:
	print u"ты выиграл"
else:
	print u"ты проиграл"