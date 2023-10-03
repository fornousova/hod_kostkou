import random

seznam = [0,0,0,0,0,0,0,0,0,0,0]

hody_kostkou = 10000
for i in range(hody_kostkou):
    k1 = random.randint (1,6)
    k2 = random.randint (1,6)
    seznam[k1+k2-2]+=1
    