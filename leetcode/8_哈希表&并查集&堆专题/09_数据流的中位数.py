# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/30 17:12
 @desc: 第295题
"""
"""
    解题思路：对顶堆来实现
    
    小根堆来维护比中位数大的那一部分元素，大根堆维护比中位数小的那一部分元素
    
    大根堆的堆顶元素是它的最大值，小根堆的堆顶元素是它的最小值。
    
    要求中位数，规定：
        如果元素总个数n为偶数，则大根堆和小根堆的元素个数都为 n/2，中位数为两个堆顶元素的平均数
        如果元素总个数n为奇数，则大根堆和小根堆的元素个数分别为 n//2 + 1，n//2，中位数为大根堆的堆顶元素
        
    所以我们要一直动态维护两个堆的元素即可。
    
    具体过程：
        新的元素插入大根堆 -> 弹出大根堆的最大值 -> 弹出的最大值插入小根堆
        
        如果当前插入的是第奇数个元素，则把小根堆的堆顶元素弹出来，插入到大根堆中，此时大根堆元素比小根堆元素多1
        如果当前插入的是第偶数个元素，则不弹出小根堆的元素，此时大根堆元素和小根堆元素相等
"""

import heapq


class MedianFinder:

    def __init__(self):
        self.cnt = 0  # 统计当前传入的是第几个元素
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        self.cnt += 1
        heapq.heappush(self.max_heap, [-num, num])  # heapq是小根堆，为了模拟大根堆，把num进行取反
        _, max_heap_top = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_heap_top)
        if self.cnt & 1:
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, [-min_heap_top, min_heap_top])

    def findMedian(self) -> float:
        if self.cnt & 1:
            return self.max_heap[0][1]  # heapq对应的堆，第0个元素为堆顶元素，其余不是按顺序排的
        else:
            return (self.max_heap[0][1] + self.min_heap[0]) / 2
