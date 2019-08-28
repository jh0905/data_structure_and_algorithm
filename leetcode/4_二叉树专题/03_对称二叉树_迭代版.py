# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/21 11:21
 @desc: 第101题

        递归版解法，在剑指offer中学习过了，见上面 jianzhi_offer系列第22题

        本篇代码考察迭代版写法
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    在上一份代码中，我们学习了如何通过迭代的方式，对二叉树进行中序遍历。
    
    按照相同的思想，我们对当前二叉树，迭代地进行两种不同的"中序遍历"
    一种是正常的"左->根->右"的顺序，另一种是变种的"右->根->左"的顺序。
    
    将左链添加到lstack中，将右链添加到rtsack中，p指向根的左节点，q指向根的右儿子
    
    当p和q同时存在，将左链和右链加入到各自的栈中。循环结束时，正常情况p和q应该同为空,如果有一个不为空的话，直接返回False
    
    按照之前的思路，接下来应该是出栈操作，但是这里要提前判断一下栈是否都不为空，因为可能一开始的时候，就没有元素入栈。
    
    然后比较出栈的元素是否相等即可。
    
    最后就是添加右链和左链，p=p.right, q=q.left
"""


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        lstack = []
        rstack = []
        p = root.left
        q = root.right
        while p or q or lstack or rstack:
            while p and q:
                lstack.append(p)
                rstack.append(q)
                p = p.left
                q = q.right
            if p or q:  # 如果左链和右链节点，一个为空，另一个不为空，说明二叉树不对称
                return p and q
            if lstack and rstack:  # 判断栈是否为空
                p = lstack.pop()
                q = rstack.pop()
            if p.val != q.val:
                return False
            p = p.right
            q = q.left
        return True
