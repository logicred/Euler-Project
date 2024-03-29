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

## Problem 13(Python, cost < 0.001s) ★★★★★
### Answer: 5537376230

利用python简单求和……然后取最高10位为结果即可。

## Problem 14(Python, cost =39.7s) ★★★
### Answer: 837799

求解collatz猜想(又称冰雹猜想)中1000000以内，雹程最长的数。一个朴素的想法是挨个计算每个数的雹程;另一种想法就是一条一条递归计算(只记录起始数及其雹程)，两种方法不清楚谁会更快。

## Problem 15(Python, cost = 0.002s) ★★★★★
### Answer: 137846528820

首先考虑上方和左方的边结点，显然只有一条路可以走，所以标记为1；接下来考虑中间的节点，可以发现到达其路径条数为其上方和左方节点路径数之和，所以通过简单的递推就可以求解。


## Problem 16(Python, cost < 0.001s) ★★★★★
### Answer: 1366

计算2 ^ 1000的各位数字和……没啥技巧，利用python自带的大整数计算，然后逐个数位累和即可，没啥技术含量。

## Problem 18(Python, cost = 0.017s) ★★★★★
### Answer: 1074

金字塔内寻找路径和最大的路径，采用DFS简单搜索即可得出结果。

## Problem 19(Python, cost < 0.001s) ★★★★★
### Answer: 171

计算20世纪内星期日的个数，一个简单的想法就是直接遍历计数，需要注意的一个问题是闰年，其他都很简单。

## Problem 21(Python, cost = 0.138s) ★★★★★
### Answer: 36126

寻找10000以下亲和数(数A的因子和是数B, 数B的因子和是数A)之和。其实只要记录每个数的因子和，然后两两比较（排序也可）就可以找出亲和数，最后累和即可。

## Problem 22(Python, cost = 0.0289s) ★★★★★
### Answer: 871198282

输入文件，统计每个名字根据题设所得分数，最后累和即可

## Problem 26(Python, cost = 0.323s) ★★★★★
### Answer: 983

题目要求1000以内使得倒数的循环节最长的正整数。这道题可以用KMP算法求解，但是由数论的结论可以得知b进制下循环节长度为$ord_u b$(u为分母与b互质的最大因子),而整数的阶$ord_u b$是使得$b^x = 1 (mod u)$最小的正整数x，穷举都行。

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

## Problem 33(Python, cost = 0.019s) ★★★★★
### Answer: 100

遍历所有数即可。

## Problem 35(Python, cost = 8.84s) ★★★★
### Answer: 55

## Problem 38(Python, cost = 0.0638s) ★★★★★
### Answer: 932718654

遍历即可……没啥好说的

## Problem 42(Python, cost = 0.007s) ★★★★★
### Answer: 162

文件I/O，统计TXT中，满足特定规则的单词数。没什么难点，直接遍历就可以。

## Problem 44(Python, cost = 38.7s) ★★★
### Answer: 5482660

题目要求寻找形如M = N * (3 * N - 1) / 2的正整数PI和PJ，使得|PI - PJ|也满足以上形式，而且|PI - PJ|最小。显然直接搜索就可以，需要注意的是当求出差值验证时，只需要验证下一个|PI-PI-1|即可。

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

## Problem 49(Python, cost = 0.913s) ★★★★★
### Answer: 296962999629

题目要求找出3个四位数，它们都是质数，并且构成等差数列，而且每个数包含的数字及其个数均相同，并且不是，输出从小到大排列成的12位结果。一个很自然的想法就是从4位质数中搜寻结果，然后直接穷举就可以。需要注意的是，最好在内循环就做剪枝，不然时间复杂度会较高。

## Problem 53(Python, cost = 0.0152s) ★★★★★
### Answer: 4075

计算组合数的关键在于计算，如果单纯采用计算阶乘的方法，显然是十分复杂的，而且每个数都要计算一遍，会占用很多时间。
在这里我们采用杨辉三角来递推组合数，不难证明，杨辉三角第N行从左数第M个对应于组合数C（N，M），而C（N，M）= C（N - 1, M）+ C（N - 1, M - 1）
那么很快就可以计算出来，再根据题设条件计数就好。

## Problem 55(Python, cost = 0.0927s) ★★★★★
### Answer = 249

题目要求求解10000以下的Lychrel数(通过不超过50次迭代——该数和其逆序数相加，最终能得到回文数的数)，没有什么难度，简单的挨个判断过去即可。

