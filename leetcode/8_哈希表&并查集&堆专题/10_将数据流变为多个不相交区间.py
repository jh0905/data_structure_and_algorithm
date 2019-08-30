# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/30 19:51
 @desc: 第352题
"""

"""
    解题思路： 借助小根堆来实现
    
    (1)添加元素：
        我们直接把[x,x]添加到小根堆中
    
    (2)合并区间：
        我们把小根堆中的所有元素弹出来，将连续区间进行归并，弹出来的区间，必定有着一个递增的关系，即：
        按照顺序弹出来的[a,b],[c,d],[e,f]...一定满足 a<=b < c<=d < e<=f
        
        弹出来的区间是有顺序的，分情况讨论：
            如果merged为空，直接把区间加入到merged中；
            如果merge不为空，但是merge中最后一个区间的右边界 + 1 < 新加入区间的左边界，说明新加入的区间不需合并
            如果merge不为空，但是merge中最后一个区间的右边界 + 1 >= 新加入区间的左边界，说明需要合并，取新加入区间
            的右边界和原最后一个区间的右边界中的较大值，作为最终的右边界。
        
        当弹出来的区间处理完毕之后，merged就是此时最终的区间，而且是有序的，我们把merged再赋给小根堆。
            
        
"""

import heapq


class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.min_heap = []

    def addNum(self, val: int) -> None:
        heapq.heappush(self.min_heap, [val, val])

    def getIntervals(self):
        merged = []
        while self.min_heap:
            x = heapq.heappop(self.min_heap)
            if not merged or merged[-1][1] + 1 < x[0]:
                merged.append(x)
            else:
                merged[-1][1] = max(merged[-1][1], x[1])
        self.min_heap = merged
        return self.min_heap


if __name__ == '__main__':
    sol = SummaryRanges()
    sol.addNum(5)
    sol.addNum(2)
    sol.addNum(1)
    sol.addNum(7)
    print(sol.getIntervals())
    sol.addNum(3)
    sol.addNum(6)
    print(sol.getIntervals())
