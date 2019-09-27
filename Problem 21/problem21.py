#Answer = 36126
#cost = 0.138s

import time
import math

start = time.time()

limit = 10000
L = [0] * (limit + 1)
summary = 0
def factor_sum(num):
    if num == 1:
        return 0
    summary = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if i ** 2 == num:
                summary += i
            elif i != 1:
                summary += i + num // i
            else:
                summary += i
    return summary

for i in range(1, limit + 1):
    L[i] = factor_sum(i)
for i in range(1, limit + 1):
    if L[i] <= limit and L[L[i]] == i and i < L[i]:
        summary += (i + L[i])

print(summary)   

end = time.time()

print(end - start)