## Problem 56(Python, cost = 0.357s) ★★★★★
### Answer = 972

## Problem 62(Python, cost = 9.65s) ★★★★
### Answer = 127035954683

计算这样一个数：它各数位上的数字形成的排列组合中，恰好有5个数是完全立方数。一个简单的想法就是从立方根入手，一个个遍历，并且保存对应立方的数值进行比较即可。

## Problem 63(Python, cost < 0.001s) ★★★★★
### Answer = 49

计算有多少组(a, N)满足这样的条件：其N次幂为N位数。首先考虑这个问题的边界：10 ^ (N - 1) <= a ^ N < 10 ^ N, 显然a < 10且(N - 1) / N <= lg a,在这样的条件下穷举很快就可以得出结果。 

## Problem 65(Python, cost < 0.001s) ★★★★★
### Answer = 272

计算e的连分数近似式第100项分母各位数字之和，根据递推就可以得到相应分子分母，直接加和就可。

## Problem 69(Python, cost < 0.001s) ★★★★★
### Answer = 510510

求解当n ≤ 1000000时使得n/φ(n)最大的n,根据欧拉函数的性质，我们可以得出n/φ(n) = Π(p / (p - 1)),显然p越小时p / (p - 1)越大，所以只要选取尽可能小的p连乘即可，也即求最大的n = 2 * 3 * 5 * 7 * ... * p <= 1000000(p为质数)，很容易求解。

## Problem 73(Python, cost = 4.79s) ★★★★
### Answer = 7295372

求解1/3至1/2之间，分母小于12000的最简真分数的个数，一个很自然的想法，当分母为M时，显然分子>1/3M，小于1/2M，之后直接遍历区间，寻找使得分子分母互质（gcd == 1）即可。如果追求更快的速度，可以尝试打表。

## Problem 76(Python, cost = 118s) ★★
### Answer = 190569291

求解100能够被写成不同数字之和的方式总数，一个很自然的想法就是递归，设res(100,100)-1为结果，其中后一个100代表拆解的最大数为100，显然res(100,100) = res(100, 99) + res(100, 98) + ... + res(100, 1);对于res(100, 99) = res(99, 1),而对于res(100, 2) = res(98, 2) + res(2, 1),由此就可以求解。不过速度很慢，看论坛似乎有一种递推的方法，然而并没有看懂，还望大佬教我ORZ。

## Problem 80(Python, cost = 0.176s) ★★★★★
### Answer = 40886

题目要求计算100内非完全平方数，其平方根结果的前100位数字之和的累加(实在是比较拗口)。一个很简单的想法是直接利用python不限位数的计算，然而很可惜精度不足。所以说要努力将平方根求解化归为大整数运算，采用二分搜索寻找结果。考虑到算法量级为log2(n), n = √m * 10 ^ 100, 所以实际运算复杂度还好，直接求解即可。

## Problem 85(Python, cost = 0.029s) ★★★★★
### Answer = 2772

题目要求计算一个网格中长方形的个数最接近2000000的长方形面积大小。第一个考虑是对边界进行预估，考虑到长方形长宽互换情况相同，不妨假定长a,宽b且a > b。
一个极限考虑是一个b = 1的长方形，若要接近目标，其上限为n = 2000(此时长方形总数为2000 * (2000 + 1) / 2 > 2000000)，因此可以得出n = 2000 > a > b是我们的搜索域。 
这样显然是不太好的，因为计算量大约是O(n ^ 3)，我们需要进一步压缩。想到当a确定时，长方形个数关于b单调递增，于是我们可以关于b采用二分搜索的方法，这样就将运算量降至O(n ^ 2 * log n)，可喜可贺。
最后一点是关于长方形个数计算的，不难发现长方形总数为a * (a + 1) / 2 * b * (b + 1) / 2，可以实现常数级运算。

## Problem 87(Python, cost = 1.701s) ★★★★
### Answer = 109743

本题目的在于求解50 000 000以下一类数的个数，这类数能够写成a = x ^ 2 + y ^ 3 + z ^ 4(x, y, z均为质数)的形式，一个简单的想法就是x, y, z必不超过√50 000 000,所以简单求解其中的质数，进行穷举即可。要注意的是，最好根据上限适当剪枝，提升运算效率。

