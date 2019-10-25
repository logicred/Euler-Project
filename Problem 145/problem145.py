#Answer = 608720
#cost = 254.4s
import time

start = time.time()

limit = 100000000
summary = 0
def odd(num):
    if num % 10 == 0:
        return False
    s = str(num)
    x = str(int(s) + int(s[::-1]))
    for i in x:
        if int(i) % 2 == 0:
            return False
    return True

for i in range(1, limit):
    if odd(i):
        summary += 1

print(summary)

end = time.time()

print(end - start)