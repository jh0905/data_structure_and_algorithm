# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/5 20:50
 @desc:
"""


class Solution(object):
    def numberOf1Between1AndN_Solution(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = []
        res = 0
        if not n:  # 输入为0
            return res
        while n:
            nums.append(n % 10)
            n //= 10
        nums.reverse()  # 1999 变为[1,9,9,9]
        for i in range(len(nums)):
            left = 0  # 第i个元素左边的数值,如i=2时,left=19
            right = 0  # 第i个元素右边的数值,如i=2时,right=9
            t = 0  # 第i个元素右边的元素个数
            for j in range(0, i):
                left = left * 10 + nums[j]
            for j in range(i + 1, len(nums)):
                right = right * 10 + nums[j]
                t += 1
            res += left * 10 ** t
            if nums[i] > 1:
                res += 10 ** t
            elif nums[i] == 1:
                res += right + 1
        return res


if __name__ == "__main__":
    input = 100
    print(Solution().numberOf1Between1AndN_Solution(input))
