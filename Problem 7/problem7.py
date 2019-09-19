#Answer = 104743
#cost = 0.569s

import time
import math

start = time.time()

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

limit = 10001
i = 2
flag = 0
while i >= 2:
    if is_prime(i):
        flag += 1
    if flag == limit:
        break
    i += 1
print(i)

end = time.time()

print(end - start)