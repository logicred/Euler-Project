# Euler-Project
My solutions and programs on Euler Project Problem

# 评等要求

★:算法应当能成功作答，但囿于太过复杂导致无法在可接受时间内完成

★★:成功作答，但运行时间超过60s

★★★:成功作答，并且运行时间在60s以内(Euler Project要求)

★★★★:成功作答，并且运行时间在10s以内

★★★★★:成功作答，并且运行时间在1s以内

# 问题列表

## Problem 1(Python, cost < 0.001s) ★★★★★
### Answer: 233168

统计1000以内3或5的倍数之和，直接搜索一遍1000以内的数即可，非常简单

## Problem 22(Python, cost = 0.0289s) ★★★★★
### Answer: 871198282

输入文件，统计每个名字根据题设所得分数，最后累和即可

## Problem 29(Python, cost = 0.0110s) ★★★★★
### Answer: 9183

根据python集合（set）元素互异的特性，直接计算所有值并置于同一集合中，取集合大小即为答案

## Problem 35(Python, cost = 8.84s) ★★★★
### Answer: 55

## Problem 38(Python, cost = 0.0638s) ★★★★★
### Answer: 932718654

## Problem 44(Python, cost = 38.7s) ★★★
### Answer: 5482660

## Problem 47(Python, cost = 0.196s) ★★★★★
### Answer: 134043
这是一个非常朴素的题目，题目让我们找出最小且连续的4个正整数，使得每个正整数都恰有4个互异的正因子。

思路也非常明确，直接打表搜索1-MAX(MAX为人为规定上界)内的正整数互异正因子个数，然后再跑一遍全列表，判断连续4个数是否满足题设。

其实还有可以提升的地方，比如在寻找连续4个数时，用KMP算法的思想会更快一些，不过也已经达到了设定最高要求，有兴趣的话可以改进一下。

## Problem 53(Python, cost = 0.0152s) ★★★★★
### Answer: 4075

计算组合数的关键在于计算，如果单纯采用计算阶乘的方法，显然是十分复杂的，而且每个数都要计算一遍，会占用很多时间。
在这里我们采用杨辉三角来递推组合数，不难证明，杨辉三角第N行从左数第M个对应于组合数C（N，M），而C（N，M）= C（N - 1, M）+ C（N - 1, M - 1）
那么很快就可以计算出来，再根据题设条件计数就好。

## Problem 55(Python, cost = 0.0927s) ★★★★★
### Answer = 249

## Problem 56(Python, cost = 0.357s) ★★★★★
### Answer = 972

## Problem 62(Python, cost = 9.65s) ★★★★
### Answer = 127035954683

## Problem 63(Python, cost < 0.001s) ★★★★★
### Answer = 49

## Problem 69(Python, cost < 0.001s) ★★★★★
### Answer = 510510

## Problem 76(Python, cost = 118s) ★★
### Answer = 190569291

## Problem 92(Python, cost = 58.1s) ★★★
### Answer = 8581147

## Problem 97(Python, cost = 0.454s) ★★★★★
### Answer = 8739992577
