N, x = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = len(data)
for i in range(N):
    if data[i] == x:
        start = i
        break
for i in range(start,N):
    if start == 0:break
    elif data[i] != x:
        end = i
        break
    
if start == 0: 
    print(-1)
else:
    print(end-start)