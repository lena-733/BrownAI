from math import pow
from math import sqrt
from random import randint
from random import shuffle
from random import choice

result_1 = pow(2,4)
print("result_1 "+ str(result_1))

result_2 = sqrt(16)
print("result_2 "+str(result_2))

result_3 = randint(0,10)
print("result_3 "+str(result_3))

names = ['fun','help', 'wow']
print("names "+ str(names))

shuffle(names)
print("names after shuffle = " + str(names))

result_4 = choice(names)
print("chosen name "+ result_4)
