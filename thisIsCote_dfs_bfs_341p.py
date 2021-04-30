N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))
temp = [[0]*M for _ in range(N)]

result = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def get_score():
    score = 0
    for i in range(N):
        # print(temp[i])
        for j in range(M):
            if temp[i][j] == 0:
                score += 1
    # print()
    return score

def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx,ny)

def dfs(count):
    global result
    if count == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j] = graph[i][j]
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    virus(i,j)
        a = get_score()
        # print("get_score(): ",get_score())
        result = max(result,a)
        return 
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                count -= 1
                graph[i][j] = 0

dfs(0)
print(result)