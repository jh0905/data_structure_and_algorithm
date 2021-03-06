# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/29/19 4:58 PM
 @desc: 冒泡排序
"""
"""
 1.基本思想：
    在要排序的一组数中，对当前还未排好序的范围内的全部数，自上而下对相邻的两个数依次进行比较和调整，让较大的数往下沉，较小的往上浮。
 即：每当两相邻的数比较后发现它们的排序与排序要求相反时，就将它们互换。每一趟排序后的效果都是将没有沉下去的元素给沉下去

 2.算法流程：
    (1)比较相邻的两个元素，如果前面的数据大于后面的数据，就将两个数据进行交换；这样对数组第0个元素到第n-1个元素进行一次遍历后，
       最大的一个元素就沉到数组的第n-1个位置；
       
    (2)下一次就是重复上述过程，但是元素区间是第0个到第n-2个之间的元素    【无序数组在左边，右边是有序数组，无序数组个数逐渐减小】
    
    (3)以此类推，直至只剩首部1个元素；

 3.时间复杂度分析：
    时间复杂度为O(n^2)
 
 4.稳定性分析：
    冒泡排序是一种稳定的排序
"""


def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1, -1, -1):  # 冒泡n-1轮
        flag = True
        for j in range(i):  # 每轮枚举从第0个元素，到第i-1个元素
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = False
        if flag:  # 如果flag为True，如果本轮的冒泡未发生元素交换，则数组已经有序
            break
    return nums


if __name__ == '__main__':
    numbers = [int(x) for x in input().split()]
    print(bubble_sort(numbers))
