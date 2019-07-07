# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 7/7/19 1:34 PM
 @desc:
"""
import sys

lines = sys.stdin.readlines()
input_mat = []
for line in lines:
    input_mat.append([int(x) for x in line.strip().split()])

rows = len(input_mat)
columns = len(input_mat[0])

# 初始化distance矩阵，shape和输入矩阵一样，目的是存储矩阵中每个点距离起点的距离
dist_mat = [[-1 for i in range(columns)] for j in range(rows)]

# 第一步：把第一轮遍历的起点坐标加入到队列中
queue = []
for i in range(rows):
    for j in range(columns):
        if input_mat[i][j] == 2:
            dist_mat[i][j] = 0
            queue.append([i, j])

# 每一对[dx,dy]表示朝上下左右的某一个方向移动
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 第二步：开始 bread first search
while queue:
    idx_x, idx_y = queue.pop(0)  # 弹出队列中的第一个元素
    for i in range(4):
        x = idx_x + dx[i]
        y = idx_y + dy[i]
        # 如果上下左右的点，索引没有越界，并且它对于的值为1，而且它还没被访问过dist_mat[x][y] == -1
        if 0 <= x < rows and 0 <= y < columns and input_mat[x][y] == 1 and dist_mat[x][y] == -1:
            dist_mat[x][y] = dist_mat[idx_x][idx_y] + 1  # 当前点距起点的距离，等于它上一点的距离值+1
            queue.append([x, y])  # 把这个点添加到队列中，之后继续执行bfs

# 第三步：遍历距离矩阵，找到-1则返回-1，否则返回矩阵中最大的值
res = 0
for i in range(rows):
    for j in range(columns):
        if dist_mat[i][j] == -1:
            res = -1
        else:
            res = max(res, dist_mat[i][j])
print(res)
