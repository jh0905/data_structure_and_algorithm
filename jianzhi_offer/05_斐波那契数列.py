# encoding: utf-8
"""
 @project:Data_Structure&&Algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/4/2 00:11
 @desc: 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）
"""


class Solution:
    # 算法思路: 迭代法
    # 先初始化斐波那契数列的前两个元素0，1
    # 然后再用循环的思想，逐个求出下面每个元素的值，循环与递归一般是可以相互转化的，循环时间复杂度较低
    def Fibonacci(self, n):
        fib_numbers = [0, 1] + [0] * (n - 1)
        if n < 2:
            return fib_numbers[n]
        else:
            for i in range(2, n + 1):
                fib_numbers[i] = fib_numbers[i - 2] + fib_numbers[i - 1]
            return fib_numbers[n]
        # 经典的思路是用递归的思想，f(n) = f(n-1)+f(n-2),但是时间复杂度太高，为O(2^n)
        # 换成上面循环思想，时间复杂度为O(n)


# 递归做法
# class Solution:
#     # 算法思路：递归思想，f(n) = f(n-1)+f(n-2)，比较简洁，但是复杂度为O(n^2)
#     def Fibonacci(self, n):
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)


if __name__ == '__main__':
    sol = Solution()
    print(sol.Fibonacci(10))
