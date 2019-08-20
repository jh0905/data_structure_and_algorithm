class Solution:
    # 正视图、侧视图、俯视图
    def get_area(self, rows, cols, mat):
        import numpy as np
        mat = np.array(mat)
        # 正视图，每一列的最大值
        a = 0
        for i in range(cols):
            a += max(mat[:, i])
        # 侧视图，每一行的最大值
        b = 0
        for i in range(rows):
            b += max(mat[i])
        # 俯视图，矩形中非零元素个数
        c = 0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] != 0:
                    c += 1
        res = (a + b + c) * 2
        return res


if __name__ == '__main__':
    rows, cols = [int(x) for x in input().strip().split()]
    import sys

    mat = []
    lines = sys.stdin.readlines()
    for line in lines:
        mat.append([int(x) for x in line.strip().split()])
    print(Solution().get_area(rows, cols, mat))
