#Answer = 142913828922
#cost = 1.69s

import time
import math

start = time.time()

limit = 2000000
L = [1] * (limit + 1)
summary = 2
for i in range(3, limit + 1, 2):
    if L[i]:
        summary += i
        j = 2 * i
        while j <= limit:
            L[j] = 0
            j += i
        
print(summary)

end = time.time()

print(end - start)