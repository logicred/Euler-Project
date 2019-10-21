#answer = 190569291
#cost = 118s

import time

start = time.time()

test = [[0 for i in range(0, 101)] for j in range(0, 101)]

print(test[0][0])

def summation(num, maxnum):
    global test
    if maxnum == 1 or num == 1:
        return 1
    else:
        res = 0
        if test[num][maxnum] == 0:
            if num > maxnum:
                res += summation(num - maxnum, maxnum)
                res += summation(num, maxnum - 1)
            else:
                res += 1
                res += summation(num, num - 1)
                test[num][maxnum] = res
        else:
            res = test[num][maxnum]
        return res

print(summation(100, 100) - 1)

end = time.time()

print(end - start)