# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/21 10:42
 @desc: 第94题
"""
"""
    递归版的中序遍历思路和代码都比较简单：
    def inOrder(self, root):
        if root==None:
            return []
        return self.inOrder(root.left)+[root.val]+self.inOrder(root.right)
        
    而本题考察的是迭代版本的中序遍历，解题思路如下：
    
    将整棵二叉树的最左边一条链压入栈中，每次取出一个栈顶元素，并判断是否存在右子树，存在的话，将右子树压入栈中。
    
    经典代码，考虑背下来。
 
"""


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return []
        stack = []
        p = root
        while p or stack:
            while p:  # 将左链上的所有节点全部压入栈中
                stack.append(p)
                p = p.left
            p = stack.pop()  # 弹出栈顶元素
            res.append(p.val)
            p = p.right  # 考虑栈顶元素是否存在右子树，如果存在的话，对右子树重复上面操作
        return res
