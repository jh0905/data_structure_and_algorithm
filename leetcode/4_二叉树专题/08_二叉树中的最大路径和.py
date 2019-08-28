# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/21 16:01
 @desc: 第124题
"""
"""
  本题思路和上一题有相通之处，每一个节点有一个权重，以该节点为根结点的路径最大值有三种情况：
    (1) 从根结点往左子树走，不一定到达左子树的根结点，此时 max_path = root.val + L
    (2) 从根结点往右子树走，不一定到达右子树的根结点，此时 max_path = root.val + R
    (3) 不走，路径只有该节点一个节点，当L和R都小于0时取这种情况
    
  重点：##
  
    最终取得的最大值，如果小于0，则应当返回0，表示我们在计算最大路径时，不考虑该分支的路径长度。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    ans = 0

    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float('-inf')
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.ans = max(self.ans, left + right + root.val)
        # 原始为：max(0,max(root.val,root.val+left,root.val+right))
        # 可以把root.val提出来，得到 max(0,root.val+max(0,left,right))
        # 因为left和right是大于等于0的，所以内层的0也可以去掉，max(0,root.val+max(left,right))
        return max(0, root.val + max(left, right))  # 如果最大值小于0的话，则返回0，对应我们说明的三种情况
