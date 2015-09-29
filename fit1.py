# -*- coding: utf-8 -*-                                      
from random import randint
print u"тебе надо угадать число, которое я загадаю"
print u"введи предел чисел"
n = int(raw_input(">"))
logic = 0
while (logic !=0):
	print u"введите число"
inp = int (raw_input('>'))
if( x==inp): 
	print u"ты угадал"
	logic = 1
else:
	print u"ты не угадал"