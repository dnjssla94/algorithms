n, m = map(int,input().split())
array = []  # 화폐단위

for i in range(n):
    array.append(int(input()))

result = [10001]*(m+1)  #dp memory
result[0] = 0
for i in range(n):
    for j in range(array[i],m+1):
        if result[j-array[i]] != 1001:
            result[j] = min(result[j], result[j-array[i]]+1)

if result[m] == 10001:
    print(-1)
else:
    print(result[m])

 