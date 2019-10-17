#Answer = 336108797689259276
#cost = 3.44s
import time
import math

start = time.time()

limit = 1000000000000
summary = 1

for i in range(2, int((-1 + math.sqrt(4 * limit - 3)) / 2) + 1):
    num = int(math.log10((i - 1) * limit + 1) / math.log10(i)) - 1
    summary += ((i ** (num - 1) - 1) // (i - 1) * i ** 3 - (num - 1)) // (i - 1)

print(summary - 31 - 8191)

end = time.time()

print(end - start)