## Problem 92(Python, cost = 58.1s) ★★★
### Answer = 8581147

一个迭代过程，事实证明最后总会落入1或89的无限循环中，需要计算的是10000000以下最终会落入89的数。一个简单的思路就是沿着迭代过程去找，为了避免迭代造成爆栈，最好用个List记录一下，也能提高运行速度。

## Problem 94(Python, cost = ?) ?
### Answer = ?

?

## Problem 97(Python, cost = 0.454s) ★★★★★
### Answer = 8739992577

计算给定梅森素数的最后10位数，如果懒一些直接利用python自带的大整数运算就好，勤劳一点每次对10 ^ 10取余可以显著减少运算量，直接计算即可。

## Problem 99(Python, cost = 0.003s) ★★★★★
### Answer = 709

计算一组底数和指数给定的数据中，哪一行拥有最大的数值。只需要读入数据，将其取对数，就可以进行直接比较。

## Problem 102(Python, cost = 0.022s) ★★★★★
### Answer = 228

题目要求计算出在题目给出的一些点对中，到底有多少能够构成内部含有原点的三角形。一个很自然的想法就是采用向量的方式来判别内部和外部，然而作者并没有这么做，而是采用这样一个方式：原点包含在三角形内，当且仅当 原点和三个顶点中的两个构成的三角形面积之和均恒为正数且等于原三角形的面积，而三角形的面积可以通过顶点构成的行列式直接求得，避免一些冗杂的运算。

## Problem 104(Python, cost = 15.9s) ★★★
### Answer = 329468

计算K值，使得第K个斐波那契数满足以下条件：末尾9个数字遍历1-9且，首位9个数字遍历1-9。如果直接搜索的话，在K <= 100,000时已经相当吃力，2-3分钟肯定是别想跑出来的，所以考虑先用第一个条件限制搜索范围，第一个条件只要对整个数列做取1,000,000,000的模，还是很快出结果的(K <= 1,000,000时只有300多个符合要求)。然后再在这些数中进行搜索，值得注意的问题是……太大了，大到python都会爆出result too large的错误，所以考虑每次只保留前18位进行运算，这样即使有误差也能够接受，然后直接搜索即可。

## Problem 120(Python, cost < 0.001s) ★★★★★
### Answer = 333082500

题目要求Σ R(a)max(3 <= a <= 1000), 其中R(a)max为对于所有n, (a + 1) ^ n + (a - 1) ^ n mod (a ^ 2)的最大值。可以由二项式展开显然看到，当a为奇数时，R(a)max = a * (a - 1); 当a为偶数时，R(a)max = a * (a - 2), 求和即可。

## Problem 145(Python, cost = 254.4s) ★★
### Answer = 608720

无他，穷举耳。（但是可以证明一个九位数不可能是符合该条件的，所以搜索范围压缩到10 ^ 8）

## Problem 173(Python, cost = 0.996s) ★★★★★
### Answer = 1572729

题目要求计算1000000以下这样的数N（能被表示为至少两种以上的平方差形式，即N = A^2 - B^2,A > 0 且B > 0）表示形式的总数。显然N是4的倍数，而表示形式的数量正好是N的所有小于N ^ (1/2)因子的个数，所以简单求和就好。

## Problem 203(Python, cost = 0.004s) ★★★★★
### Answer = 34029210557338

题目要求计算杨辉三角中前51行，不重复且不能被质数的平方整除的数之和。用递推算法打出杨辉三角，注意到杨辉三角中的数都是组合数的形式，意味着前51行中的质因子都在50以内，因此只要检验50以内的质数平方即可，注意不重复即可。

## Problem 205(Python, cost = 0.996s) ★★★★★
### Answer = 1572729

题目要求计算1000000以内，能够满足不同地砖铺设方法的种类。考虑到正方形的对称性，可以得到这样的数N必然是4的倍数，而且N的每一对因子(D, N / D)构成一种铺设方法，显然D = N / D时是不满足题设的，从而统计每个N的因子数即可。需要注意的是，注意每个数N计算的消耗，采用打表的方式可能会有很好的提升。

## Problem 206(Python, cost = 12.8s) ★★★
### Answer = 1389019170

