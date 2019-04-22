# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/22/19 3:36 PM
 @desc: 最简单的有二叉树查找算法，优化后的平衡查找树之2-3查找树、平衡查找树之红黑树，下面逐一进行介绍，并补充一些关于树的知识
"""
"""
 1.二叉查找树算法
    (1)基本思想
        二叉查找树是先将待查找的数据生成一棵树，确保树的左分支的值小于右分支的值，这个算法的查找效率很高，但是要求首先建立一棵二叉搜索树.
        
    (2)二叉查找树(BinarySearchTree，也叫二叉搜索树，或者二叉排序树BinarySortTree)，要求具有如下性质：
        (a)若任意节点的左子树不为空，那么左子树所有节点上的值，均小于根节点上的值；
        (b)若任意节点的右子树不为空，那么右子树所有节点上的值，均大于根节点上的值；
        (c)任意节点的左右子树，也分别为二叉查找树
        
    (3)二叉查找树的插入
        二叉排序树是一种动态树表。
        其特点是：树的结构通常不是一次生成的，而是在查找过程中，当树中不存在关键字等于给定值的结点时再进行插入。
        【新插入的结点一定是一个新添加的叶子结点，并且是查找不成功时查找路径上访问的最后一个结点的左孩子或右孩子结点!!!】 
        
    (4)二叉查找树的查找/搜索
        (a)首先将关键字与根节点的值进行比较，若相等则查找成功
        (b)若小于根节点的值，则递归地查找左子树
        (c)若大于根节点的值，则递归地查找右子树
        (d)若子树为空，则查找不成功
    
    (5)二叉查找树的性质
        二叉查找树使用中序遍历，即可得到有序的数列
    
    (6)二叉查找树查找与插入的时间复杂度
        平均时间复杂度为O(log n),最坏的情况下也可能是O(n)，此时二叉树结构像一条直线,为了避免这种极度不平衡的状态，后面才引入平衡树的优化!
"""


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 求树的深度
def depth(root):
    if root is None:
        return 0
    return 1 + max(depth(root.left), depth(root.right))


# 递归实现，先序用pre_order表示，后序用post_order表示
def in_order_traverse(root):
    if root is None:
        return None
    in_order_traverse(root.left)
    print(root)
    in_order_traverse(root.right)


# 非递归实现
def in_order_traverse_2(root):
    if root is None:
        return None
    stack = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = root.left
        node = stack.pop()  # while结束，表示已经访问到最左的左节点了
        print(node.val)
        node = node.right


# 递归实现算法----二叉查找树的搜索算法
def binary_search(root, key):
    if root is None or root.val == key:
        return root
    if root.val > key:
        return binary_search(root.left, key)
    if root.val < key:
        return binary_search(root.right, key)


# 迭代实现算法----二叉查找树的搜索算法
def binary_search_2(root, key):
    while root and root.val != key:
        if root.val > key:
            root = root.left
        else:
            root = root.right
    return root


"""
 2.平衡查找树之2-3Tree【这里只做了解，不给出代码】
    (1)2-3查找树定义
        2-3Tree中，每个节点保存1个或者2个值
            对于保存一个值的节点，称为2节点，它保存一个key并指向左、右节点；
            对于保存两个值的节点，称为3节点，它保存两个值key1和hey2，并指向左、中、右三个节点；
    
    (2)2-3查找树每个节点的要求
        (a)要么为空，否则：
        (b)对于2节点，必须满足左子树上所有的值均小于key，右子树上所有的值均大于key
        (c)对于3节点（有key1,key2,且key1<key2），必须满足左子树的值均小于key1，中子树的值均处于(key1,key2)区间，右子树的值均大于key2
        
    (3)2-3查找树的性质
        (a)如果中序遍历2-3查找树，可以得到排好序的数列
        (b)在一棵完全平衡的2-3查找树中，根节点到每一个为空节点的距离相等（平衡的要求）
        (c)避免了上面二叉排序树中，那种最坏的情况（除了根节点以外的所有节点全为左节点或右节点），所有时间复杂度最坏时也是O(log n) 
        
    (4)时间复杂度分析
        2-3查找树的查找效率与树的高度是息息相关的!     （插入与查找效率一致）
        (a)在最坏的情况下，也就是所有的节点都是2-node节点，查找效率为O(log2 n)
        (b)在最好的情况下，也就是所有的节点都是3-node节点，查找效率为O(log3 n)    
        
        
 3.平衡查找树之红黑树Red-Black Tree【这里只做了解，不给出代码】
    2-3查找树能保证在插入元素之后能保持树的平衡状态，最坏情况下即所有的子节点都是2-node，树的高度为log2 n，从而保证了最坏情况下的时间复杂度
    
    但是2-3树实现起来比较复杂，于是就有了一种简单实现2-3树的数据结构，即红黑树（Red-Black Tree）
    
    (1)红黑树的基本思想
        红黑树是将节点之间的链接分为两种不同的类型，红色链接，它用来链接两个2-node节点来表示一个3-node节点；
        黑色链接用来链接普通的2-node节点，没有实际意义，相当于前面说的2-node节点；
        
        特别地，使用红色链接的两个2-node节点，要向左旋转，即一个是另一个的左节点的形式，用node1表示左子节点，node2表示父节点，其中node1的
        左子树上所有的值小于node1的值，node1右子树上所有的值都大于node1的值，但是小于node2的值，node2右子树的所有的值都大于node2的值；
        
        我们如果把红色链接水平绘制，那么它链接的两个2-node，就会形似2-3树的3-node了
    
    (2)红黑树的性质
        (a)红黑树的红色链接向左倾斜
        (b)一个节点不可能有2个红色链接，因为如果有2个链接，最后会形成一个含有3个值的节点，这与3-node只含有2个节点相违背
        (c)整棵树完全黑色平衡，即从根节点到所有叶子节点的路径上，黑色链接的个数相同
    
    (3)时间复杂度分析
        红黑树的平均高度为log2 n，它其实就是2-3查找树的一种实现，能保证最坏情况下仍然具有对数的时间复杂度!
    
 4.树表查找总结
    二叉查找树平均查找性能不错，为O(log n)，但是最坏情况会退化为O(n)，为了避免最坏情况，我们对数据结构做了优化，提出平衡查找树，保证树的高度
 在对数范围内，但是2-3查找树在实现起来比较困难，为此提出红黑树的概念，它实际上就是2-3树的一种简单高效的实现，红黑树是一种比较高效的平衡查找树，
 应用十分广泛，除此之外，2-3查找树的另一个扩展——B/B+平衡树，在文件系统和数据库系统中有着广泛的应用.
            
"""
