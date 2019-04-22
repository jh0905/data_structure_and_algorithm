# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/22/19 9:35 AM
 @desc: 顺序查找法，适合于存储结构为顺序存储或链式存储的线性表
"""

"""
 1.基本思想：
 
    顺序查找也称为线形查找，属于无序查找算法。从数据结构线形表的一端开始，顺序扫描，依次将扫描到的结点关键字与给定值k相比较，若相等则表示
 查找成功；若扫描结束仍没有找到关键字等于k的结点，表示查找失败；
    
 2.复杂度分析：
 
    查找成功时的平均查找长度：（假设每个数据元素概率相等）ASL = 1 / n * (1+2+3+...+n) = (n+1)/2
    查找不成功时，需要进行n次比较，时间复杂度为O(n)

"""


# 顺序查找实现代码
def sequence_search(nums, key):
    for i, num in enumerate(nums):
        if num == key:
            return i
    return -1


if __name__ == "__main__":
    search_nums = [1, 2, 3, 8, 3, 4, 2, 1]
    search_key = 4
    print(sequence_search(search_nums, search_key))
