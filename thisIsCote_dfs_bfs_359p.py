import sys
N = int(sys.stdin.readline())
datas = []
for i in range(N):
#    datas.append(list(map(str, input().split())))
    datas.append(sys.stdin.readline().split())

datas.sort(key=lambda x: (-int(x[1]),int(x[2]),(-int(x[3])),x[0]))
for data in datas:
    print(data[0])