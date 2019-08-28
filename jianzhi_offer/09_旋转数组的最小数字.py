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

    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return -1
        n = len(rotateArray) - 1
        # 去重
        while rotateArray[n] == rotateArray[0]:
            n -= 1
        # 如果剩下数组为递增序列，直接返回首元素
        if rotateArray[n] >= rotateArray[0]:
            return rotateArray[0]
        # 否则使用二分查找法
        l = 0
        r = n
        while l < r:
            mid = (l + r) // 2
            if rotateArray[mid] < rotateArray[0]:
                r = mid
            else:
                l = mid + 1
        return rotateArray[l]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minNumberInRotateArray([4, 5, 6, 7, 8, 0, 1, 2]))
