# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/21 09:31
 @desc: 第98题
"""
"""
 解题思路：
    这是一个充分发挥二叉搜索树性质的思路，我们判断一棵树是否为二叉搜索树时，通过遍历它的每一个节点，判断它的值是否在正确的区间内即可。
    
    初始时，根结点的取值区间为(-∞，+∞)
    
    左儿子的取值区间则为(-∞，root.val -1]，右儿子的取值区间为[root.val+1,+∞)
    
    递归判断每一个节点的取值是否符合取值要求即可。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, root, minv, maxv):
        if not root:
            return True
        if root.val < minv or root.val > maxv:
            return False
        return self.dfs(root.left, minv, root.val - 1) and self.dfs(root.right, root.val + 1, maxv)


"""
    除了上面方法外，有另外一种较笨的思路，即判断二叉树的中序遍历顺序是否严格单调递增。
 
    实现起来也比较简单，设置一个temp值来存上一个节点值，比较当前节点值是否比上一个值大，是的话再把当前值存入temp
"""


class Solution2(object):
    res = True
    value = 0

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = True
        self.value = float('-inf')
        if not root:
            return True
        self.inorder(root)
        return self.res

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if root.val > self.value:
            self.value = root.val
        else:
            self.res = False
            return
        self.inorder(root.right)
