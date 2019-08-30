# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/30 09:58
 @desc: 第560题
"""

"""
    解题思路：前缀和 + 哈希映射
    
    前缀和：
        s[0] = 0
        s[1] = a[0]
        s[2] = a[0] + a[1]
        ...
        s[n] = a[0] + a[1] + ... + a[n-1]
        
    i从 0 到 n-1 开始遍历：
        t = s[i] - k
        那么我们要统计，j从0到i-1中，s[j] = t 的个数，它的值则可以加到最终返回的ans里面
        
    我们用哈希表来存t的个数，即 d[s[i]-t]，并把每一个前缀和都存到哈希表中
"""


class Solution:
    def subarraySum(self, nums, k):
        ans, pre_sum = 0, 0
        d = {0: 1}  # 用来处理单个元素等于k的情况
        for i in range(len(nums)):
            pre_sum += nums[i]
            if pre_sum - k in d:
                ans += d[pre_sum - k]
            d[pre_sum] = d.get(pre_sum, 0) + 1  # 这一步必须计算d[pre_sum-k]之后，否则会引起重复
        return ans
