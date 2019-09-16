# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/9/10 16:21
 @desc: 给定n个矩阵序列，(A1,A2,A3,A4,...,An). 计算他们的乘积：A1A2A3...An.

        由于矩阵的乘法运算符合结合律，因而可以通过调整计算顺序，从而降低计算量。
"""

"""
    样例分析：
    
    我们已知，矩阵A(m*n)与矩阵B(n*p)进行相乘：(可自行推导)
        乘法操作次数为：m*n*p
        加法操作次数为：m*p(n-1) 

    本题我们只考虑乘法操作次数作为计算量，分析下面实例：

    比如有三个矩阵，它们的shape分别为：A1:10*100, A2:100*5, A3:5*50
        - 按照(A1A2)A3的顺序计算，计算量为：10*100*5+10*5*50=7500次运算。
        - 按照A1(A2A3)的顺序计算，计算量为：100*5*50+10*100*50=75000次运算。

    可以发现：上面两种不同的运算顺序所有的计算量相差十倍。因而，一种最优的计算顺序将能很大程度的减少矩阵连乘的运算量。
"""

"""
    假设有 ABCD 四个矩阵连乘，它的最小乘法次数为：min{ A(BCD), (AB)(CD), (ABC)D}
          BCD的最小乘法次数为 min{(BC)D, B(CD)}
          ABC的最小乘法次数为 min{(AB)C, A(BC)}
    
    不难发现，涉及到递归的思想在里面,但是递归涉及到很多重复的计算，如上面就需要计算几次AB, BC, CD的运算次数。
    所以可以考虑动态规划的思想来做。
    
    以矩阵链ABCD为例:
        
        按照矩阵链长度递增计算最优值
        矩阵链长度为1时，分别计算出矩阵链A、B、C、D的最优值
        矩阵链长度为2时，分别计算出矩阵链AB、BC、CD的最优值
        矩阵链长度为3时，分别计算出矩阵链ABC、BCD的最优值
        矩阵链长度为4时，计算出矩阵链ABCD的最优值
    
    状态表示：dp[i][j] 从第i个矩阵开始到第j个矩阵结束的最少运算次数。
    状态转移：
           遍历i到j区间的值，找到一个最佳的切分点，dp[i][k]+dp[k+1][j] + 第i个矩阵的行*第k个矩阵的列*第j个矩阵的列
           求得一个最小值，作为dp[i][j]的值
    
    最终结果即为 dp[0][n-1]
"""


class Solution:
    def matrix_chain(self, matrices):
        """
        :param matrices: 列表，每一个元素表示矩阵的[行数, 列数]
        :return:
        """
        n = len(matrices)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):  # 有多少个长度为length的矩阵链,i为矩阵链中起始矩阵下标
                j = i + length - 1  # 当前矩阵链中，末尾矩阵的下标
                min_v = float('inf')
                for k in range(i, j):
                    cnt = dp[i][k] + dp[k + 1][j] + matrices[i][0] * matrices[k][1] * matrices[j][1]
                    min_v = min(min_v, cnt)
                dp[i][j] = min_v
        return dp[0][n - 1]


if __name__ == '__main__':
    mat = [[10, 100], [100, 5], [5, 50]]
    print(Solution().matrix_chain(mat))
