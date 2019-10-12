#Answer = 1366
#cost < 0.001s

import time

start = time.time()

limit = 1000
summary = 0
for i in str(pow(2, limit)):
    summary += int(i)
print(summary)

end = time.time()

print(end - start)