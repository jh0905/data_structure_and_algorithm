# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/7 10:27
 @desc:
"""


class Solution(object):

    def get_prime_factors(self, number, res):
        if number == 1:
            return res.append(number)
        n = 2
        while number != 1:
            if number % n == 0:
                res.append(n)
                number //= n
            else:
                n += 1
        return res


if __name__ == "__main__":
    num = 144
    ans = []
    sol = Solution()
    print(sol.get_prime_factors(num, ans))
