#Answer = 249
#cost = 0.0927s
import time

start = time.time()

def is_pan(num):
    s = str(num)
    return s == s[::-1]

def is_lychrel(num):
    if num == 0:
        return True
    i = 1
    while i < 50:
        s = str(num)[::-1]
        while s[0] == '0':
            s = s[1:]
        num += int(s)
        if is_pan(num):
            return True
        i += 1
    return False

res = 0
n = 10000
for x in range(0, n):
    if not is_lychrel(x):
        res += 1
print(res)

end = time.time()

print(end - start)
