# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/5 18:40
 @desc:
"""
import heapq


class Solution(object):
    def getLeastNumbers_Solution(self, input, k):
        """
        :type input: list[int]
        :type k: int
        :rtype: list[int]
        """
        heap = []  # 维护一个元素个数为k的最大堆结构
        for x in input:
            heapq.heappush(heap, -x)
            if len(heap) > k:
                heapq.heappop(heap)  # 弹出最小元素，即实际上最大元素的相反数
        res = heapq.nlargest(k, heap)  # 从大到下排列的k个值，如[-1,-2,-3]
        return [-x for x in res]
    # return heapq.nsmallest(k, input)
