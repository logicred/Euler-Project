# Answer = 7295372
# cost = 4.79s
import time
from math import gcd
start = time.time()

limit = 12000
summary = 0
for i in range(4, limit + 1):
    low = i // 3 + 1
    upp = i // 2
    for j in range(low, upp + 1):
        if gcd(i, j) == 1:
            summary += 1
print(summary)

end = time.time()

print(end - start)