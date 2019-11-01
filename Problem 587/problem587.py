#Answer = 2240
#cost = 0.006s
import time
import math 
from math import sqrt
start = time.time()

pi = 3.14159265
for n in range(1, 100000):
    y = (n + 1 - sqrt(2 * n)) / (n ** 2 + 1)
    x = n * y
    s1 = 0.5 * (x * y + (y + 1) * (1 - x)) - math.atan((1 - x) / (1 - y)) / 2
    s2 = 1 - 1 / 4 * pi
    temp = s1 / s2
    if temp < 0.001:
        print(n)
        break

end = time.time()

print(end - start)