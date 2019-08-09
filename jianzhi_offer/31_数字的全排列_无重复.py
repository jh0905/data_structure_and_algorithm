# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/5 15:47
 @desc:
"""


class Solution:
    res = []
    holes = []

    def permutation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return self.res
        self.holes = [None] * len(nums)  # 初始化坑的状态
        self.dfs(nums, 0, 0)
        return self.res

    def dfs(self, nums, idx, state):
        """
        :param nums: 输入的数组
        :param idx: idx 表示当前待填入holes中的元素的下标
        :param state: 当前holes的状态，换成二进制表示，1表示已有元素，0表示暂无元素
        :return:
        """
        if idx == len(nums):
            self.res.append(self.holes.copy())
            return
        for i in range(0, len(nums)):
            if not state >> i & 1:  # 从右往左，第i个位置第值是否为1，从i=0开始
                self.holes[i] = nums[idx]
                self.dfs(nums, idx + 1, state + (1 << i))


if __name__ == '__main__':
    input_nums = [1, 2, 3]
    print(Solution().permutation(input_nums))
