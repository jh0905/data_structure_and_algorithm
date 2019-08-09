# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/5 14:43
 @desc:
"""


class Solution:
    res = []
    path = []

    def permutation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return self.res
        self.path = [None] * len(nums)
        sorted(nums)  # 排完序，保证重复的元素相邻
        self.dfs(nums, 0, 0, 0)
        return self.res

    def dfs(self, nums, idx, start, state):
        """
        :param nums: 输入的数组
        :param idx: idx 表示当前待填入坑中的元素的下标
        :param start: 当前元素应该从哪个位置开始枚举
        :param state: 当前"坑"的状态，换成二进制表示，1表示已有元素，0表示暂无元素
        :return:
        """
        if idx == len(nums):
            self.res.append(self.path.copy())
            return
        if idx == 0 or nums[idx] != nums[idx - 1]:
            start = 0  # 如果开始枚举第一个元素，或者当前元素与上一个元素不重复，则从第0个坑开始枚举
        for i in range(start, len(nums)):
            if not state >> i & 1:  # 从右往左，第i个位置第值是否为1，从i=0开始
                self.path[i] = nums[idx]
                self.dfs(nums, idx + 1, i + 1, state + (1 << i))


if __name__ == '__main__':
    nums = [1, 2, 2]
    print(Solution().permutation(nums))
