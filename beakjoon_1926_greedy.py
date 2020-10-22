
testCase = []
testNum = int(input())
for i in range(testNum):
    testCase.append([])
    candiNum = int(input())
    for j in range(candiNum):
        testCase[i].append(list(map(int, input().split())))

# print(testCase)

for i in range(testNum):
    count = 1
    sortedCase = sorted(testCase[i], key=lambda parameter_list: parameter_list[0])
    # print('sortedCase: ',sortedCase)
    for j in range(1, len(sortedCase)):
        if sortedCase[j][1] < sortedCase[j-1][1]:
            # print( '카운트됨:',sortedCase[j])
            count += 1
    print(count)
