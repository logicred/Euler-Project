#Answer = 25164150
#cost < 0.001s
import time

start = time.time()

limit = 100
sum1 = sum2 = 0
for i in range(1, limit + 1):
    sum1 += i ** 2
    sum2 += i
sum2 *= sum2
print(sum2 - sum1)

end = time.time()

print(end - start)