import time

start = time.time()

limit = 1000000

def is_triangle(a, b):
    if b % 2 == 1:
        return 0
    else:
        b = b // 2
        c = int((a ** 2 - b ** 2) ** (1 / 2))
        if c ** 2 == a ** 2 - b ** 2:
            return a + b + c
        else:
            return 0

'''summary = 0
for i in range(2, (limit + 1) // 3 + 1):
    summary += is_triangle(i, i - 1)
for i in range(2, (limit - 1) // 3 + 1):
    summary += is_triangle(i, i + 1)
print(summary)'''
for m in range(1, 10 + 1):
    for n in range(1, m):
        print(m ** 2 + n ** 2, m ** 2 - n ** 2, 2 * m * n)
end = time.time()

print(end - start)