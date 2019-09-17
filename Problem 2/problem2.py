#Answer = 4613732
#cost < 0.001s

import time

start = time.time()

i = 3
L = [1, 1, 2] + [0] * 97
summary = 0
while i >= 3:
    L[i] = L[i - 2] + L[i - 1]
    if L[i] > 4000000.0 or i == 100:
        break
    i += 1
i = 2
while i >= 2:
    if L[i] == 0:
        break
    summary += L[i]
    i += 3
print(summary)

end = time.time()

print(end - start)