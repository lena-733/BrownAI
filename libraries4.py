
from math import pow as pwr
from math import sqrt as squirt
from random import randint as rando
from random import shuffle as mix
from random import choice as decision

result_1 = pwr(2,4)
print("result_1 "+ str(result_1))

result_2 = squirt(16)
print("result_2 "+str(result_2))

result_3 = rando(0,10)
print("result_3 "+str(result_3))

names = ['fun','help', 'wow']
print("names "+ str(names))

mix(names)
print("names after shuffle = " + str(names))

result_4 = decision(names)
print("chosen name "+ result_4)
