# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/28 10:37
 @desc: 第26题
"""


# 经典做法：找到有序数组中的连续项
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        for i in range(len(nums)):
            j = i
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            nums[i:j] = nums[i:i + 1]  # 删除重复项
        return nums


"""
    解法二：双指针算法
        输入： 0  0  1  1  1  2  3  3  4  4  4
        
        首先，第0个元素肯定要留在数组中，我们令i=1, i之前的所有元素必须为不重复元素，j从1到len(nums)-1开始枚举
        因为数组是有序的，我们每次只需要比较nums[j]和nums[i-1]是否相等即可，如果不相等，那么绝对不可能和i-1之前
        的元素相等，如果不相等，在把第i个元素的值赋为nums[j], i再右移一位。
"""


class Solution2:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1
        return nums[:i]


if __name__ == '__main__':
    print(Solution2().removeDuplicates([0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3]))
