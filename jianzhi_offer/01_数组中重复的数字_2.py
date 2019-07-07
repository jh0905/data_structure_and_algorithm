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
 分析：
    根据题意，数组中一定有重复数字，我们取1~n的中间值m，则m = n//2 ，划分为 [1,m] 和 [m+1,n] 两个区间。
    如果数组中，统计处于1~m区间数字的个数大于m，意味着在这个区间内有重复数字，否则重复数字一定在[m+1,n]区间
    
    这个思想是借用了二分查找的思想，不过这个不能保证找到所有的重复数字，如在[1,]区间，{2,2}的个数为2，但是不会把2认作是重复数字，
    最终得到的一个区间，是一个形同[n,n+1]的区间，里面的元素个数必须大于2，然后继续查找[n,n]的元素数，只要里面的元素数大于1即认为n为重复元素
"""


class Solution:
    def find_duplicate(self, numbers):
        length = len(numbers)
        # 二分查找区间是 1~length-1，注意查找区间不是下标区间!
        start = 1
        end = length - 1
        while start <= end:
            mid = (end - start) // 2 + start
            count = self.count_range(numbers, length, start, mid)
            print('count:', count)
            if start == end:
                if count > 1:
                    return start
                else:
                    break
            # 如果在start~mid区间的数字个数，大于mid-start+1，说明重复值在这个区间
            if count > mid - start + 1:
                end = mid
            else:
                start = mid + 1
        return -1

    def count_range(self, numbers, length, start, end):
        if numbers is None:
            return 0
        count = 0
        for i in range(length):
            if start <= numbers[i] <= end:
                count += 1
        return count


if __name__ == '__main__':
    test_numbers = [2, 3, 5, 4, 3, 2, 6, 7]
    sol = Solution()
    print(sol.find_duplicate(test_numbers))
