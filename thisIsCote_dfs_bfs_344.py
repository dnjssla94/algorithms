
from collections import deque

N, K = map(int, input().split())
data = []  # v,x,y,s
plate = []
s = 0
for i in range(N):
    row = list(map(int, input().split()))
    plate.append(row)
    for j in range(N):
        if plate[i][j] != 0:
            data.append([plate[i][j], i, j, s])

S, X, Y = map(int, input().split())

data.sort()
queue = deque(data)
#print("queue:",queue)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

while queue:
    value,cor_x, cor_y, sec = queue.popleft()
    if sec >= S:
        break
    for i in range(4):
        x = cor_x + dx[i]
        y = cor_y + dy[i]
        if x >= 0 and x < N and y >= 0 and y < N:
            if plate[x][y] == 0:
                plate[x][y] = value
                queue.append([value, x,y,sec+1])
                


print(plate[X-1][Y-1])