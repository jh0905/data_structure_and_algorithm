# encoding: utf-8
"""
 @project:Data_Structure&&Algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/9/19 8:43 PM
 @desc: 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号
"""


class Solution:
    """
     算法思路，以13+11为例：

        13的二进制 ：  1 1 0 1            -----a   13
        11的二进制 ：  1 0 1 1            -----b   11

        (a&b)<<1 : 1 0 0 1 0            -----c   18
        a^b      : 0 0 1 1 0            -----d   6

        (c&d)<<1 : 0 0 1 0 0            -----e   4
        c^d      : 1 0 1 0 0            -----f   20

        (e&f)<<1 : 0 1 0 0 0            -----g   8
        e^f      : 1 0 0 0 0            -----h   16

        (g*h)<<1 : 0 0 0 0 0            -----i   0      ----退出循环
        g^h      : 1 1 0 0 0            -----j   24     ----输出结果

    程序的基本代码如下：
        while num1!=0:
            temp = ((num1 & num2) << 1)
            num2 = (num1 ^ num2)
            num1 = temp
        return num2

    但是，根据我们前面的学习，Python长整数类型可以表示无限位，所以需要人为设置边界，避免死循环，我们这里需要把它控制在32位，故实际做的时候
    加了一层转换，限制边界。

    """

    def Add(self, num1, num2):
        while num2:
            sum = (num1 ^ num2) & 0xffffffff  # 转为正数，但是对应的32位的数不变
            carry = (num1 & num2) & 0xffffffff
            num1 = sum
            num2 = carry << 1
        if not num1 << 31 & 1:  # 如果小于这个值011...111（31个1），说明num2为正数，直接返回
            return num1
        else:
            # 否则说明num2为负数，因为我们之前限定了边界（0xffffffff），转成了正值，所以要做处理，还原成原来的负数
            # num2为负数，32位之前的二进制位都为1，num2 ^ 0xffffffff截取后32位
            # 异或操作，相同为0，不同为1，这里把num2的后32位相当于全部按位取反，32位之前的同为0，仍然是0
            # 按位取反，把num2全部按位取反，也就还原了整个负数
            # 整个思路是一个32位取反，再所有位都取反的过程.
            return ~(num1 ^ 0xffffffff)


if __name__ == '__main__':
    sol = Solution()
    print(sol.Add(-4, 2))

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
