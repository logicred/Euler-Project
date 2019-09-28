#Answer = 1533776805
#cost = 0.056s

import time
import math

start = time.time()

flag = 0
limit = 150000
low = 145
for i in range(low, limit):
    h = i * (2 * i - 1)
    p = (math.sqrt(24 * h + 1) + 1) // 6
    if h == (p * (3 * p - 1) // 2):
        flag = 1
        print(h)
        break
if flag == 0:
    print("mission uncompleted.")

end = time.time()

print(end - start)