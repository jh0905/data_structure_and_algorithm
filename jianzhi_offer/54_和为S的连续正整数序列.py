# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/7 22:25
 @desc:
"""


class Solution(object):
    # 暴力搜索，对搜索空间进行了优化
    def findContinuousSequence(self, sum):
        """
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1, sum // 2 + 1):  # i的最后一个取值是sum/2向下取整
            for j in range(i + 1, (sum + 1) // 2 + 1):  # j从i+1开始，j的最后一个取值是sum/2向上取整
                s = (i + j) * (j - i + 1) // 2  # 高斯求和公式
                if s == sum:
                    res.append(list(range(i, j + 1)))
        return res

    # 改进，双指针法
    def findContinuousSequence_2(self, sum):
        """
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        i = 1
        j = 2
        while i <= sum // 2 + 1 and j <= (sum + 1) // 2 + 1:
            s = (i + j) * (j - i + 1) / 2
            if s == sum:
                res.append(list(range(i, j + 1)))
                i += 1
                j += 1
            elif s < sum:
                j += 1
            else:
                i += 1
        return res


if __name__ == '__main__':
    print(Solution().findContinuousSequence(2))
