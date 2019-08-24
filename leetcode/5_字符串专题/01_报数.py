# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/21 21:01
 @desc: 第38题
"""
"""
 解题思路：
        本题的难点大概在于读懂题意
        1
        11 前一行相同元素的段只有1段，长度为1，输出格式为 ：段长度+段的元素
        21 前一行相同元素的段只有1段，长度为2，写作：21
        1211 前一行相同元素的段有2段，长度分别为1，1，写作：1211
        111221 前一行相同元素的段有3段，长度分别为1，1，2，写作：111221
        312211 前一行相同元素的段有3段，长度分别为3，2，1，写作：312211
        
        回顾之前做过的题，把字符串或者列表，切成连续的段，模版代码：
        j = 0
        n = len(s)
        while j < n:
            k = j
            while k < n and s[k] == s[j]:
                k += 1
            #do sth#
            j = k
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for i in range(1, n):
            ns = ''  # 统计本轮的输出
            j = 0
            while j < len(s):
                k = j
                while k < len(s) and s[k] == s[j]:
                    k += 1
                ns = ns + str(k - j) + s[j]
                j = k  # 把j的值更新为k
            s = ns
        return s


if __name__ == '__main__':
    print(Solution().countAndSay(5))
