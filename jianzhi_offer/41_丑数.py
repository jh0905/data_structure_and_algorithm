# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/7 09:23
 @desc:
"""


class Solution(object):
    # 用空间换时间
    def getUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        nums = [1]
        i, j, k = 0, 0, 0
        n -= 1
        while n:
            t = min(nums[i] * 2, nums[j] * 3, nums[k] * 5)
            if t == nums[i] * 2:
                i += 1
            if t == nums[j] * 3:
                j += 1
            if t == nums[k] * 5:
                k += 1
            nums.append(t)
            n -= 1
        return nums[-1]

    # 用时间换空间
    def getUglyNumber_2(self, n):
        if n <= 1:
            return n
        ugly_count = 0
        number = 0
        while True:
            number += 1
            if self.is_ugly(number):
                ugly_count += 1
            if ugly_count == n:
                break
        return number

    def is_ugly(self, number):
        while number % 2 == 0:
            number //= 2
        while number % 3 == 0:
            number //= 3
        while number % 5 == 0:
            number //= 5
        return True if number == 1 else False


if __name__ == '__main__':
    print(Solution().getUglyNumber(12))
    # print(Solution().getUglyNumber_2(12))
