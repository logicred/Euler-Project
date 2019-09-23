#Answer = 76576500
#cost = 0.485s
import time

start = time.time()

limit = 500
prime_list = [3] + [0] * limit
def primefind():
    global prime_list
    k = 0
    for i in range(2, limit):
        flag = True
        j = 0
        while j < limit and prime_list[j] != 0:
            if i % prime_list[j] == 0:
                flag = False
                break
            j += 1
        if flag:
            prime_list[k] = i
            k += 1

def factor(num):
    summary = 1
    i = 0
    while prime_list[i] != 0:
        j = 0
        while num % prime_list[i] == 0:
            num = num // prime_list[i]
            j += 1
        summary *= (j + 1)
        i += 1
    return summary

def triangular_num(num):
    return num * (num + 1) // 2

primefind()
i = 1
while factor(triangular_num(i)) <= limit:
    i += 1
print(triangular_num(i))

end = time.time()

print(end - start)