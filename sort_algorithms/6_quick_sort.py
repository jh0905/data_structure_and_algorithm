# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/29/19 5:23 PM
 @desc: 快速排序（Quicksort）是对冒泡排序的一种改进，借用了分治的思想，由C. A. R. Hoare在1962年提出。
"""

"""
 1.基本思想：快速排序算法的基本思想为分治思想
    ①从数列中挑出一个元素，称为 “基准”（pivot）；
    ②重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）；
    ③对所有两个小数列重复第二步，直至各区间只有一个数
    
 2.时间复杂度分析
    O(n*log(n))，但若初始数列基本有序时，快排序反而退化为冒泡排序O(n^2)
    
 3.稳定性分析
    快速排序是一种不稳定的排序
"""


def quick_sort(nums):
    length = len(nums)
    if length <= 1:
        return nums
    else:
        pivot = nums[0]
        greater = [element for element in nums[1:] if element > pivot]
        lesser = [element for element in nums[1:] if element <= pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


# 经典的快排算法
def quick_sort_2(sorting, left, right):
    if right <= left:
        return
    a = i = left
    b = right
    pivot = sorting[left]
    while i <= b:
        if sorting[i] < pivot:
            sorting[a], sorting[i] = sorting[i], sorting[a]
            a += 1
            i += 1
        elif sorting[i] > pivot:
            sorting[b], sorting[i] = sorting[i], sorting[b]
            b -= 1
        else:
            i += 1
    quick_sort_2(sorting, left, a - 1)
    quick_sort_2(sorting, b + 1, right)


if __name__ == '__main__':
    numbers = [int(x) for x in input().split()]
    print(quick_sort(numbers))
    quick_sort_2(numbers, 0, len(numbers) - 1)
    print(numbers)
