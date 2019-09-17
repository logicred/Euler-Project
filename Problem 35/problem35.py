#Answer = 55
#cost = 8.84s

import time
import math

start = time.time()

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False

def is_cir_prime(num):
    if not is_prime(int(num)):
            return False
    if int(num) < 10 and int(num) > 1:
        return True
    s = num
    for i in range(len(num)):
        s = s[1:] + s[0]
        if not is_prime(int(s)):
            return False
    return True

n = 0
for x in range(1000000+1):
    if is_cir_prime(str(x)):
        n = n + 1

print(n)

end = time.time()

print(end - start)