# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/15 16:36
 @desc:
"""


class Solution:
    def get_n(self, nums):
        if len(nums) < 2:
            return -1
        for i in range(3, len(nums) + 1):
            max_v = max(nums[:i])
            if sum(nums[:i]) > 2 * max_v:
                return i
        return -1


if __name__ == '__main__':
    n = input()
    print(Solution().get_n([int(x) for x in input().strip().split()]))
