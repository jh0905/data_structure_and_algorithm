# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/23/19 1:02 PM
 @desc:给你六种面额 1、5、10、20、50、100 元的纸币，假设每种币值的数量都足够多，编写程序求组成N元（N为0~10000的非负整数）的不同组合的个数
"""
"""
 输入描述:输入包括一个整数n(1 ≤ n ≤ 10000)

 输出描述：输出一个整数，表示不同的组合方案数
 
 输入例子：1 
 输出例子：1

 输入例子：5 
 输出例子：2
"""


class Solution:
    """
     算法思路：
        我们分别考虑只用前1个硬币表示该数、只用前2个硬币表示该数、只用前三个硬币表示该数...、用所有硬币来表示
        硬币数组为 coins = [1,5,10,20,50,100]
        建立一个长为n+1的数组dp，初始化dp[0]=1，我们可以发现规律如下：
        只用第一个硬币表示某个数时，dp[1] = dp[2] = dp[3] = ... = dp[n] = 1
        用前2个硬币(1,5)来表示某个数时，dp[j] = dp[j] + dp[j - coins[1]]，前提是j>=coins[1]=5
        用前3个硬币(1,5,10)来表示某个数时，dp[j] = dp[j] + dp[j - coins[2]]，前提是j>=coins[2]=10
        依次类推下去
        用前6个硬币(1,5,10,20,50,100)来表示某个数，dp[j] = dp[j] + dp[j - coins[5]]，前提是j>=coins[5]=100

     ok,实现代码如下
    """

    def output(self, num):
        dp = [1] * (num + 1)  # 直接初始化全为1，那么后面的遍历直接从i=1开始
        coins = [1, 5, 10, 20, 50, 100]
        for i in range(1, 6):
            for j in range(num + 1):
                if j >= coins[i]:
                    dp[j] += dp[j - coins[i]]
        return dp[num]


if __name__ == '__main__':
    sol = Solution()
    number = int(input())
    print(sol.output(number))
