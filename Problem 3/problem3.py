#Answer = 6857
#cost = 0.017s

import time
import math

start = time.time()

def is_prime(num):
    if num == 1 or num == 0:
        return False
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True

num = 600851475143
limit = 10000
L = [0] * limit

maxprime = 0
x = 1
while x >= 1:
    if x >= limit or x > num:
        break
    if L[x] == 0 and is_prime(x):
        L[x] = 1
    if L[x] == 1 and num % x == 0:
        num = num // x
        maxprime = x
    else:
        x += 1
print(maxprime)

end = time.time()

print(end - start)