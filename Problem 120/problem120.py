#Answer = 333082500
#cost < 0.001s
import time

start = time.time()

limit = 1000
summary = 0
for a in range(3, limit + 1):
    if a % 2 == 0:
        summary += a * (a - 2)
    else:
        summary += a * (a - 1)
print(summary)

end = time.time()

print(end - start)