from collections import deque
import sys

N,M,K,X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
distances = [-1]*(N+1)

for i in range(M):
    a,b=map(int, sys.stdin.readline().split())
    graph[a].append(b)

queue = deque([X])
distances[X] = 0

while queue:
    city = queue.popleft()
    # queue.extend(graph[city])
    for next_city in graph[city]:
        if distances[next_city] == -1: 
            distances[next_city] = distances[city]+1
            queue.append(next_city)

flag = False
for i in range(len(distances)):
    if distances[i] == K:
        print(i)
        flag = True

if flag == False:
    print(-1)


