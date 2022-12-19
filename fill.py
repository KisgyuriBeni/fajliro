

import random

number = random.randint(0,1000)

lista = []

for i in range (0,100):
    number = random.randint(0,1000)
    lista.append(number)


f = open ("elso", "w")

for number in lista:
    f.write(str(number)+ ",")
f.close()
