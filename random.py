#! /usr/bin/env python

#要求用户选择投掷的色子个数以及每个色子具有的面数
from random imprort randrange
num = input('How many dice? ')
sides = input('How many sides per die? ')
sum = 0
for i in range(num): sum += randrange(sides) + 1
print 'The result is',sum

#运势fortune.py
import fileinput,random
fortunes = list(fileinput.input())
print random.choice(fortunes)
#测试python fortune.py /usr/dict/words

#随机发牌
values = range(1,11) + 'Jack Queen king'.spilt()
suits = 'diamonds clubs hearts spades'.spilt()
deck = ['%s of %s' % (v,s) for v in values for s in suits]
