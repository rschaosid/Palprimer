#Edit range here
bottomrange = 0
toprange = 10000000


import math
import time

primeslist = []
palprimeslist = []
hpalprimeslist = []
print("PRIMES FOR THAT RANGE:")
time.sleep(1)
for i in range (bottomrange,toprange):
    num = i
    for i in range(2,num):
       if (num % i) == 0:
           break
    else:
        print(num)
        primeslist.append(num)
        
print("THAT'S A TOTAL OF:")
time.sleep(1)
print(len(primeslist))
time.sleep(1)

print("OF THOSE, THESE ARE PALPRIMES:")
time.sleep(1)
for item in primeslist:
    if str(item) != str(item)[::-1] or item<10:
        pass
    else:
        print(item)
        palprimeslist.append(item)
time.sleep(1)
print("THAT'S A TOTAL OF:")
time.sleep(1)
print(len(palprimeslist))