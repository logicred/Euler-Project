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

## Problem 2(Python, cost < 0.001s) ★★★★★
### Answer: 4613732

四百万以下的偶斐波那契数求和，直接采用递推公式计算斐波那契数（偶数每3个数出现一次），累和即可

## Problem 3(Python, cost = 0.017s) ★★★★★
### Answer: 6857

求一个大整数的最大质因子，基本想法是从小到大用各个质数除这个大整数，直到除不尽为止，当商为1时，即为最大正整数。

## Problem 4(Python, cost = 0.291s) ★★★★★
### Answer: 906609

求两个三位数的积构成的最大回文数，基本想法就是遍历900 * 900 = 810000 种可能，不过注意到该回文数必为11倍数，所以削减为原来搜索范围的1/11，然后直接搜索即可。

## Problem 5(Python, cost < 0.001s) ★★★★★
### Answer: 23279256

求1,...,20的最小公倍数。一个简单的想法是两两求最小公倍数，算法复杂度大概是log(N) * log(N),其实已经很快了。我在这时比较懒，所以直接用循环分解质因数求解，也省得写个辗转相除了。

## Problem 6(Python, cost < 0.001s) ★★★★★
### Answer: 25164150

计算100以内数平方和与和的平方之差，如果懒一点，直接用公式就好;如果勤奋些，可以写个循环累和。

## Problem 7(Python, cost = 0.569s) ★★★★★
### Answer: 104743

求第10001个质数，直接挨个搜寻，直到找到10001个为止


## Problem 9(Python, cost = 0.222s) ★★★★★
### Answer: 31875000

寻找一个直角三角形，使得其周长之和为1000.直接搜索未免范围太大，所以采用“两边之和大于第三边，两边之差小于第三边”进行约束，可以得到比较理想的搜索域。
然后直接暴力搜索即可。

## Problem 10(Python, cost = 1.69s) ★★★★
### Answer: 142913828922

打表求质数（一个个判断很慢），然后一个个累和即可

## Problem 12(Python, cost = 0.485s) ★★★★★
### Answer: 76576500

题目需要求拥有超过500因子的三角数(n * (n + 1) / 2),那么如果对三角数进行一个个因子的试除比较慢，所以采用 因子个数 = (x1 + 1) * ... * (xn + 1)，其中x1,...,xn为其质因数分解的各质因子的幂次，加上超过500因子，所以该数一定大于250^2(考虑因子成对)，进一步压缩搜索范围，然后开始搜索即可。


## Problem 14(Python, cost =39.7s) ★★★
### Answer: 837799

求解collatz猜想(又称冰雹猜想)中1000000以内，雹程最长的数。一个朴素的想法是挨个计算每个数的雹程;另一种想法就是一条一条递归计算(只记录起始数及其雹程)，两种方法不清楚谁会更快。

## Problem 15(Python, cost = 0.002s) ★★★★★
### Answer: 137846528820

首先考虑上方和左方的边结点，显然只有一条路可以走，所以标记为1；接下来考虑中间的节点，可以发现到达其路径条数为其上方和左方节点路径数之和，所以通过简单的递推就可以求解。

## Problem 18(Python, cost = 0.017s) ★★★★★
### Answer: 1074

金字塔内寻找路径和最大的路径，采用DFS简单搜索即可得出结果。

## Problem 21(Python, cost = 0.138s) ★★★★★
### Answer: 36126

寻找10000以下亲和数(数A的因子和是数B, 数B的因子和是数A)之和。其实只要记录每个数的因子和，然后两两比较（排序也可）就可以找出亲和数，最后累和即可。

## Problem 22(Python, cost = 0.0289s) ★★★★★
### Answer: 871198282

输入文件，统计每个名字根据题设所得分数，最后累和即可

## Problem 27(Python, cost = 0.873s) ★★★★★
### Answer: -59231

暴力求解即可

## Problem 28(Python, cost < 0.001s) ★★★★★
### Answer: 665168997

数列求和问题，简单暴力求解即可

## Problem 29(Python, cost = 0.0110s) ★★★★★
### Answer: 9183

根据python集合（set）元素互异的特性，直接计算所有值并置于同一集合中，取集合大小即为答案

## Problem 31(Python, cost = 0.050s) ★★★★★
### Answer: 73682

问题也即求解不定方程:x1 + 2x2 + 5x3 + 10x4 + 20x5 + 50x6 + 100x7 = 200 的整数解，简单想法用贪心/递归都可以实现。

## Problem 35(Python, cost = 8.84s) ★★★★
### Answer: 55

## Problem 38(Python, cost = 0.0638s) ★★★★★
### Answer: 932718654

## Problem 44(Python, cost = 38.7s) ★★★
### Answer: 5482660

## Problem 45(Python, cost = 0.056s) ★★★★★
### Answer: 1533776805

这题的目标是找到一个大于40755的数X,使其满足X = N * (N - 1) / 2 = M * (3 * M - 1) / 2 = L * (2 * L - 1).单纯一个个算出来比对是不靠谱的，我们显然可以发现，最后一种表示方式增长最快(分布最稀疏)，而且令L = 2 * N就可以发现第一种和第三种表示是相同的。因此我们将它作为标准，代入方程，反解出M,看是不是正整数即可。

## Problem 46(Python, cost = 0.095s) ★★★★★
### Answer: 5777

题目要求找出最小的奇合数n，使得其不能写成n = p + 2 * p ^ 2(p为素数)的形式。显然，在对素数打表的过程中，我们可以一次标注出素数和奇合数来。通过观察可以发现，对于每个奇素数n，使得该式成立的p必小于n的算术平方根。在前述条件下直接依次搜索即可。

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
