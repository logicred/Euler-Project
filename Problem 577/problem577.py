# Answer = 265695031399260211
# cost = 15.51s
import time

start = time.time()

def hexagon_count(num):
    summary = 0
    i = 1
    while i * 3 <= num:
        k = num - i * 3 + 1
        summary += i * (k + 1) * k // 2
        i += 1
    return summary
low = 3
upp = 12345
summary = 0
for i in range(low, upp + 1):
    summary += hexagon_count(i)
print(summary)

end = time.time()

print(end - start)