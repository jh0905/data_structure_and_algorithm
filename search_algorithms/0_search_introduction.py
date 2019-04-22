# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/22/19 9:11 AM
 @desc: 查找算法简介
"""
"""
 引子：
    查找是在大量的信息中寻找一个特定的信息元素，在计算机应用中，查找是常用的基本运算，例如编译程序中符号表的查找。本文简单概括性的介绍了常见的
 六种查找算法，分别是顺序查找、二分查找、差值查找、树查找、分块查找以及哈希查找，之后逐一进行详细介绍。
 
 关于查找的相关概念：
    
    1.查找定义：
      
        根据给定的某个值，在表中确定一个其关键字等于给定值的数据元素（或记录）
    
    2.查找算法分类：
    
        (1)静态查找和动态查找
            静态或者动态都是针对查找表而言的。动态表指查找表中有删除和插入操作的表
        
        (2)无序查找和有序查找
            无序查找：被查找数列有序无序均可；
            有序查找：被查找数列必须为有序数列；
        
    3.平均查找长度（Average Search Length,ASL）
        
        需要和指定的key进行比较的关键字的个数的期望值，称为查找算法在查找成功时的平均查找长度
        
        对于含有n个数据元素的查找表，查找成功的的平均查找长度为 ASL = Pi*Ci的和，其中Pi表示查找表中第i个数据元素的概率，Ci为找到第i个数据
    元素时已经比较过的次数
        
    
"""
