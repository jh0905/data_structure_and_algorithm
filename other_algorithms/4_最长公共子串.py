# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/23/19 2:35 PM
 @desc: 给出两个字符串（可能包含空格）,找出其中最长的公共连续子串,输出其长度
"""
"""
 输入描述:
    输入为两行字符串（可能包含空格），长度均小于等于50.

 输出描述:
    输出为一个整数，表示最长公共连续子串的长度。

 输入例子:
    abcde
    abgde

 输出例子:
    2
"""

"""
 1.第一个思路，暴力破解法，比如说字符串'abcdefghi'和'defgk'，选择长度较短的那一个，利用Python的语言特性 'in'函数，如str_1 in str_2
   进行遍历，先判断 'defgk' in 'abcdefghi'是否为True，不是的话，再选择长度为4的字符串，'defg;或'efgk' in 'abcdefghi'进行判断，下
   一轮选择长度为3的字符串， 一旦满足为True，直接返回该子串，长度当然也就知道了
"""


def brute_force_match(str_1, str_2):
    s1 = str_1 if len(str_1) > len(str_2) else str_2  # s1是较长的那个字符串
    s2 = str_1 if len(str_1) < len(str_2) else str_2  # s2是较短的那个字符串
    length = len(s2)
    for i in range(length, 0, -1):
        candidate_set = {s2[j:i + j] for j in range(length - i + 1)}  # 生成s2中长度为i的字符串集合
        for s in candidate_set:
            if s in s1:  # 这里有偷懒的嫌疑，直接判断某个字串是否在s1内
                return s
    return -1


if __name__ == '__main__':
    string_1 = input()
    string_2 = input()
    print(brute_force_match(string_1, string_2))
