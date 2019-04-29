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


def merge_sort(nums):
    length = len(nums)
    if length > 1:
        midpoint = length // 2
        left_half = merge_sort(nums[:midpoint])
        right_half = merge_sort(nums[midpoint:])
        i = 0
        j = 0
        k = 0
        left_length = len(left_half)
        right_length = len(right_half)
        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                nums[k] = left_half[i]
                i += 1
            else:
                nums[k] = right_half[j]
                j += 1
            k += 1

        while i < left_length:
            nums[k] = left_half[i]
            i += 1
            k += 1

        while j < right_length:
            nums[k] = right_half[j]
            j += 1
            k += 1

    return nums


'''
Python implementation of merge sort algorithm.
Takes an average of 0.6 microseconds to sort a list of length 1000 items.
Best Case Scenario : O(n)
Worst Case Scenario : O(n)
'''


def merge_sort_fastest(nums):
    start = []
    end = []
    while len(nums) > 1:
        a = min(nums)
        b = max(nums)
        start.append(a)
        end.append(b)
        nums.remove(a)
        nums.remove(b)
    if nums:
        start.append(nums[0])
    end.reverse()
    return start + end


if __name__ == "__main__":
    numbers = [int(x) for x in input().split()]
    print(merge_sort(numbers))
    print(merge_sort_fastest(numbers))
