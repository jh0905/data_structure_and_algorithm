# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/22/19 8:24 PM
 @desc: 分块查找法
"""

"""
    分块查找又称索引顺序查找，它是顺序查找的一种改进方法
    
    算法思想：将n个数据元素"按块有序"划分为m块（m ≤ n）。每一块中的结点不必有序，但块与块之间必须"按块有序"；
    
            即第1块中任一元素的关键字都必须小于第2块中任一元素的关键字；而第2块中任一元素又都必须小于第3块中的任一元素
            
    算法流程：
　　  step1 先选取各块中的最大关键字构成一个索引表；
　　  step2 查找分两个部分：先对索引表进行二分查找或顺序查找，以确定待查记录在哪一块中；然后，在已确定的块中用顺序法进行查找

    这里了解算法思想即可
"""
