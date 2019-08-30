# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/29 14:40
 @desc: 第187题
"""

"""
    考察哈希表的使用
    
    遍历一轮字符串，所有长度为10的子串，计算出现的次数。
"""


class Solution:
    def findRepeatedDnaSequences(self, s):
        d = {}
        res = []
        for i in range(len(s) - 9):  # 因为每个子串长度大于10
            substr = s[i:i + 10]
            d[substr] = d.get(substr, 0) + 1
            if d[substr] == 2:
                res.append(substr)
        return res


if __name__ == '__main__':
    print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
