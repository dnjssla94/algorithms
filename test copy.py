number = int(input())
data = []
dest = []
result = 0
for i in range(number):
	data.append(int(input()))
data.sort()

print(data)
del data[0]
del data[0]
print(data)