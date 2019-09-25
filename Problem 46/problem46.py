#Answer = 5777
#cost = 0.095s

import time
import math
start = time.time()

limit = 10000
L = [0] * (limit + 1)

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True 

for i in range(3, limit + 1, 2):
    if is_prime(i):
        j = 1
        while i + 2 * j ** 2 <= limit:
            L[i + 2 * j ** 2] = 1
            j += 1
for i in range(3, limit + 1, 2):
    if L[i] == 0 and is_prime(i) == False:
        print(i)
        break

end = time.time()

print(end - start)