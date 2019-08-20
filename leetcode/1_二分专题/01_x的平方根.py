# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/16 09:00
 @desc: 第69题
"""

"""
二分法流程：
    1.确定二分的边界
    2.编写二分的代码框架
    3.设计check函数 (mid ** 2 > x)
    4.判断区间如何更新
"""


class Solution:
    def sqrt(self, x):
        l = 0
        r = x
        while l < r:
            mid = l + r + 1 >> 1
            if mid > x / mid:  # 两个整数相乘，可能会溢出，所以写成左边形式
                r = mid - 1
            else:
                l = mid
        return l


if __name__ == '__main__':
    print(Solution().sqrt(225))
