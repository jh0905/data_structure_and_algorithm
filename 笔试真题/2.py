# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/23 20:18
 @desc: 贝壳笔试，统计字符串划分的方案数，结果等于指定值
"""


def get_nums(s, a):
    if a not in s:
        return 0
    cnt = s.count(a)  # 统计a出现了多少次
    idxs = []  # 把a字符所以的索引存起来
    t = -1
    for i in range(cnt):
        idx = s.find(a, t + 1)
        t = idx
        idxs.append(idx)
    res = 0
    for idx in idxs:
        j = idx
        c = len(a)
        while j >= 0 and int(s[j:idx + c]) == int(a):
            j -= 1
            res += 1
    cnt = s.count('100000000')
    idxs = []
    t = -1
    for i in range(cnt):
        idx = s.find('100000000', t + 1)
        t = idx + 8
        idxs.append(idx)
    for idx in idxs:
        j = 1
        while idx + 9 + j < len(s):
            num = int(s[idx:idx + 9 + j]) % 1000000007
            if num < int(a):
                j += 1
            elif num == int(a):
                res += 1
                # 找到之后，可以判断100000000前面有多少个0
                k = idx - 1
                while k >= 0 and s[k] == '0':
                    res += 1
                    k -= 1
                break
            else:
                break
    return res


if __name__ == '__main__':
    s = input()
    n = int(input())
    for i in range(n):
        a = input()
        print(get_nums(s, a))
