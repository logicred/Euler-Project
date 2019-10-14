#Answer = 1389019170
#cost = 12.8s

import time
import math

start = time.time()

def is_cs(num):
    s = str(num)
    if s[0] == '1' and s[2] == '2' and s[4] == '3' and s[6] == '4'\
        and s[8] == '5' and s[10] == '6' and s[12] == '7' and s[14] == '8'\
        and s[16] == '9' and s[18] == '0':
        return True
    else:
        return False

maxnum = 1929394959697989990
maxnum = int(math.sqrt(maxnum)) + 1
minnum = 1020304050607080900
minnum = int(math.sqrt(minnum)) + 1

x = (minnum // 10 * 10) + 20

while x >= minnum and x < maxnum:
    if is_cs(x ** 2):
        print(x)
        break
    t = x % 100
    if t == 30:
        x += 40
    elif t == 70:
        x += 60

end = time.time()

print(end - start)