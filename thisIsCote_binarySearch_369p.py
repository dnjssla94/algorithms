N, C = map(int, input().split())
data = []
for i in range(N):
    data.append(int(input()))
data.sort()

houses = [0 for i in range(data[-1]+1)]

for i in range(N):
    houses[data[i]] = 1
print(houses)