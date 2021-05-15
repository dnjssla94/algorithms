
size = int(input())
data = []
for i in range(size):
    data.append(list(map(int, input().split())))


for i in range(1, size):
    for j in range(i+1):
        #왼쪽 위에서
        if j == 0:
            up_left = 0
        else:
            up_left = data[i-1][j-1]
        #오른쪽 위에서
        if j == i:
            up_right = 0
        else:
            up_right = data[i-1][j]
        data[i][j] = data[i][j]+max(up_left,up_right)

print(max(data[size-1]))







# result = 0

# def solution(depth, position, sum):
#     global result
#     if depth == 0:
#         sum += data[0][0]
#         solution(depth+1,position,sum)
#         solution(depth+1,position+1,sum)
#     elif depth == size-1:
#         sum += data[size-1][position]
#         if sum > result: result = sum
#         # break
#     else:
#         sum += data[depth][position]
#         solution(depth+1,position,sum)
#         solution(depth+1,position+1,sum)

# solution(0,0,0)
# print(result)
