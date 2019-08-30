# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/29 19:21
 @desc: 远景
"""
if __name__ == '__main__':
    nums = list(map(int, input().split(',')))
    k = int(input())
    x = int(input())
    d = dict()
    for num in nums:
        if not abs(num - x) in d:
            d[abs(num - x)] = [num]
        else:
            d[abs(num - x)].append(num)
    res = []
    nd = sorted(d)
    flag = True
    i = 0
    while flag:
        for j in d[nd[i]]:
            res.append(j)
            k -= 1
            if k == 0:
                flag = False
                break
        i += 1
    res = [str(x) for x in sorted(res)]
    print(','.join(res))
