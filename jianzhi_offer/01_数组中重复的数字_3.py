# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 7/1/19 7:24 PM
 @desc: 给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
        找到所有出现两次的元素。
"""


class Solution:
    def findDuplicates(self, nums):
        """
        正负存储元素法，遍历nums,将nums[i]的绝对值作为下标，如果对应元素为正，则转为负数，否则添加到result里面
        :param nums:
        :return:
        """
        if nums is None or len(nums)==0:
            return []
        result=[]
        nums[nums[0]] *= -1
        for i in range(1,len(nums)):
            num = abs(nums[i])
            if nums[num-1] > 0:
                nums[num-1] = nums[num-1]*(-1)
            else:
                result.append(num)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
