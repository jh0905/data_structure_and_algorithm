# encoding: utf-8
"""
 @project:Data_Structure&&Algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/9/19 8:43 PM
 @desc: 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号
"""


class Solution:
    def add(self, num1, num2):
        while num2:
            sum = (num1 ^ num2) & 0xffffffff  # 限制为32位，但是对应的32位的数不变
            carry = ((num1 & num2) << 1) & 0xffffffff
            num1 = sum
            num2 = carry
        if num1 < 0x7fffffff:  # 如果小于这个值011...111（31个1），说明num2为正数，直接返回
            return num1
        else:
            return ~(num1 ^ 0xffffffff)


if __name__ == '__main__':
    sol = Solution()
    print(sol.add(-4, 2))

"""
 拓展：
    不用temp变量，交换两个整数的值
    (1)加减法
        a = a + b
        b = a - b
        a = a - b
    
    (2)异或运算
        a = a ^ b
        b = a ^ b
        a = a ^ b   （基于 a ^ b ^ a = b的原理）
"""
