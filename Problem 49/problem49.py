#Answer = 296962999629
#cost = 0.913s
import time

start = time.time()

def is_prime(num):
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** (1/2)) + 1, 2):
        if num % i == 0:
            return False
    return True

def is_same(a, b):
    sa = sorted(str(a))
    sb = sorted(str(b))
    return(sa == sb)

upp = 10000
low = 1000
prime = []
for i in range(low, upp):
    if is_prime(i):
        prime += [i]
length = len(prime)
for i in range(0, length):
    for j in range(i + 1, length):
        if is_same(prime[i], prime[j]):
            temp = 2 * prime[j] - prime[i]
            if temp in prime and is_same(prime[i], temp):
                print(prime[i], prime[j], temp)

end = time.time()

print(end - start)