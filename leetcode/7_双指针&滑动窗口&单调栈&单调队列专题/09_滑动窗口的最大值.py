# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/29 08:58
 @desc: 第239题
        给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

        返回滑动窗口中的最大值。

        输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
        输出: [3,3,5,5,6,7]

"""

"""
    解题思路： 涉及到滑动窗口的最值问题，绝大多数考虑用 单调队列来实现
    
    单调队列存储元素的下标，这里要求窗口中的最大值，如果在窗口里，后一个值比前一个值大，那么前一个值永远都不会成为
    最大值输出，所以我们要维护一个单调递减的队列。
    
    一个新元素加入时，首先判断队列中，是否有元素需要被移除。
    
    然后在考虑把新元素加入队列中时，它的队列尾部元素的关系，把尾部所有小于它的元素弹出，因为只有新元素在窗口内，
    窗口里其他比它小的元素永远不会成为窗口内最大的元素。
    
    当新元素的下标 - 队列首部元素的下标 >= k-1时，说明当前需要弹出队首元素，并添加到res数组中
        
"""


class Solution:
    def maxSlidingWindow(self, nums, k):
        res, queue = [], []
        for i in range(len(nums)):
            if queue and i - queue[0] == k:  # 窗口滑动，删除单调队列中，不在窗口中的元素
                queue.pop(0)
            while queue and nums[queue[-1]] <= nums[i]:  # 维持单调递减性
                queue.pop()
            queue.append(i)
            if i >= k - 1:  # 添加当前窗口内的最大值到res数组中
                res.append(nums[queue[0]])
        return res


if __name__ == '__main__':
    print(Solution().maxSlidingWindow([5, 4, 2, 3, 7, 6], 3))
