# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/3 14:01
 @desc:
"""


class Solution:
    seq = []

    def verifySequenceOfBST(self, sequence):
        """
        :type sequence: List[int]
        :rtype: bool
        """
        self.seq = sequence
        if not self.seq:  # 空二叉树
            return True
        return self.dfs(0, len(self.seq) - 1)

    def dfs(self, l, r):
        if l >= r:  # 说明当前分支的节点数为空
            return True
        k = l
        for i in range(l, r):
            if self.seq[i] >= self.seq[r]:
                break
            k += 1

        for j in range(k, r):
            if self.seq[j] <= self.seq[r]:
                return False
        return self.dfs(l, k - 1) and self.dfs(k, r - 1)


if __name__ == '__main__':
    sequence = [7, 4, 6, 5]
    print(Solution().verifySequenceOfBST(sequence))
