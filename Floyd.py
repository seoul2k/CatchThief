"""
算法具体过程由AI实现，算法为自行寻找哈。
"""
def floyd_warshall(graph, start, end):
    """
    使用弗洛伊德算法计算给定加权图中所有顶点对之间的最短路径，
    并返回从起点到终点的最短路径上的顶点。
    
    参数:
    graph (list of list of int): 图的邻接矩阵表示，其中graph[i][j]是从顶点i到顶点j的距离。
                                 如果不存在边，则距离可以设置为一个很大的数（如float('inf')）。
    start (int): 起点索引。
    end (int): 终点索引。
    
    返回:
    path (list of int): 从起点到终点的最短路径上的顶点列表。
                       如果没有路径存在，则返回空列表。
    """
    V = len(graph)
    dist = [[0 for _ in range(V)] for _ in range(V)]
    next_hop = [[None for _ in range(V)] for _ in range(V)]

    # 初始化dist矩阵为输入的邻接矩阵，并初始化next_hop矩阵
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]
            if graph[i][j] != float('inf') and i != j:
                next_hop[i][j] = j

    # 更新dist矩阵以考虑中间节点k
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_hop[i][j] = next_hop[i][k]

    # 重建路径
    def reconstruct_path(start, end):
        path = []
        u = start
        if dist[u][end] == float('inf'):
            return []  # 没有路径存在
        while u != end:
            path.append(u)
            u = next_hop[u][end]
        path.append(end)
        return path

    return reconstruct_path(start, end)