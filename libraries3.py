import math as matematic
import random as verschiedenen

result_1 = matematic.pow(2,4)
print("result_1 "+ str(result_1))

result_2 = matematic.sqrt(16)
print("result_2 "+str(result_2))

result_3 = verschiedenen.randint(0,10)
print("result_3 "+str(result_3))

names = ['fun','help', 'wow']
print("names "+ str(names))

verschiedenen.shuffle(names)
print("names after shuffle = " + str(names))

result_4 = verschiedenen.choice(names)
print("chosen name "+ result_4)
