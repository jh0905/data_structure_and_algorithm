# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/29/19 6:40 PM
 @desc: 基数排序，属于“分配式排序”，又称“桶子法”
"""


def radix_sort(lst):
    radix = 10
    placement = 1
    max_digit = max(lst)
    while placement < max_digit:
        # declare and initialize buckets
        buckets = [list() for _ in range(radix)]
        # split lst between lists
        for i in lst:
            tmp = int((i / placement) % radix)
            buckets[tmp].append(i)
        # empty lists into lst array
        a = 0
        for b in range(radix):
            buck = buckets[b]
            for i in buck:
                lst[a] = i
                a += 1
        # move to next
        placement *= radix


if __name__ == "__main__":
    numbers = [int(x) for x in input().split()]
    radix_sort(numbers)
    print(numbers)
