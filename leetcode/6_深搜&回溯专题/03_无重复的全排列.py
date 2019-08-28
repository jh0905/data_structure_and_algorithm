# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/23 15:32
 @desc: 第46题
"""

"""
    解题思路：
        深搜可以完成此题。
        
        从第一个数字开始，枚举它所有可能的位置，如果当前位置未被占用，我们把它放进去，并继续枚举下一个数字，并把当前占用位置的状态
        标记为已占有。
        
        这里我们用二进制来标记位置是否已占用。
           
"""


class Solution:
    holes = []
    res = []

    def permute(self, nums):
        if not nums:
            return []
        self.res = []
        self.holes = [0] * len(nums)
        self.dfs(nums, 0, 0)
        return self.res

    def dfs(self, nums, idx, state):
        """
        :param nums:输入数组
        :param idx: 当前枚举元素
        :param state: 当前坑的填充情况，二进制表示
        :return:
        """
        if idx == len(nums):
            self.res.append(self.holes.copy())
            return
        for i in range(len(nums)):
            if not state >> i & 1:
                self.holes[i] = nums[idx]
                self.dfs(nums, idx + 1, state + (1 << i))


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
