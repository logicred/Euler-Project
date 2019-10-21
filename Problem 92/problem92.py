#Answer = 8581147
#cost = 58.1s
import time

start = time.time()

test = [0 for i in range(0, 10000000)]

def chain(num):
    global test
    x = num
    while (x != 1 and x!= 89):
        s = str(x)
        s_sum = 0
        for y in s:
            s_sum += int(y) ** 2
        x = s_sum
        if x < 10000000:
            if test[x] == 1:
                x = 1
            if test[x] == -1:
                x = 89
    if x == 1:
        test[num] = 1
        return True
    else:
        test[num] = -1
        return False


num = 0
for x in range(1, 10000000):
    if chain(x):
        num += 1
print(10000000 - num)

end = time.time()

print(end - start)
