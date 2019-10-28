#Answer= 329468
#cost = 15.9s

import time
import math
start = time.time()

string = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
limit = 500000
a = 1
b = 1
L = []
for k in range(3, limit):
    temp = a + b
    a = b % 1000000000
    b = temp % 1000000000
    if sorted(str(b)) == string:
        L += [k]

x = (1 + math.sqrt(5)) / 2
y = (1 - math.sqrt(5)) / 2
upp = pow(10, 18)
for k in L:
    t1 = t2 = 1 / math.sqrt(5)
    for i in range(0, k):
        t1 *= x
        t2 *= y
        if t1 > 10 * upp:
            t1 = t1 // 10
        if t2 > 10 * upp:
            t2 = t2 // 10
    temp = t1 - t2
    s = str(int(temp))
    if sorted(s[:9]) == string:
        print(k)
        break

end = time.time()

print(end - start)