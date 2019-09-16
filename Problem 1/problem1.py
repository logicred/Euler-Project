#Answer = 233168
#cost < 0.001s
import time

start = time.time()

summary = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        summary += i
print(summary)

end = time.time()

print(end - start)