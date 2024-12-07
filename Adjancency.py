import Floyd as a
import random as r
#邻接矩阵
adjacency = [[float('inf') for i in range(50)] for j in range(50)]
#邻接矩阵初始化
for i in range(50):
    for j in range(50):
        if i == j:
            adjacency[i][j] = 0
        elif i < j:
            if r.randint(1, 10) > 2:
                adjacency[i][j] = r.randint(1, 10)
                adjacency[j][i] = adjacency[i][j]
            else:
                adjacency[i][j] = float('inf')
                adjacency[j][i] = adjacency[i][j]
