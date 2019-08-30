# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/29 14:28
 @desc: 第1题
"""
"""
    考察哈希表的使用
    
    创建一个哈希表，遍历数组中的每一个值，如果该值不在哈希表的key中，就把target-nums[i]作为key,i作为value，存到
    哈希表中。
"""


class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                d[target - nums[i]] = i
        return []
