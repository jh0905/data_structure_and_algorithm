# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/29/19 6:19 PM
 @desc: 归并排序（Merge sort）是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用
"""
"""
 1.基本思想
    归并排序法是将两个(或两个以上)的有序表合并成一个新的有序表，即把待排序序列分为若干个子序列，每个子序列是有序的，然后再把有序子序列合并为
 整体有序的序列。
 
 2.时间复杂度分析
    O(n*log(n))
    
 3.稳定性分析
    归并排序是一种稳定排序算法
"""


def merge_sort(nums, l, r):
    if l >= r:
        return [nums[l]]
    mid = l + r >> 1
    left = merge_sort(nums, l, mid)
    right = merge_sort(nums, mid + 1, r)
    sorted_nums = []
    while left and right:
        if left[0] <= right[0]:
            sorted_nums.append(left.pop(0))
        else:
            sorted_nums.append(right.pop(0))
    if left:
        sorted_nums.extend(left)
    if right:
        sorted_nums.extend(right)
    return sorted_nums


if __name__ == "__main__":
    numbers = [int(x) for x in input().split()]
    print(merge_sort(numbers, 0, len(numbers) - 1))
