#Answer = 100
#cost = 0.019s

import time
import math

start = time.time()

def cancel(i, j):
    if i % 10 == 0 and j % 10 == 0:
        return False
    si = str(i)
    sj = str(j)
    for x in range(0, len(si)):
        for y in range(0, len(sj)):
            if si[x] == sj[y]:
                ti = list(si)
                tj = list(sj)
                ti.pop(x)
                tj.pop(y)
                if int(''.join(ti)) * j == int(''.join(tj)) * i:
                    return True
    return False

x = 1
y = 1
for i in range(10, 100):
    for j in range(i + 1, 100):
        if cancel(i, j):
            print(i, j)

end = time.time()

print(end - start)