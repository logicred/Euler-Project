#Answer = 665168997
#cost < 0.001s

import time

start = time.time()

limit = 1000
summary = 1
for i in range(3, limit + 1, 2):
    summary += (4 * i ** 2 - 6 * (i - 1))
print(summary)

end = time.time()

print(end - start)