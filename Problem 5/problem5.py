#Answer = 232792560
#cost < 0.001s

import time
import math

start = time.time()

limit = 20
prime = [0] * (limit + 1)
def find_prime(num):
    summary = 1
    global prime
    for i in range(1, num + 1):
        prime[i] = 1
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                prime[i] = 0
        if prime[i] != 0 and i >= 2:
            prime[i] = int(math.log(num)/math.log(i))
            summary *= int(pow(i, prime[i]))
    return summary

print(find_prime(limit))

end = time.time()

print(end - start)