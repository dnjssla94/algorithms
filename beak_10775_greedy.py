import sys

gateNum = int(sys.stdin.readline())
planeNum = int(sys.stdin.readline())
giList = list()
airPort = list()

for i in range(planeNum):
    a = int(sys.stdin.readline())
    giList.append(a)

for i in range(gateNum):
    airPort.append([])

# def solution():
#     maxPlane = 0
#     for i in range(len(giList)):
#         target = giList[i]
#         for j in range(target-1,-1,-1):
#             if airPort[j] == []: 
#                 airPort[j].append(1)
#                 maxPlane += 1
#                 break
#             if j==0 and airPort[j] != []: return maxPlane
#     return maxPlane

# result = solution()
# print(result)
def parent_find(x):
    if x == parent[x]:
        return x
    p = parent_find(parent[x])
    parent[x] = p
    return parent[x]
def union(x,y):
    x = parent_find(x)
    y = parent_find(y)
    parent[x] = y


parent = {i:i for i in range(gateNum+1)}
maxPlane = 0
for i in giList:
    x = parent_find(i)
    if x == 0: break
    union(x,x-1)
    print('parent',parent)
    maxPlane += 1
print(maxPlane)

#https://m.post.naver.com/viewer/postView.nhn?volumeNo=26835018&memberNo=33264526