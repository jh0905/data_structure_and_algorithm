# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/7/30 20:15
 @desc: 层次遍历的重要特性，下标为i的节点，它的左孩子下标为2*i+1，右孩子为 2*2+2
"""

import math

nums = []


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def createTree(array):
    nodes = []
    n = len(array)  # n 表示树的节点总数
    m = int(math.log(n + 1, 2))  # m 表示树的层数 log(num,base:默认为e)，返回一个float值，得转为int
    # 将输入元素转化为树节点
    for i in range(n):
        if array[i] == '#':
            nodes.append(None)
        else:
            node = TreeNode(int(array[i]))
            nodes.append(node)
    # 如果树的层数为0，说明树不存在，直接返回None
    if m == 0:
        return None
    # 如果树的层数为1，说明只有一个根结点
    if m == 1:
        return nodes[0]
    # 如果树的层数>=2，则需要对节点分配左孩子和右孩子
    for i in range(pow(2, m - 1) - 1):  # 只遍历到倒数第二层的节点
        if nodes[i] is None:  # 当前节点为叶节点
            continue
        nodes[i].left = nodes[2 * i + 1]
        nodes[i].right = nodes[2 * i + 2]
    return nodes[0]


# 用前序遍历验证二叉树的创建结果
def preorder(root):
    if root is None:
        return
    nums.append(root.val)
    preorder(root.left)
    preorder(root.right)


if __name__ == '__main__':
    array = ['5', '4', '3', '#', '#', '2', '1', '#', '#', '#', '#', '1', '2', '#', '3']
    head = createTree(array)
    preorder(head)
    print(nums)
