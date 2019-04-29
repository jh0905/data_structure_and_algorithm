# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/29/19 3:44 PM
 @desc: 直接选择排序
"""
"""
 1.基本思想：
    在要排序的一组数中，选出最小（或者最大）的一个数与第1个位置的数交换；然后在剩下的数当中再找最小（或者最大）的与第2个位置的数交换，
    依次类推，直到第n-1个元素（倒数第二个数）和第n个元素（最后一个数）比较为止
    
 2.算法流程：
    (1)初始时，数组为无序区 a[0,1,2,...,n-1]，令i=0
    
    (2)在无序区a[i,...,n-1]中，找到一个最小的元素，与a[i]交换，交换之后，a[0,1,...,i]为有序区
    
    (3)i=i+1，重复(2)过程，直至i=n-1

 3.时间复杂度分析：
    每一轮都要找出无序数组中的最小值然后插到有序数组中，所以此算法的时间复杂度为O(n^2)，最坏情况是原数组为递减序列

 4.稳定性分析：
    直接选择排序是不稳定的，举个例子：(7) 2 5 9 3 4 [7] 1
                                (7)和1进行交换之后，(7)就到[7]的后面了。
"""


def straight_select_sort(nums):
    length = len(nums)
    idx = -1  # 初始化最小值对应的index，用于之后交换
    for i in range(length):
        min_value = nums[i]
        for j in range(i, length):
            if nums[j] < min_value:
                min_value = nums[j]
                idx = j
        nums[i], nums[idx] = nums[idx], nums[i]
    return nums


if __name__ == '__main__':
    numbers = [int(x) for x in input().split()]
    print(straight_select_sort(numbers))
