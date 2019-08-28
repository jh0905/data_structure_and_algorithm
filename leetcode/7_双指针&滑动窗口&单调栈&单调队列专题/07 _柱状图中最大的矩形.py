# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/28 19:09
 @desc: 第84题    单调栈的典型应用
"""

"""
    我们先不妨来看看暴力法的实现方式：
    
    我们分别枚举每一个柱形，以它的高度作为最大矩形的高，然后向左，向右搜索，找到左边第一个比它矮的柱形，然后停止移动，
    右边同理，找到右边第一个比它矮的柱形，然后停止移动，那么对应的最大矩形的宽则为： r - l - 1
    
    代码实现起来也比较简单，通过来97/99个样例，剩余两个样例超时，因此我们需要尝试优化解法。
"""


class Solution:
    def largestRectangleArea(self, nums):
        # 暴力枚举每个柱形的上边界作为上界的最大面积
        ans = 0
        for i in range(len(nums)):
            l = i
            while l >= 0 and nums[l] >= nums[i]:
                l -= 1
            r = i
            while r < len(nums) and nums[r] >= nums[i]:
                r += 1
            ans = max(ans, nums[i] * (r - l - 1))
        return ans


"""
    *** 单调栈的使用来进行优化 ***
    
    单调栈就是用来找：
        
        - 数组中，每个元素左边第一个比它小的元素(下标)   栈单调递增，如果栈顶元素大于当前元素，栈顶元素弹出，最终的栈顶
          元素，就是数组中第一个比当前元素小的元素，最后再把当前元素加入栈中。
        
        
        - 数组中，每个元素右边第一个比它小的元素(下标)   从右往左遍历，栈单调递增，如果栈顶元素大于当前元素，栈顶元素弹出，
          最终的栈顶元素，就是数组右边第一个比当前元素小的元素，最后再把当前元素加入栈中。
"""


class Solution2:
    def largestRectangleArea(self, nums):
        n = len(nums)
        left, right = [0] * n, [0] * n  # left[i]表示第i个元素，左边第一个比它小的元素下标
        stack = []
        for i in range(n):  # 生成left数组
            while stack and nums[stack[-1]] >= nums[i]:  # 弹栈操作，保证加入当前元素之后，栈还能单调递增
                stack.pop()
            if not stack:
                left[i] = -1  # 当前元素左边的所有元素都比它大
            else:
                left[i] = stack[-1]
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):  # 生成right数组
            while stack and nums[stack[-1]] >= nums[i]:  # 弹栈操作，保证加入当前元素之后，栈还能单调递增
                stack.pop()
            if not stack:
                right[i] = n  # 当前元素右边的所有元素都比它大
            else:
                right[i] = stack[-1]
            stack.append(i)
        res = 0
        for i in range(n):
            res = max(res, nums[i] * (right[i] - left[i] - 1))
        return res


if __name__ == '__main__':
    print(Solution2().largestRectangleArea([2, 1, 5, 6, 2, 3]))
