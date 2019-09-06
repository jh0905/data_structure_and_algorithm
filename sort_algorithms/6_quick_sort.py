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


def partition(nums, l, r):
    pivot = nums[l]
    while l < r:
        while l < r and nums[r] >= pivot:
            r -= 1
        nums[l], nums[r] = nums[r], nums[l]
        while l < r and nums[l] <= pivot:
            l += 1
        nums[l], nums[r] = nums[r], nums[l]
    return l


def quick_sort(nums, l, r):
    if l >= r:  # 如果数组为[4, 3]，partition返回的值则为1，右边变成l=2,r=1，所以此种情况要return，这里取大于等于号
        return
    idx = partition(nums, l, r)
    quick_sort(nums, l, idx - 1)
    quick_sort(nums, idx + 1, r)


if __name__ == '__main__':
    numbers = [int(x) for x in input().split()]
    quick_sort(numbers, 0, len(numbers) - 1)
    print(numbers)
