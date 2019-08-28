# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/23 16:14
 @desc: 第47题
"""

"""
    解题思路：
        在前面无重复元素全排列的基础上，我们增加了一些限制
        
        首先是要对数组进行排序，这样可以使得相邻元素相邻，然后进行dfs操作，传入四个参数
            nums: 有序的数组
            idx: 当前遍历的元素
            start: 当前遍历元素从哪个位置开始搜索可以填的"坑"
            state: 当前"坑"的状态
        
        dfs具体过程：
            
            首先判断idx是否等于数组长度，是的话，说明当前深搜已经完成，可以将结果存到res中
            
            否则判断待枚举的"坑"的起点，如果 idx大于0且nums[idx]!=nums[idx-1]的话，那么枚举起点设为0，否则就是上一个元素的后一位
            
            具体枚举过程的代码和无重复全排列相似。
"""


class Solution:
    res = []
    holes = []

    def permuteUnique(self, nums):
        if not nums:
            return []
        nums = sorted(nums)  # 排完序之后，重复元素相邻
        self.res = []
        self.holes = [0] * len(nums)
        self.dfs(nums, 0, 0, 0)
        return self.res

    def dfs(self, nums, idx, start, state):
        """
        :param nums:
        :param idx: 当前遍历的元素
        :param start: 当前遍历元素从哪个位置开始搜索可以填的"坑"
        :param state: 当前"坑"的状态
        :return:
        """
        if idx == len(nums):
            self.res.append(self.holes.copy())
            return
        if idx and nums[idx] != nums[idx - 1]:
            start = 0
        for i in range(start, len(nums)):
            if not state >> i & 1:
                self.holes[i] = nums[idx]
                self.dfs(nums, idx + 1, i + 1, state + (1 << i))


if __name__ == "__main__":
    print(Solution().permuteUnique([1, 1, 2, 2]))
