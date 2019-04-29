# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/29/19 4:12 PM
 @desc: 堆排序是一种树形选择排序，是对直接选择排序的有效改进
"""

"""
 我们在数据结构中，主要谈到的还是二叉堆，二叉堆有最大堆和最小堆之分。
 最大（最小）堆是一棵每一个节点的键值都不小于（大于）其孩子（如果存在）的键值的树。
 
 大顶堆是一棵完全二叉树，同时也是一棵最大树     【一棵深度为h的完全二叉树，前h-1层是满二叉树，第h层的所有叶子节点都集中在最左边】
 小顶堆是一棵完全二叉树，同时也是一棵最小树
    (a)大顶堆序列：（96, 83,27,38,11,09)
    (b)小顶堆序列：（12，36，24，85，47，30，53，91）
 需要注意的问题是：堆中的任一子树也还是堆，即大顶堆的子树也都是大顶堆，小顶堆同样
"""

"""
 1.基本思想：
    初始时把要排序的n个数的序列看作是一棵顺序存储的二叉树（一维数组存储二叉树），调整它们的存储序，使之成为一个堆，将堆顶元素输出，
 得到n个元素中最小(或最大)的元素，这时堆的根节点的值最小（或者最大）
    然后对前面(n-1)个元素重新调整使之成为堆，输出堆顶元素，得到n 个元素中次小(或次大)的元素。
    依此类推，直到只有两个节点的堆，并对它们作交换，最后得到有n个节点的有序序列。称这个过程为堆排序。

 2.时间复杂度：
    一般来说，对于树形的数据结构，时间复杂度为O(n*log n)
    
 3.稳定性分析：
    元素的位置会发生交换，因此堆排序是不稳定排序
 
 4.堆排序的强大之处，在于用于解决top-K问题，在本文结尾详细说明，面试可能会问到
"""


# 构建堆序列
def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index

    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


def heap_sort(unsorted):
    n = len(unsorted)
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted


if __name__ == '__main__':
    numbers = [int(x) for x in input().split()]
    print(heap_sort(numbers))

"""
 我们先看一个大数据top-K示例：

　例子：
    搜索引擎会通过日志文件把用户每次检索使用的所有检索串都记录下来，每个查询串的长度为1-255字节。假设目前有一千万个记录（这些查询串的重复度
 比较高，虽然总数是1千万，但如果除去重复后，不超过3百万个。一个查询串的重复度越高，说明查询它的用户越多，也就是越热门），请你统计最热门的10个
 查询串，要求使用的内存不能超过1G。

　　首先，我们知道这是一个典型的top-K问题。

    针对大数据问题进行统计首先应该想到的就是Hash_map。
    
    所以第一步就是先遍历全部的1千万Query，构建出一个大小为3百万的Hash_map，其中的key值为某条Query，对应的value值为该条Query的查询次数。
 建好Hash_map以后，我们接下来的问题就是如何在3百万的Query中找出10个最热门的Query，也就是要用到排序算法。排序算法中效率最高的时间复杂度为
 O(n*log(n))，这是最简单粗暴的方法，也是最直接的方法。
 
    或者我们进一步优化，该题目是要求寻找top-K问题，那么我们可以直接取前K个Query构建一个数组，然后对其进行排序。遍历剩余的全部Query，如果
 某条Query的查询次数大于数组中最小的一个，将数组中最小的Query剔除，加入这条新的Query。接着调整数组顺序，依次进行遍历，这样的最坏情况下的
 复杂度为O(n*K)    
    动画过程见：http://www.benfrederickson.com/heap-visualization/ 
    
    在上面的基础上，可以进一步优化，可以用小根堆来实现，具体过程如下：
    
    堆顶存放的是整个堆中最小的数，现在遍历N个数，把最先遍历到的k个数存放到最小堆中，并假设它们就是我们要找的最大的k个数，X1>X2...Xmin(堆顶)
 而后遍历后续的(n-K)个数，一一与堆顶元素进行比较，如果遍历到的Xi大于堆顶元素Xmin，则把Xi放入堆中，而后更新整个堆，更新的时间复杂度为logK，
 如果Xi<Xmin，则不更新堆，整个过程的复杂度为O(K)+O((N-K)*logK)=O（N*logK）
    
    这样一来，我们的时间复杂度从O(n*log n)到O(n*k)到O(n*log k)，一步步地进行了优化。
"""
