# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/24 16:44
 @desc:
"""
if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    res = ''
    for num in nums:
        if nums.count(num) <= m:
            res += str(num) + ' '
    print(res.rstrip())
