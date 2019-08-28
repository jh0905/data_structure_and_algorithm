# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/24 13:15
 @desc: 第90题     输入的list中，存在重复元素，输出所有子集的list
"""


class Solution:
    res = []
    sub = []

    def subsetsWithDup(self, nums):
        if not nums:
            return []
        self.res = []
        self.sub = []
        self.dfs(sorted(nums), 0)
        return self.res

    def dfs(self, nums, idx):
        if idx == len(nums):
            self.res.append(self.sub.copy())
            return
        # 统计当前枚举数字的个数
        k = 0
        while idx + k < len(nums) and nums[idx + k] == nums[idx]:
            k += 1
        # 考虑往集合中加入，0，1，2，... ,k 个 nums[idx]
        for i in range(k + 1):  # 枚举区间要弄清楚是0到k，所以这里填k+1
            self.sub.extend(i * [nums[idx]])
            self.dfs(nums, idx + k)
            while i:
                self.sub.pop()
                i -= 1


if __name__ == '__main__':
    print(Solution().subsetsWithDup([1, 2, 2]))
