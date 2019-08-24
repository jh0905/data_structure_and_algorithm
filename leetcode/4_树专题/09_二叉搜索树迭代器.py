# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/21 16:35
 @desc: 第173题
        实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。

        调用 next() 将返回二叉搜索树中的下一个最小的数。
"""

"""
 解题思路：
     解法和前面学习的迭代式中序遍历二叉搜索树的代码一样，只不过是在这里，将原代码拆分成两部分。
     
     初始化的时候，把二叉树的最左链加入到栈中
     
     弹出元素的时候，判断弹出的节点是否存在右子树，存在的话，就把该右子树的最左链加入。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    stack = []

    def __init__(self, root: TreeNode):  # 初始化时，把最左边的链加进来
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        p = self.stack.pop()
        res = p.val
        p = p.right
        while p:  # 如果存在右子树，把右子树的最左边的链加入栈中
            self.stack.append(p)
            p = p.left
        return res

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
