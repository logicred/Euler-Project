#Answer = 171
#cost < 0.001s
import time

start = time.time()

summary = 0
limit = 2000
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
k = 2
for i in range(1901, limit + 1):
    for j in range(1, 13):
        if i == limit and j == 12:
            break
        if k % 7 == 0:
            summary += 1
        k += month[j]
        if j == 2 and ((i % 4 == 0 and i % 100 != 0) or i % 400 == 0):
            k += 1
print(summary)
end = time.time()

print(end - start)