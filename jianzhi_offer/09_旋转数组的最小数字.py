# encoding: utf-8
"""
 @project:Data_Structure&&Algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/2/19 9:34 PM
 @desc: 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
        输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
        例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
        NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""


class Solution:
    # 算法思路：
    #       首先要做的，当然是找到数组中最小的元素，那么第一反应可能是用一遍顺序遍历，找到最小的元素，此时时间复杂度为O(n)
    #       但是，我们原数组是一个递增排序，那么它任意一个点作为旋转之后，得到的数组，如果分成两部分，一定满足左部分的点>=右部分的点
    #       并且这两部分的元素仍是递增排序的，而最小的元素，则刚好是两部分的分界线
    #       因此尝试用二分查找来寻找最小的元素
    # 伪代码：
    #       排除异常情况
    #       初始化三个指针，left指向数组头，right指向数组尾，mid初始化为0
    #       当left指向的元素>=right指向的元素时：(根据旋转数组所得)
    #           如果 right-left=1：
    #               说明两个指针相邻了，right即为数组中的最小值，循环结束
    #           计算left与right的中间元素mid(向下取整)
    #           如果mid指向的元素>=left指向的元素：
    #               说明left到mid之间处于递增关系，最小值在mid和right之间，于是把mid赋给left
    #           否则:
    #               由mid指向的元素<left指向的元素得知，最小值在left和mid之间,于是把mid赋给right

    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0 or rotateArray is None:
            return 0
        left = 0
        right = len(rotateArray) - 1
        mid = left
        while rotateArray[left] >= rotateArray[right]:
            if right - left == 1:
                mid = right
                break
            mid = (left + right) // 2  # 向下取余
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            else:
                right = mid
        return rotateArray[mid]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minNumberInRotateArray([4, 5, 6, 7, 8, 1, 2, 3]))