本题目的是要求一个给定的正整数使其为一个完全平方数。根据题意，可以发现直接搜索的范围是10 ^ 9，这个代价比较大，需要进行剪枝。可以发现末尾是0，所以根据完全平方数的性质，可以得出最后一个空位应该是0，也可递推出倒数第二个空位只能是3或7，这样就缩小了20倍，最后我们对其开根号的结果进行搜索而不是原数搜索，同样可以减小搜索范围，得到一个比较好的结果。

## Problem 346(Python, cost = 3.44s) ★★★★
### Answer = 336108797689259276

本题目的是求在不同进制下能够被表征为全1序列的正整数之和。显然自然数N显然能在N - 1进制下满足此要求，于是只需要再寻求另一种不同进制的情况即可。考虑到N = 1 + A + ... + A ^ M(M > 1)为其充要条件，因此可以将其化归为等比数列求和问题。然而还有一个问题，那就是重复计算的问题，例如31 = 1 + 2 + 4 + 8 + 16 = 1 + 5 + 25，令人头疼。但是如果逐个计算……那么范围在10 ^ 9时所需时间 > 1s，达到题设要求大概需要1000s以上，很难让人接受。根据Goormaghtigh猜想，31和8191是唯一的两个特例，因此把他们挑出来之后就可以大胆使用上述方法了。

## Problem 357(Python, cost = 181s) ★★
### Answer = 1739023853137

本题目的是求在100000000以内的N使得N的每个因子D满足D+N/D为质数的N之和，显然D=1时，要求N+1为质数；D=2时，要求2+N/2为质数，通过这些可以压缩搜索域，虽然速度不咋地，但是凑合着看吧。

## Problem 401(Python, cost = 59.7s) ★★★
### Answer = 281632621

本题目定义了一个因子平方和函数sigma2(N),它可以计算N所有因子的平方和。现在要求的是SIGMA2(N) = sigma2(1) + ... + sigma2(10 ^ 15) mod 10 ^ 9的结果。如果直接加和……那么大概在10^4左右就暴毙(cost = 1 min);如果聪明一些考虑到因子从10 ^ 15 / 2 + 1 ~ 10 ^ 15都出现了1次，10 ^ 15 / 3 + 1 ~ 10 ^ 15 / 2都出现了2次，以此类推加和，那么大概可以提升到10^8~9左右(cost = 1 min);如果更聪明一些，用平方和公式降低运算复杂度，那么就能在规定时间内完成题设要求了。

## Problem 504(Python, cost = 161.3s) ★★
### Answer = 694687

本题目的是求给定参数范围，使得格点四边形ABCD内部的格点数为完全平方数的四边形个数。由题意可知1<= a, b, c, d <=100，如果直接进行求解，大概是10 ^ 8种情况，很可惜，这次我也不知道怎么剪枝(或者说我想到的剪枝方法都很麻烦，未必比不剪枝会好)。我们主要把精力放在如何计算上来，根据格点多边形面积公式，我们可以得到“边界格点数/2 + 内部格点数 - 1 = 面积”，面积 = (a + c)(b + d) / 2，而边界格点之和恰好为gcd(a, b) + gcd(b, c) + gcd(c, d) + gcd(d, a)。为了进一步提升效率，我们可以对gcd值打表，进一步提升效率。(虽然我至今不明白别人写的跟我没啥差别，但就在论坛上说能跑进1s)。

## Problem 577(Python, cost = 15.51s) ★★★
### Answer = 265695031399260211

求题设所给的三角形内部的正六边形数量之和。通过分析可以得知，一个边长为N的正六边形内部，可以内接N种不同的正六边形，而且当三角形边长M >= 3N时该正六边形存在，且个数为N * (M - 3N + 1) * (M - 3N + 2) / 2，直接累加就可以。

## Problem 587(Python, cost = 0.006s) ★★★★★
### Answer = 2240

一个很简单的问题，根据积分计算一下两部分面积之比，依次迭代就行。如果追求速度，可以用forward-backward二分查找，不过依次查找速度也不慢了。

## Problem 613(Python, cost = ?) ★★★★★
### Answer = 0.3916721504

本题目的要求一个小蚂蚁在一个直角三角形内随机位置，沿着随机方向爬行，求出其从斜边爬出的概率。通过简单计算就可以得出，设蚂蚁初始位置为O(x, y),三角形三个顶点分别为A(0, b), B(a, 0), C(0, 0)。我们连结AO,BO,CO,并认为蚂蚁从三边爬出的概率和其角度成正比。从而我们可以得出公式，直接计算积分结果即可。
