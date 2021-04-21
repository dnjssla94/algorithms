from collections import deque

# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]
# dfs_visited = [False]*9
# bfs_visited = [False]*9
# dfs_result = []
# bfs_result = []

def dfs(graph, node, visited):
    # print('node: ',node)
    dfs_result.append(node)
    visited[node] = True
    for i in graph[node]:
        if visited[i] == False:
            dfs(graph,i,visited)

def bfs(graph, start, visited):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if visited[node] == False:
            visited[node] = True
            bfs_result.append(node)
            queue.extend(graph[node])
start = 1
dfs(graph, start, dfs_visited)
print("dfs_result: ",dfs_result)
bfs(graph,start,visited)
print("bfs_result: ",bfs_result)
