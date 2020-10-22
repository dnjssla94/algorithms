
graph = dict()
visited_queue = list()
countName = 1
board = [[0,0,0,0,0,0,0,0,0]]

for i in range(7):
    temp = [0]
    temp.extend(list(map(int,input().split())))
    temp.append(0)
    board.append(temp)
board.append([0,0,0,0,0,0,0,0,0])
# for i in range(9):
#     print(board[i])

for i in range(1,8):
    for j in range(1,8):
        graph[countName] = [board[i][j], board[i-1][j],board[i+1][j],board[i][j-1],board[i][j+1],False]
        countName += 1

# print(graph[15])
def solution(n):
    if graph[n][5] == True: return 0
    visited_queue.append(n)
    graph[n][5] = True
    if graph[n][0] == graph[n][1] and graph[n-7][5] == False:
        return solution(n-7)
    elif graph[n][0] == graph[n][2] and graph[n+7][5] == False:
        return solution(n+7)
    elif graph[n][0] == graph[n][3] and graph[n-1][5] == False:
        return solution(n-1)
    elif graph[n][0] == graph[n][4] and graph[n+1][5] == False:
        return solution(n+1)
    else:
        return len(visited_queue)

count = 0
for i in range(1, 50):
    result = solution(i)
    #print(i,'번째: ', visited_queue)

    if result >= 3:
        count += 1
    else: 
        for j in range(len(visited_queue)):
            graph[visited_queue[j]][5] = False
            # print(i,'번째: ', graph[visited_queue[j]][5])
        
    visited_queue = []
print(count)


# 입력예시:
# 4 4 4 4 1 4 3 
# 4 4 4 4 3 2 4 
# 4 4 4 4 5 5 4 
# 4 4 4 4 2 1 3 
# 5 5 3 2 4 4 4 
# 2 1 1 3 4 4 4 
# 5 4 5 5 4 4 4 
# 답: 2

# 2 1 5 1 1 3 4
# 2 1 5 1 3 5 3
# 2 3 4 5 2 2 4
# 4 4 3 2 3 1 3
# 4 3 5 3 1 4 3
# 5 4 4 3 3 5 5
# 2 1 3 5 1 1 2
# 답: 4

# 1 1 1 1 1 1 1 
# 2 2 2 2 1 2 2 
# 3 3 3 3 1 3 3 
# 4 5 3 4 1 4 3 
# 4 5 3 4 4 4 2 
# 4 5 3 4 1 4 3 
# 1 1 1 1 1 1 1 
# 답: 8