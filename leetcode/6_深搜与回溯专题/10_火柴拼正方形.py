# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/24 19:51
 @desc: 第473题
        使用所有火柴拼成一个正方形，每个火柴只能用一次，且必须被使用一次

        本版本的代码，近适用于小数据量的数据集，在数据量比较大的时候，会报TLE的错误，我们在下一讲中学习剪枝优化本版本的代码。
"""

"""
    
    *我们来把题意转换成数学语言，所有火柴拼成正方形，也就意味着，把数组分成四部分，每一部分的长度为 sum/4，sum表示数组的总和。*
    
    那么我们可以在搜索之前，进行第一轮判断，如果sum为0或者不能被4整除，说明必定不可能拼成正方形。
    
    否则我们需要枚举数组中的每一个数字，定义 dfs(u,cur_len,length)，u表示当前拼好的正方形的边数，cur_len表示当前正在拼的边的
    长度，length表示每条边的长度。
    
    我们还需要定义一个全局变量，记录某个数组是否已被使用，然后dfs每个可能的数字。
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
        self.nums = sorted(_nums)
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
        for i in range(len(self.nums)):
            if not self.is_used[i] and cur_len + self.nums[i] <= self.length:
                self.is_used[i] = 1
                if self.dfs(u, cur_len + self.nums[i]):
                    return True
                else:
                    self.is_used[i] = 0
        return False


if __name__ == '__main__':
    print(Solution().makesquare([1, 3, 5, 8, 7, 8]))
