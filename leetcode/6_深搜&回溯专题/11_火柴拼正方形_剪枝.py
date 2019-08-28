# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/24 20:36
 @desc: 第473题   剪枝优化策略，避免TLE
"""

"""
    剪枝策略：
        1.从大到下枚举数组中的数字(把nums数组从大到下排列)，优先枚举分支少的数字，越大的数字，拼成正方形边长用到的火柴越少
        2.如果当前火柴拼接失败，并且是当前边的第一个，则直接剪掉该分支，return False
        3.如果当前火柴拼接失败，则跳过接下来所有长度相同的木棒
"""


class Solution:
    is_used = []
    nums = []
    length = 0  # 正方形的边长

    def makesquare(self, _nums):
        cnt = sum(_nums)
        if not cnt or cnt % 4:
            return False
        self.is_used = [0] * len(_nums)
        self.nums = sorted(_nums, reverse=True)  # 剪枝策略1
        self.length = cnt / 4
        return self.dfs(0, 0)

    def dfs(self, u, cur_len):
        """
        :param u: 当前拼好的正方形的边数
        :param cur_len: 当前拼好的长度
        :return: bool
        """
        if cur_len == self.length:  # 如果当前拼好的长度等于边长
            u += 1
            cur_len = 0
        if u == 4:  # 0->1, 1->2, 2->3, 3->4说明拼好了四条边
            return True
        i = 0
        while i < len(self.nums):
            if not self.is_used[i] and cur_len + self.nums[i] <= self.length:
                self.is_used[i] = 1
                if self.dfs(u, cur_len + self.nums[i]):
                    return True
                else:
                    self.is_used[i] = 0
                    if not cur_len:  # 剪枝策略2
                        return False
                    while i + 1 < len(self.nums) and self.nums[i + 1] == self.nums[i]:  # 剪枝策略3
                        i += 1
            i += 1
        return False


if __name__ == '__main__':
    print(Solution().makesquare([1, 3, 5, 8, 7, 8]))
