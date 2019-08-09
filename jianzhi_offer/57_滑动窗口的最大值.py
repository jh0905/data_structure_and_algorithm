# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/8 17:03
 @desc:
"""


class Solution(object):
    # 直观解法，时间复杂度为O(kn)，每轮要从k个数中找到最大值
    def maxInWindows(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        queue = []
        for num in nums:
            if len(queue) < k:
                queue.append(num)
            if len(queue) == k:
                res.append(max(queue))
                queue.pop(0)
        return res

    def maxInWindows(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        queue = []
        for i, num in enumerate(nums):
            if queue and i - queue[0] == k:  # 判断队列头元素是否需要弹出
                queue.pop(0)
            while queue and nums[queue[-1]] <= num:  # 维护队列单调递减
                queue.pop()  # 队列尾部小于num的元素陆续出队
            queue.append(i)
            if i >= k - 1:  # 队列的头元素始终为当前窗口内最大值的下标
                res.append(nums[queue[0]])
        return res
