# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/22 20:56
 @desc: 第208题   trie树，也叫字典树、前缀树、单词查找树
"""

"""
    我们来了解一下什么是trie树：
                                root 
                                / | \  
                               t  a  i
                              / \     \  
                             o   e     n
                                /|\    /
                               a d n   t
                               
    如上图所示，trie树是一种多叉树结构，表示了关键字集合{'a', 'to', 'tea','ted','ten','int'}
    
    它具有如下性质：
        (1) 根结点不包含字符，除根结点以外的每一个节点，都包含一个字符
        (2) 从根结点到任意一个节点，路径上的字符拼接起来，表示该节点对应的字符串
        (3) 每个单词的公共前缀，作为一个字符节点保存下来
        
    # 定义trie树节点：
            我们这里只考虑英文小写字母，所以这里的trie树是一个26叉树，每个节点最多有26个儿子。
            每个儿子代表着一个字符，如果第1个儿子存在，说明字符'b'已经在当前节点的儿子中了。
    
    # 添加操作：
            首先找到根结点，遍历要添加的字符串，找到第一个字母对应的节点索引，idx = ord(ch) - ord('a')，如果该idx对应的节点
            为空，则创建新节点，并把它赋值给当前节点的第idx个儿子。
            然后向下移动，到达idx个儿子，重复上面过程。
            最后一个字符处理完毕之后，把对应的is_end设为True
            
    # 搜索操作：
            找到根结点，遍历要添加的字符串，找到第一个字母对应的节点索引，idx = ord(ch) - ord('a')，如果该idx对应的节点
            为空，直接返回False,否则向下遍历。
            遍历结束之后，返回当前节点的is_end
            
    # 查询前缀操作：
            本操作和搜索操作整体一致，只是结尾的时候，不需要判断最后一个字符对应的节点的is_end是否为True.
            
"""


# 定义一个前缀树节点的代码
class TrieNode:
    def __init__(self):
        self.nodes = [None] * 26
        self.is_end = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        for ch in word:
            idx = ord(ch) - ord('a')  # 找到当前字母是第几个儿子，'a','b','c'对应的index分别为0，1，2，...,25
            if not p.nodes[idx]:  # 该儿子不存在，则创建node
                p.nodes[idx] = TrieNode()
            p = p.nodes[idx]  # 然后p走到该儿子节点
        p.is_end = True  # 单词中的最后一个字符，对应的is_end设为True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not p.nodes[idx]:
                return False
            p = p.nodes[idx]
        return p.is_end  # 如果最后一个字符，对应的is_end为True,则返回True，否则返回False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # 思路和search一样，只是不需要判断is_end
        p = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not p.nodes[idx]:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
