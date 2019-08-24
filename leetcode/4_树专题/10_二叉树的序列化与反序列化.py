# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/21 17:16
 @desc: 第297题
"""

"""
    我们根据层次遍历，将二叉树序列化成字符串的形式，如
 
                                6
                              /  \ 
                             3    9
                                   \ 
                                    4
    序列化成：  "6 3 9 # # # 4 # # "    
    
    做法是，根据层次遍历的模板代码，稍微不同的是，不去判断当前节点是否存在左、右子树，而是直接加入到队列中
    如果弹出的节点不为空，则把节点值添加到字符串中，并往队列中添加当前节点的左右孩子
    如果弹出的节点为空，则往字符串中添加 #  
    每轮判断完节点，都要往字符串中添加一个空格
    最终队列为空时结束
    
    反序列化过程：
    
    首先把字符串分割成列表，用s表示，如果list中的第一个元素为'#'，说明树为空，直接返回None
    否则的话，第一个节点即为根结点，把它保存起来，再定义i=1,表示从s中的第二个元素开始。
    第一轮出来的是TreeNode(6)，不为空，于是添加左右儿子，发现s[1]和s[2]不为空，于是把左右儿子转成树节点，i+=2,添加儿子到队列中
    下一轮出来的是TreeNode(3)，不为空，于是添加左右儿子，发现s[3]和s[4]都为#，于是左右儿子设为None,i+=2，并添加到队列中
    下一轮出来的是TreeNode(9)，不为空，于是添加左右儿子，发现s[5]为#，s[6]不为空，转换成对应的节点,i+=2，并添加到队列中
    下一轮出来的是None,为空，不进行任何处理，直接进入下一轮
    下一轮出来的是None,为空，不进行任何处理，直接进入下一轮
    下一轮出来的是None,为空，不进行任何处理，直接进入下一轮
    下一轮出来的是TreeNode(4),不为空，于是添加左右儿子，发现s[7]和s[8]都为#，于是把左右儿子设为None,i+=2，并添加到队列中
    下一轮出来的是None,为空，不进行任何处理，直接进入下一轮
    下一轮出来的是None,为空，不进行任何处理，直接进入下一轮
    最终队列为空，退出循环。
        
    
                    
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        s = ''
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                s += str(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                s += '#'  # 表示该节点为空
            s += ' '
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        s = data.split(',')
        if s[0] == '#':
            return None
        root = TreeNode(int(s[0]))
        queue = [root]
        i = 1
        while queue:
            node = queue.pop(0)
            if node:
                node.left = TreeNode(int(s[i])) if s[i] != '#' else None
                node.right = TreeNode(int(s[i + 1])) if s[i + 1] != '#' else None
                i += 2  # i往后移两位
                queue.append(node.left)
                queue.append(node.right)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
if __name__ == "__main__":
    node1 = TreeNode(6)
    node2 = TreeNode(3)
    node3 = TreeNode(9)
    node4 = TreeNode(4)

    node1.left = node2
    node1.right = node3
    node3.right = node4
    sol = Codec()
    print(sol.serialize(node1))
