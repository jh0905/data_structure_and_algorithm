# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/25/19 8:35 AM
 @desc: 有一个文本串S，和一个模式串P，现在要查找P在S中的位置，怎么查找呢？
"""

"""
 暴力匹配的思路，并假设现在文本串S匹配到 i 位置，模式串P匹配到 j 位置，则有：
    如果当前字符匹配成功（即S[i] == P[j]），则i++，j++，继续匹配下一个字符；
    如果失配（即S[i]! = P[j]），令i = i - (j - 1)，j = 0。相当于每次匹配失败时，i 回溯到，j 被置为0
    
 暴力搜索的思路，可以这样子想象，一开始文本串S和模式串P头部对齐，然后比较第一个元素，相同的话，比较下一个元素，如果遇到有不同的元素，那么就
    将文本串向左移动一格，重复上面的比较操作。
    
    停止条件：文本串S向左全部移动完了，或者找到了字符串S中pattern串的位置
    
 暴力匹配的时间复杂度为O(n*m) ，其中 n 为 S 的长度，m 为 P 的长度。很明显，这样的时间复杂度很难满足我们的需求。
 之后要介绍的KMP算法，时间复杂度为O(n+m)
"""


def brute_force_search(string, pattern):
    i = j = 0
    while i < len(string) and j < len(pattern):
        if string[i] != pattern[j]:
            i = i - j + 1  # 回退到str中，第一个匹配成功点的下一位置
            j = 0
        else:
            i += 1
            j += 1
    if j == len(pattern):
        return i - j  # 匹配成功，返回文本串S中，等于pattern第一个元素的索引
    else:
        return -1  # 匹配失败


"""
 KMP算法（Knuth-Morris-Pratt三个人名组成），是一个字符串查找算法，在一个文本串中查找模式串的出现位置
"""


def generate_next(string):
    next_array = [-1] + [0] * (len(string) - 1)
    i = 0
    j = -1
    while i < len(string):
        if j == -1 or string[i] == string[j]:
            i += 1
            j += 1
            next_array[i] = j
        else:
            j = next_array[i]
    return next_array


if __name__ == '__main__':
    s = input()
    p = input()
    print(brute_force_search(s, p))
