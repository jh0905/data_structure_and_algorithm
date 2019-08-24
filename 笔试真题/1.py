# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/23 19:47
 @desc: 贝壳笔试 吃糖果
"""
if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    nums = sorted(nums)  # 对输入数组进行排序
    print(nums)
    #  相同元素合并，合并后的元素值加1，最终集合的元素个数即为最少次数
    i = 1
    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums[i] += 1
            nums.remove(nums[i - 1])
            nums = sorted(nums)
        else:
            i += 1
    print(nums)
    print(len(nums))
