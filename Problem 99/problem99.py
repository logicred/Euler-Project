#Answer = 709
#cost = 0.003s
import time
from math import log2
start = time.time()

num = 0
maxnum = 0
f = open('p099_base_exp.txt','r')
flag = 0
try:
    while True:
        fi = f.readline()
        flag += 1
        if fi:
            s = fi
            for i in range(0, len(s)):
                if s[i] == ',':
                    sa = s[:i]
                    sb = s[i + 1:]
                    break
            a = int(sa)
            b = int(sb)
            temp = b * log2(a)
            #print(flag, a, b, temp)
            if maxnum < temp:
                maxnum = temp
                num = flag
        else:
            break
finally:
    f.close()
print(num)

end = time.time()

print(end - start)