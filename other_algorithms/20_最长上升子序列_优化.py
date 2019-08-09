# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/8 09:29
 @desc:
"""


class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        tails = []  # tails是一个递增数组，tails[i]存储所有长度为i+1的子序列中的尾部元素的最小值
        for num in nums:
            l = 0
            r = len(tails) - 1
            while l < r:
                mid = l + r >> 1
                if tails[mid] < num:  # 要找的元素，它的左边全部小于它，不包含mid
                    l = mid + 1
                else:
                    r = mid
            if not tails or tails[l] < num:  # tails数组中的所有元素均小于num，则将num添加到tails中
                tails.append(num)
            else:  # 否则把tails中，第一个大于num的元素修改为num
                tails[l] = num
        return len(tails)


if __name__ == "__main__":
    numbers = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    sol = Solution()
    print(sol.lengthOfLIS(numbers))
