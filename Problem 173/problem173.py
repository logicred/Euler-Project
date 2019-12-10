# Answer = 1572729
# cost = 0.996s
import time

start = time.time()

limit = 1000000
upp = limit // 4

f = [0 for i in range(0, upp + 1)]
for i in range(1, upp + 1):
    j = i
    while j <= upp:
        f[j] += 1
        j += i
for i in range(1, int(upp ** (1 /2)) + 1):
    f[i ** 2] -= 1

summary = 0
for i in range(1, upp + 1):
    summary += f[i]
summary = summary // 2
print(summary)

end = time.time()

print(end - start)