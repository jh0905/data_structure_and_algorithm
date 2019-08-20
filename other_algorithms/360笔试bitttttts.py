# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/15 14:43
 @desc:
"""


class Solution:
    # 十进制转k进制，存为数组
    def d2k(self, k, num):
        res = []
        while num:
            res.append(num % k)
            num //= k
        return res[::-1]

    # k进制数组转为十进制数
    def k2d(self, k, nums):
        num = 0
        n = len(nums)
        for i in range(n):
            num += nums[i] * k ** (n - i - 1)
        return num

    def get_num(self, k, l, r):
        if l == r:  # 排除l,r相等的情况
            return l
        if l > r:
            return -1
        # 将l和r都用k进制数组来表示
        kl = self.d2k(k, l)
        kr = self.d2k(k, r)
        kl = [0] * (len(kr) - len(kl)) + kl
        n = len(kr)
        i = 0
        while kr[i] == kl[i]:
            i += 1
        if kr.count(k - 1) == n - i:
            return self.k2d(k, kr)
        return self.k2d(k, kl[:i + 1] + [k - 1] * (n - i - 1))


if __name__ == '__main__':
    n = input()
    import sys

    lines = sys.stdin.readlines()
    sol = Solution()
    for line in lines:
        line = [int(x) for x in line.strip().split()]
        print(sol.get_num(line[0], line[1], line[2]))
