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
    # 解法一：动态规划法
    # 算法思路：
    #   我们把原问题分解成一个个的小问题，要计算f(n)的最大值，实际上是计算f(i)*f(n-i)的最大值
    #   于是我们需要遍历i=1,2,3,...,n//2,找到满足f(i)*f(n-i)最大的分割点
    #   第一反应可能是想到了递归，但是会有大量的重复计算，根据之前做递归的思路，我们改成由下而上的计算方式
    #   即计算出f(1),f(2),f(3),f(4),......，f(n)，保存在数组中，最终返回f(n)即可.
    #   需要注意的特殊情况就是，n=0,1,2,3时为特殊情况，我们得单独返回，不能用上面的数组返回!!!
    def max_product(self, n):
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        # 由于递归会有大量不必要的重复计算，因此这里从小而上的顺序，求解长度为n时的最大值f(n)
        # 于是f(0)=0,f(1)=1,f(2)=2,f(3)=3,...
        # 从0到n一共有n+1个元素，所以我们这里初始化(n+1)个点
        products = [0, 1, 2, 3] + [0] * (n - 3)
        for i in range(4, n + 1):
            max_value = 0
            # 我们将整体求最优问题转换成每个子问题求最优的形式，根据max{f(i)*f(n-i)}
            # 根据对称性，我们只需要遍历一半的元素即可，如f(5)的话，查找f(1)*f(4),f(2)*f(3)
            # 计算f(6)，用f(1)*f(5),f(2)*f(4),f(3)*f(3)
            for j in range(1, i // 2 + 1):
                product = products[j] * products[i - j]
                if product > max_value:
                    max_value = product
            products[i] = max_value
        return products[n]

    # 解法二：贪心算法
    # 算法思路：
    #   (1) 当n=0,1,2,3时，直接返回特定的值；
    #   (2) 当n=4时，把绳子减为两段长为2的绳子；
    #   (3) 当n>=5时，尽可能多的，减长度为3的绳子；（有数学理论证明）
    def max_product_2(self, n):
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        time_of_3 = n // 3  # n//3向下取整，统计绳子可以剪出多少个长度为3的绳子
        if n - 3 * time_of_3 == 1:  # 说明倒数第二根绳子长度为4，2*2>1*3，不再剪长为3的绳子
            return 3 ** (time_of_3 - 1) * 4
        elif n - 3 * time_of_3 == 2:  # 说明倒数第二根绳子长度为5，剪去3之后，还剩下长度2，最后再乘以2
            return 3 ** time_of_3 * 2
        else:  # 说明倒数第二根绳子长度为3，刚好剪完
            return 3 ** time_of_3


if __name__ == "__main__":
    sol = Solution()
    print(sol.max_product(10))
    print(sol.max_product_2(10))
