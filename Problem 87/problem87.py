#Answer = 109743
#cost = 1.701s

import time

start = time.time()

lim = 50000000
lim1 = int(lim ** (1/2))
lim2 = int(lim ** (1/3))
lim3 = int(lim ** (1/4))

prime1 = prime2 = prime3 = []
L = [1] * (lim1 + 1)
L[0] = L[1] = 0
for i in range(2, lim1):
    if L[i] == 1:
        j = 2 * i
        while j < lim1:
            L[j] = 0
            j += i
        prime1 += [i]

res = set([])
for x in prime1:
    t1 = x ** 4
    if t1 >= lim:
        break
    for y in prime1:
        t2 = y ** 3 + t1
        if t2 >= lim:
            break
        for z in prime1:
            t3 = z ** 2 + t2
            if t3 <= lim:
                res.add(t3)
print(len(res))

end = time.time()

print(end - start)