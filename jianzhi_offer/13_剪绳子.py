# encoding: utf-8
"""
 @project:Data_Structure&&Algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/8/19 5:24 PM
 @desc: 给你一根长度为n的绳子，请把绳子剪成m段 (m和n都是整数，n>1并且m>1)每段绳子的长度记为k[0],k[1],...,k[m].
        请问k[0]*k[1]*...*k[m]可能的最大乘积是多少？
"""


class Solution:
    def maxProductAfterCutting(self, n):
        if n <= 3:
            return 1 * (n - 1)
        a = n % 3
        if a == 0:  # 能被3整除，直接全部划分为3
            return pow(3, n // 3)
        elif a == 1:  # 模为1，则划分出2个长度为2的段，其余全部为3
            return pow(3, (n - 4) // 3) * 4
        else:  # 模为2，则划分出1个长度为2的段，其余全部为3
            return pow(3, (n - 2) // 3) * 2


if __name__ == "__main__":
    sol = Solution()
    print(sol.max_product(8))
