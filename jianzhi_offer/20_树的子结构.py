# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isSame(self, root1, root2):
        if not root2:  # 树B中无待匹配节点
            return True
        if not root1 or root1.val != root2.val:  # 树B还有待匹配节点，树A中无节点了 或者 根结点的值不相等
            return False
        #  如果当前点匹配了，递归判断左右子树是否同样匹配
        return self.isSame(root1.left, root2.left) and self.isSame(root1.right, root2.right)

    def hasSubtree(self, pRoot1, pRoot2):
        """
        :type pRoot1: TreeNode
        :type pRoot2: TreeNode
        :rtype: bool
        """
        if not pRoot1 or not pRoot2:  # 空子树排除
            return False
        if self.isSame(pRoot1, pRoot2):  # 判断以pRoot1为根结点的树是否与以pRoot2为根结点的树相同（根节点必须相同）
            return True
        else:
            return self.hasSubtree(pRoot1.left, pRoot2) or self.hasSubtree(pRoot1.right, pRoot2)

