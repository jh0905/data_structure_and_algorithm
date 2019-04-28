# encoding: utf-8
"""
 @project:剑指offer_by_Python
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/1/19 8:24 PM
 @desc: 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的,也不知道每个数字重复几次,
        请找出数组中任意一个重复的数字！
"""


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    # 解法一：哈希表的做法 时间复杂度0(n)，空间复杂度0(n)
    def duplicate_1(self, numbers, duplication):
        if numbers is None:
            return False
        for i in range(len(numbers)):
            if numbers[i] < 0 or numbers[i] > len(numbers) - 1:
                return False
        num_dict = {}
        for number in numbers:
            if number in num_dict.keys():
                duplication[0] = number
                return True
            else:
                num_dict[number] = 1
        return False

    # 解法二： 时间复杂度0(n)，空间复杂度0(1)
    #   一维列表长度为n,且所有元素在0到n-1之间，如果这个数组中没有重复的数字，那么数组排序之后，数字i必定会出现在下标为i的位置，所以遍历
    #   数组i,如果当前元素与index不相等，就交换两个元素，直至当前元素与index相等为止.
    #
    #   伪代码：
    #
    #   依次遍历数组中每个元素：
    #       while当前元素与index不相等：
    #           如果当前元素与当前元素[当前元素[i]]相等认为出现了重复：
    #                 返回True
    #           否则:
    #               swap当前元素与当前元素[当前元素[i]]
    #  返回False
    def duplicate_2(self, numbers, duplication):
        if numbers is None:
            return False
        # 题目要求输入的数组在[0,n-1]区间内
        for i in range(len(numbers)):
            if numbers[i] < 0 or numbers[i] > len(numbers) - 1:
                return False
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                # swap numbers[i] 和numbers[numbers[i]]
                temp = numbers[i]
                numbers[i] = numbers[numbers[i]]
                numbers[temp] = temp
        return False


if __name__ == '__main__':
    sol = Solution()
    test_numbers = [4, 3, 0, 2, 4, 2, 5, 6]
    dumplication = [0] * len(test_numbers)
    print(sol.duplicate_1(test_numbers, dumplication))
    print(sol.duplicate_2(test_numbers, dumplication))
