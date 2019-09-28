#Answer = -61 971 70
#cost = 0.873

import time
import math

start = time.time()

limit = 1000
def is_prime(num):
    if num < 0:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True 

L = [0] * limit
maxnum = 0
j = 0
for i in range(2, 2 * limit + 1):
    if is_prime(i) == True:
        L[j] = i
        j += 1
i = 0
while i < j and L[i] <= limit:
    b = L[i]
    k = 0
    while k < j:
        c = L[k]
        m = 0
        while is_prime(m ** 2 + (c - b - 1) * m + b) == True:
            if m > maxnum:
                maxnum = m
                a_seat = c - b - 1
                b_seat = b
            m += 1
        k += 1
    i += 1
print(a_seat, b_seat, maxnum)

end = time.time()

print(end - start)