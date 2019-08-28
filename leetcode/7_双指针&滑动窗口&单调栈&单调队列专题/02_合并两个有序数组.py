# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/28 10:20
 @desc: 第88题
        输入:
            nums1 = [1,2,3,0,0,0], m = 3
            nums2 = [2,5,6]       n = 3

        输出: [1,2,2,3,5,6]

"""

"""
    解题思路：
        合并两个有序数组，我们常规思路是定义两个指针，分别指向两个数组的头部，然后取较小值添加到新的数组中。
        但是我们现在题目要求是直接改变nums1,而不能创建新的数组
        
    于是我们换个角度：
        定义两个指针，分别指向两个数组的有效长度的尾部，较大的那个值一定是全局最大值，所以我们每次选出一个当前最大的值
        添加到nums1尾部即可，然后每次添加的值向前移动一位，所以这里还要再用一个指针。
"""


class Solution:
    def merge(self, nums1, m: int, nums2, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cur = -1
        while m and n:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[cur] = nums2[n - 1]
                n -= 1
            else:
                nums1[cur] = nums1[m - 1]
                m -= 1
            cur -= 1
        if n:  # 如果m不为0，nums1数组不需改变，如果n不为0，把n的元素复制到nums1中
            nums1[:n] = nums2[:n]


if __name__ == '__main__':
    nums1 = [1, 4, 6, 0, 0, 0]
    nums2 = [2, 3, 5]
    Solution().merge(nums1, 3, nums2, 3)
    print(nums1)
