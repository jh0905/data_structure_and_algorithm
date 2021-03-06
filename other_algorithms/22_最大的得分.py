# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/9/16 09:19
 @desc: 有 n 个数字排成一排，你和对手每次只能从排头或者排尾选取一个数字，直到 n 个数取完为止，双方的得分为取走的数之和。
        假设对手足够聪明，问 从你开始取数，最多能得多少分？
"""

"""
    解题思路：区间DP
    
    举几个简单的例子：
        (1) 对于序列 [1, 100]:
            先手一定取100，后手只能取1。
            
        (2) 对于序列 [10, 100, 2, 1]:
            先手第一步可以取出10或者1，但是如果先手取10，那么后手下一轮会取走100，先手得不偿失，所以先手第一步取1；
            此时序列变成：[10, 1000, 2], 这时候后手不论怎么取，先手在下一轮一定会取走100。
            所以最后先手取出的总和为101，后手为12。
            
    解法：考虑先手和后手在序列 a[0], a[1], a[2],... ,a[n-1]上进行博弈：
         (1) 如果先手取走了a[0]，那么问题转化成两人在 a[1],a[2],...,a[n-1]上博弈
         (2) 如果先手取走了a[n-1]，那么问题转化成两人在 a[0], a[1],...,a[n-2]上博弈
         
    状态表示：
        dp[l][r]表示两人在序列a[l],a[l+1],...,a[r]上进行博弈时，先手所能取到的最大分数
    
    状态转移：
        如果先手取走a[l],那么后手所能取得的最大分数为 dp[l+1][r]
        如果先手取走a[r],那么后手所能取得的最大分数为 dp[l][r-1]
        所以先手所能获得的最大价值为：(假设a[l]+a[l+1]+...+a[r]的和为s)
            max(s-dp[l+1][r], s-dp[l][r-1])
        即：
            s - min(dp[l+1][r], dp[l][r-1])
    
    初始化：
        当l和r相等时，dp[i][i] = a[i]
    
    算法模拟： [4, 7, 2, 9, 5, 2]
    
    (1) dp[0][0]=4, dp[1][1]=7, dp[2][2]=2, dp[3][3]=9, dp[4][4]=5, dp[5][5]=2
    (2) dp[0][1]=7, dp[1][2]=7, dp[2][3]=9, dp[3][4]=9, dp[4][5]=5
    (3) dp[0][2]=6, dp[1][3]=11, dp[2][4]=7, dp[3][5]=11
    (4) dp[0][3]=16, dp[1][4]=16, dp[2][5]=11
    (5) dp[0][4]=11, dp[1][5]=14
    (6) dp[0][5]=18 
"""


class Solution:
    def max_score(self, n, nums):
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for i in range(1, n):  # 表示区间长度
            for j in range(n - i):  # 枚举区间的起点
                dp[j][j + i] = sum(nums[j:j + i + 1]) - min(dp[j + 1][j + i], dp[j][j + i - 1])
        return dp[0][-1]


if __name__ == '__main__':
    _n = int(input())
    _nums = list(map(int, input().split()))
    print(Solution().max_score(_n, _nums))
