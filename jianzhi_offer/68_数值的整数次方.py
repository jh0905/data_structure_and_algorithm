# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/12 11:01
 @desc:
"""


class Solution:
    def Power(self, base, exponent):

        """
         * 1.全面考察指数的正负、底数是否为零等情况。
         * 2.写出指数的二进制表达，例如13表达为二进制1101。
         * 3.举例:10^1101 = 10^0001*10^0100*10^1000。
         * 4.通过&1和>>1来逐位读取1101，为1时将该位代表的乘数累乘到最终结果。
        """
        is_nagative = False
        if exponent > 0:
            n = exponent
        elif exponent == 0:
            return 1
        else:
            is_nagative = True
            n = - exponent
            if base == 0:
                return None
        ans = 1
        while n:
            if n & 1:
                ans *= base
            base *= base  # 精髓，对应着右移一位
            n = n >> 1
        return ans if not is_nagative else 1 / ans
