# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 7/7/19 8:26 PM
 @desc:
"""


def check(num, target):
    if num < target:
        return 1
    else:
        return 0


def bi_search(numbers, target):
    l = 0  # 二分查找的下界为原始下界
    r = len(numbers)  # 二分查找的上界，一定要为真实上界加1
    res = -1
    while l < r:
        mid = (l + r) // 2
        # 判断numbers[mid]是否小于target
        if check(numbers[mid], target):
            l = mid + 1
        else:
            r = mid
            res = mid  # 如果存在搜索结果的话，一定是在mid处取到
    if numbers[res] == target:
        return res
    else:
        return -1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    tar = 2
    print(bi_search(nums, tar))
