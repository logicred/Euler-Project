#Answer = 137846528820
#cost = 0.002s

import time

start = time.time()

length = 20 + 1
weight = 20 + 1
L = [[0 for i in range(length)] for j in range(weight)]
for i in range(weight):
    L[0][i] = 1
for j in range(length):
    L[j][0] = 1
for i in range(1, weight):
    for j in range(1, length):
        L[j][i] = L[j - 1][i] + L[j][i - 1]
print(L[weight - 1][length - 1])

end = time.time()

print(end - start)