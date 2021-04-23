import sys
from collections import deque

numCount = int(sys.stdin.readline())
numberList = list(map(int, sys.stdin.readline().split()))
operatorList = list(map(int, sys.stdin.readline().split()))



minimum = 1e9
maximum = -1e9
def dfs(target_num, nowResult):
    global minimum, maximum

    if target_num == numCount-1: 
        minimum = min(minimum,nowResult)
        maximum = max(maximum,nowResult)
        # print(minimum, maximum)
        return 
    else:
        if operatorList[0] >= 1:
            operatorList[0] -= 1
            dfs(target_num+1, nowResult + numberList[target_num+1])
            operatorList[0] += 1
        if operatorList[1] >= 1:
            operatorList[1] -= 1
            dfs(target_num+1, nowResult - numberList[target_num+1])
            operatorList[1] += 1
        if operatorList[2] >= 1:
            operatorList[2] -= 1
            dfs(target_num+1, nowResult * numberList[target_num+1])
            operatorList[2] += 1
        if operatorList[3] >= 1:
            operatorList[3] -= 1
            dfs(target_num+1, int(nowResult / numberList[target_num+1]))
            operatorList[3] += 1

dfs(0,numberList[0])
print(maximum)
print(minimum)