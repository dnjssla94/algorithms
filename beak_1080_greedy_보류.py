row, calumn = map(int, input().split())
originMatrix = []
targetMatrix = []

for i in range(row):
    rows = input()
    originMatrix.append([])
    for j in range(calumn):
        originMatrix[i].append(int(rows[j]))
for i in range(row):
    rows = input()
    targetMatrix.append([])
    for j in range(calumn):
        targetMatrix[i].append(int(rows[j]))

