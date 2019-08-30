# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/30 16:24
 @desc: 第692题
"""

"""
    解题思想：   哈希表 + 小根堆
    
    首先把单词映射到哈希表中，可以统计出各个单词出现的次数，然后对value进行排序，输出前k个单词
    b = sorted(a.items(),key = lambda item:item[1],reverse=True)
    
    问题在于排序的时间复杂度为O(n log n)，而本题的要求是O(n log k)，所以我们考虑堆的数据结构。
    
    我们要统计次数最大的k个值，那么我们需要维护一个最小堆，堆的最大元素数为k，当输入元素大于堆顶元素时，弹出堆顶元素。
    
    python实现了一个小根堆的模块heapq:
        heap = []
        - heapq.heappop(heap) 弹出堆顶元素
        - heapq.heappush(heap,x) 将元素插入到堆heap中，直接对list修改，无返回值
        - heapq.nlargest(k,heap) 返回小根堆中最大的k个元素（降序）
        - heapq.nsmallest(k,heap) 返回小根堆中最小的k个元素（升序）
"""


class Solution:
    def topKFrequent(self, words, k):
        frequent, heap = {}, []
        for word in words:
            frequent[word] = frequent.get(word, 0) + 1
        import heapq
        for word in frequent:
            heapq.heappush(heap, [-frequent[word], word])  # 先比较第一项元素，第一项相等，比较第二项的字典序
            # 我们要保证heap里面的item,有着相同的单调性，第一项大的item靠前，第一项相等时，第二项字典序大的靠前
            # 因此，我们把单词出现频率取反
        return [item[1] for item in heapq.nsmallest(k, heap)]


if __name__ == '__main__':
    w = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    print(Solution().topKFrequent(w, k))
