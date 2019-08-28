# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 6/25/19 9:30 PM
 @desc:在一个长度为n+1的数组里，所有数字都在1~n的范围内，所以数组中至少有一个数字是重复的。
       请找出数组中任意一个重复的数字，但不能修改输入的数组。如输入长度为8的数组{2,3,5,4,3,2,6,7}，那么输出为2或3
"""

"""
 解题思路：n个坑，n+1个数，找重复元素，二分法求解
 
    根据题意，数组中一定有重复数字，我们取1~n的中间值m，则m = n//2 ，划分为 [1,m] 和 [m+1,n] 两个区间。
    如果数组中，统计处于1~m区间数字的个数大于m，意味着在这个区间内有重复数字，否则重复数字一定在[m+1,n]区间
    
"""


class Solution:
    def find_duplicate(self, numbers):
        l = 1
        r = len(numbers) - 1
        while l < r:
            mid = (l + r) // 2
            if self.check(numbers, l, mid):
                r = mid
            else:
                l = mid + 1
        return l

    def check(self, numbers, l, mid):
        count = 0
        for i in range(len(numbers)):
            if l <= numbers[i] <= mid:
                count += 1
        if count > mid - l + 1:
            return 1
        else:
            return 0


if __name__ == '__main__':
    test_numbers = [2, 3, 5, 4, 3, 2, 6, 7]
    sol = Solution()
    print(sol.find_duplicate(test_numbers))
