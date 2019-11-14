#Answer = 281632621
#cost = 59.7s
import time
import math
start = time.time()

mod = 1000000000
limit = 1000000000000000
summary = 0

i = limit
flag = 1
while True:
    j = limit // (flag + 1)
    if i == j:
        break
    temp = flag * (i * (i + 1) * (2 * i + 1) - j * (j + 1) * (2 * j + 1)) // 6
    summary += (temp % mod)
    flag += 1
    i = j
for k in range(1, i + 1):
    summary += ((limit // k) * k ** 2) % mod
print(summary % mod)

end = time.time()

print(end - start)