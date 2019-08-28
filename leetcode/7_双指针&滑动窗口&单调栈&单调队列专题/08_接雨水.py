# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/28 20:21
 @desc: 第42题
"""

"""
    解题思路：
        本题也是涉及到单调栈的使用，我们要求凹下去区间的面积总和，枚举每一个柱形高度时，要找到它左边第一个比它高的柱子
                
        要知道，我们想形成一个凹区间，那么必须满足，递减栈中，存在比它矮的柱子，否则当前柱子无法形成凹区间，即不会对
        面积area作出贡献。
        
        假设现在是第i个柱子，如果它的高度小于前面的柱子高度，则不会形成凹区间，把它的下标添加到栈中，可以使其保持
        递减的特性
        
        假设第i个柱子，它的高度大于前面柱子的高度，那么递减栈中如果元素个数大于等于2的话，就可以形成一个凹区间，
        这个面积分两种情况计算：
        （1）递减栈中栈顶元素对应的柱子比当前柱子矮的情况：
            这部分面积等于（栈顶元素对应的柱子高度 - 上一个栈顶元素的柱子高度） * （当前元素与栈顶元素之间的柱子个数）
                
        （2）递减栈中栈顶元素对应的柱子比当前柱子高的情况：（此处是第一个比当前柱子高的柱子下标）
            这部分面积等于（当前元素对应的柱子高度减去上一个栈顶元素的柱子高度）* （当前元素与栈顶元素之间的柱子个数）
                
        这两种情况，我们可以利用单调递减栈来实现，具体可以看下方的代码，以及08_接雨水_计算.png
        
        最后记得把当前柱子下标添加到递减栈中
"""


class Solution:
    def trap(self, nums) -> int:
        stack = []
        area = 0
        last = 666  # 这里last初始任意值都可以，因为在下面的第一轮area计算中，i-t-1值必为0，随后last会被覆盖掉
        for i in range(len(nums)):
            while stack and nums[stack[-1]] <= nums[i]:  # 第一部分的面积，见上面推理
                t = stack.pop()
                area += (nums[t] - last) * (i - t - 1)
                last = nums[t]  # 循环结束时，last是递减栈中最后一个小于nums[i]的柱子高度
            if stack:  # 第二部分的面积
                area += (nums[i] - last) * (i - stack[-1] - 1)
            stack.append(i)  # 再把当前柱子下标添加到栈中
        return area


if __name__ == '__main__':
    print(Solution().trap([5, 4, 3, 0, 1, 4.5]))
