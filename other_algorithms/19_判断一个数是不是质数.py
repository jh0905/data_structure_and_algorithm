# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/7 11:16
 @desc:
"""


class Solution(object):
    def is_prime(self, number):
        # ceil向上取整，floor向下取整，int是向下取整,round是四舍五入
        from math import ceil, sqrt
        for i in range(2, ceil(sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

    def is_prime_2(self, number):
        if number <= 3:  # 考虑number=2,3的情况
            return number > 1

        if number == 4:
            return False

        # 不在6的倍数两侧的数，一定不是质数, 可以直接返回
        if number % 6 != 1 and number % 6 != 5:
            return False
        # 过滤下来的是 只在6的倍数的一侧的数，如 5,7,11,13,17,19,23,25,29,31,35,37 等数
        from math import sqrt
        i = 5
        while i <= sqrt(number):
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True


if __name__ == '__main__':
    print(Solution().is_prime(4))
    print(Solution().is_prime_2(4))
