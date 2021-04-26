from collections import deque
import sys

N, L, R = map(int,sys.stdin.readline().split())
ground = []
for i in range(N):
    ground.append(list(map(int,sys.stdin.readline().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def process(x, y, index):
    united = []
    queue = deque()

    union[x][y] = index
    united.append([x,y])
    queue.append([x,y])
    summary = ground[x][y]
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == -1:
                if L <= abs(ground[x][y] - ground[nx][ny]) <= R: 
                    union[nx][ny] = index
                    united.append([nx,ny])
                    queue.append([nx,ny])
                    summary += ground[nx][ny]
                    count += 1

        # print("united: ",united)

    for i,j in united:
        ground[i][j] = summary // count
    # for i in range(N):
    #     print(union[i])
    # print()
    # print()
    return 


result = 0
while True:
    union = [[-1]*N for _ in range(N)]
    index = 0
    for i in range(N):
        for j in range(N):
            if union[i][j] == -1:
                index += 1
                process(i,j, index)
                
    # print("index: ",index)
    if index == N*N:
        break
    result += 1
    

print(result)