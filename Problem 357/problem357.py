#Answer = 1739023853137
#cost = 181s

import time
import math

start0 = time.time()

num = 100000000
summary = 0
L = [1] * (num + 1)
x = 2
y = 2 * x
while y <= num:
    L[y] = 0
    y += x
x = 3
while x >=3 and x <= num:
    if L[x] == 1:
        y = 2 * x
        while y <= num:
            L[y] = 0
            y += x
    x += 2

start1 = time.time()

def is_generate(num):
    global L
    for x in range(3, int(math.sqrt(num)) + 1):
        if num % x == 0 and L[x + num // x] == 0:
            return False
    return True

x = 6
while x >= 6 and x <= num - 1:
    if L[x + 1] == 1 and L[x // 2 + 2] == 1 and is_generate(x):
        summary += x
    x += 4

print(summary + 1 + 2)
end = time.time()

print(end - start0)
print(start1 - start0)