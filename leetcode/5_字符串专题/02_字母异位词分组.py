# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/21 21:42
 @desc: 第49题
        给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
        输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
        输出:
        [
          ["ate","eat","tea"],
          ["nat","tan"],
          ["bat"]
        ]
"""

"""
 解题思路：
    本题的解法在于两点，第一点，字符串排序（字典序），第二点，哈希表存储
    掌握了这两点之后，本题的解法变得十分简单。
    
    我们首先遍历一次字符串数组，对里面的单个字符串进行排序，代码为 ''.join(sorted(s))
    然后判断拍完序之后的字符串，是否为字典的key，是的话，将原串s存到该key对应的value列表中，否则value=[s]
    
    最终，同一个key底下的字符串，即为字母异位词，收集每一个key对应的value，作为我们最终的返回结果。
"""


class Solution:
    def groupAnagrams(self, strs):
        d = dict()
        for s in strs:
            key = ''.join(sorted(s))
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
        res = []
        for key in d:
            res.append(d[key])
        return res
