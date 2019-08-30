# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/29 09:22
 @desc: 第918题
"""

"""
 解题思路：
 
    环形数组类型的题，有一个通用技巧，我们把原数组复制一份，加到原数组之后，组成一个长度为2n的新数组。
    
    本题限定，在子数组中，最多只能包含原数组中的每个元素一次，也就是说，我们的子数组，长度必须满足
    
                                1 <= len(sub_array) <= n
    
    我们的问题转化为，在一个长度为2n的数组中，有一个长度为n的窗口进行移动，我们要找到窗口内部，前缀和的最小值，
    然后用当前元素的前缀和 减去 该最小值，即为此时窗口内部的最大子数组之和。
"""


class Solution:
    def maxSubarraySumCircular(self, nums):
        if not nums:
            return 0
        n = len(nums)
        nums *= 2  # 原数组复制一遍
        pre_sum = [0] * (2 * n + 1)  # pre_sum[1]表示前1个元素的和
        for i in range(1, 2 * n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
        queue = []
        ans = float('-inf')  # 不能初始化为0，数组元素可能全为负
        for i in range(1, 2 * n + 1):
            if queue and i - queue[0] == n + 1:  # 注意这里是n+1，队列存的是前缀和的下标，前i个元素的和-前j个元素的和
                queue.pop(0)
            if queue:
                ans = max(ans, pre_sum[i] - pre_sum[queue[0]])
            while queue and pre_sum[queue[-1]] >= pre_sum[i]:  # 维护队列递增
                queue.pop()
            queue.append(i)
        return ans


if __name__ == '__main__':
    print(Solution().maxSubarraySumCircular([1, 2, 3]))
