# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/23 15:05
 @desc: 第79题
"""
"""
 解题思路：
    
    深搜 + 回溯的思想
    
    从矩阵中的每一个元素进行深度搜索，self.dfs(board,word,idx,x,y)
    
    board和word分别为输入的矩阵和单词，idx表示当前枚举到的单词下标，x,y为当前搜索的矩阵元素
    
    如果 board[x][y] != word[idx] ，直接返回False，否则执行后面的代码
    
    如果 idx == len(word)-1，说明字符串全部匹配完成，返回True
    
    否则我们需要进行单词中下一个字符的匹配，先把本轮匹配的单词，在矩阵中设为特殊字符，避免二次匹配
    
    然后用 dx 和 dy 分别从四个方向进行深搜，如果返回True，那么就返回True，否则继续进行遍历
    
    然后前面没有返回，说明本轮字符查找失败，我们往上回溯，要记得把修改过的矩阵字符恢复，然后返回False给上一层
    
    
"""


class Solution:
    def exist(self, board, word):
        if not board or not word:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, 0, i, j):
                    return True
        return False

    def dfs(self, board, word, idx, x, y):
        if board[x][y] != word[idx]:
            return False
        if idx == len(word) - 1:
            return True
        board[x][y] = '#'  # 把已访问过的词设为障碍
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < len(board) and 0 <= b < len(board[0]):
                if self.dfs(board, word, idx + 1, a, b):
                    return True
        board[x][y] = word[idx]  # 回溯，还原字符
        return False


if __name__ == '__main__':
    _board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    _word = 'ABFDECS'
    print(Solution().exist(_board, _word))
