# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/25/19 8:35 AM
 @desc: 有一个文本串S，和一个模式串P，现在要查找P在S中的位置，怎么查找呢？

        本文核心内容： KMP算法（Knuth-Morris-Pratt三个人名组成），是一个字符串查找算法，在一个文本串中查找模式串的出现位置

        PMT为什么有用？参看：http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html
"""

"""
 1.暴力匹配的思路，并假设现在文本串S匹配到 i 位置，模式串P匹配到 j 位置，则有：
    如果当前字符匹配成功（即S[i] == P[j]），则i++，j++，继续匹配下一个字符；
    如果失配（即S[i]! = P[j]），令i = i - (j - 1)，j = 0。相当于每次匹配失败时，i 回溯到，j 被置为0
    
    可以这样子想象：
        
        一开始文本串S和模式串P头部对齐，然后比较第一个元素，相同的话，比较下一个元素，如果遇到有不同的元素，那么就
    将文本串S向左拉动一格，重复上面的比较操作，可以用两张小纸条，模拟这个过程。
    
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
 2.利用Python的语言特性，还有一种朴素查找的方法，思想也比较简单
"""


def naive_match(string, pattern):
    m = len(string)
    n = len(pattern)
    for i in range(m - n + 1):
        if string[i:i + n] == pattern:
            return i
    return -1


"""
"""

"""
 3.KMP算法，个人思路及实现
 
 看之前一定要读的话！
 
 这是我根据KMP算法的原理，利用了Python的特性，来想的如何生成PMT表（或称为next数组），效率可能低一点，但是更好理解
 
 【PMT表中下标为i对应的元素x】 等于 【在KMP算法中，pattern串第i个元素匹配失败时，p串的指针应该回退的index值为x】
 
"""


def partial_match_table(pattern):
    length = len(pattern)
    pmt = [-1] + [0] * (length - 1)  # pmt[0]必须为-1，它的作用是指示S串的指针，P串的指针都要向后移一位
    for i in range(1, length):
        current_str = pattern[:i]  # 当前index所指定的str
        prefix = {current_str[:j] for j in range(1, len(current_str))}  # 将current_str所有的前缀保存在集合中
        postfix = {current_str[j:] for j in range(1, len(current_str))}  # 将current_str所有的后缀保存在集合中
        intersection = prefix & postfix
        if len(intersection) == 0:  # 前后缀集合的交集为空
            pmt[i] = 0
        else:
            pmt[i] = max({len(x) for x in intersection})
    return pmt


def kmp(string, pattern):
    pmt = partial_match_table(pattern)  # pmt也就是很多文章常提到的next数组
    s_len = len(string)
    p_len = len(pattern)
    s_ptr = 0  # 指向string的指针
    p_ptr = 0  # 指向pattern的指针
    while s_ptr < s_len:
        if p_ptr == -1 or string[s_ptr] == pattern[p_ptr]:
            s_ptr += 1
            p_ptr += 1
        else:
            p_ptr = pmt[p_ptr]  # p_ptr回溯到PMT表中对应的index
        if p_ptr == p_len:
            return s_ptr - p_ptr
    return -1


if __name__ == '__main__':
    s = input()
    p = input()
    print(brute_force_search(s, p))
    print(naive_match(s, p))
    print(kmp(s, p))
