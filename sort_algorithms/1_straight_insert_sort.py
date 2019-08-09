# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/22/19 9:06 PM
 @desc: 直接插入排序
"""

"""
 1.基本思想：
    将待排序的无序数组，看成是一个仅含有1个元素的有序数列和一个无序数列，每一次都是将无序数列中的一个元素，从后往前扫描，插入到有序数列中去，
 从而获得最终的有序数列。
 
 2.时间复杂度
    由于我们每次插入的过程中，都有比较n次，而一共有n个元素需要插入，所以此算法的时间复杂度为O(n^2)，最坏情况是原数组为递减序列
    
 3.插入排序是稳定算法
    即如果两个相等的元素，在初始数组中的先后顺序和排完序之后的先后顺序是一致的!
"""


def straight_insert_sort(nums):
    length = len(nums)
    for i in range(1, length):  # 第一个元素（下标为0）为有序数列，对之后的下标为1到n-1的元素，进行插入排序
        # 这里的 range(i,0,-1)就像是c++或Java中的倒序遍历，for(i=n;i>0;--i){}，如果要取到0的话，range(i,-1,-1)
        for j in range(i, 0, -1):  # 如i=3时，此时j分别取3,2,1，取不到0
            # j每次都和它的前1位进行比较
            if nums[j] < nums[j - 1]:  # 如果第j个元素小于有序数列的第j-1个元素，就往前移动一位，下一轮继续判断，从后往前扫描的过程！
                nums[j], nums[j - 1] = nums[j - 1], nums[j]  # 这里巧妙的利用了Python的语言特性，就是一个交换的过程，但是没有temp
            else:  # 如果当前元素大于或等于上一个元素，就不交换了，开始插入下一个元素
                break


if __name__ == '__main__':
    sort_nums = [6, 1, 3, 5, 2, 7, 3, 1, 9]
    print("origin_nums is ", sort_nums)
    straight_insert_sort(sort_nums)  # 直接在原数组上进行修改
    print("sorted_nums is ", sort_nums)
