

# monkeyNum = int(input())
# rltShip = list()

# for i in range(monkeyNum):
#     hateNum = list(input().split())
#     hateNum = hateNum[1:]
#     hateNum = list(map(int, hateNum))
#     rltShip.append(hateNum)
import sys
from collections import Counter

monkeyNum = int(sys.stdin.readline() )
rltShip = list()

for i in range(monkeyNum):
    hateNum = list(map(int,sys.stdin.readline().split()))
    hateNum = hateNum[1:]
    hateNum = list(map(int, hateNum))
    rltShip.append(hateNum)

# print(rltShip)0
cage1 = list()
cage2 = list()

cage1_sub = list()
cage2_sub = list()

notYet = list()

for i in range(monkeyNum):
    if i+1 not in cage1_sub:
        cage1.append(i+1)
        cage1_sub.extend(rltShip[i])    
    elif i+1 not in cage1_sub:
        cage2.append(i+1)
        cage2_sub.extend(rltShip[i])
    else:
        notYet.append(i+1)
for i in notYet:
    if Counter(cage1_sub)[i] < 2 :
        cage1.append(i)
        cage1_sub.extend(rltShip[i-1]) 
    else:
        cage2.append(i)
        cage2_sub.extend(rltShip[i-1]) 
# print("cage1: ", cage1)
# print(cage1_sub)
# print("cage2: ", cage2)
# print(cage2_sub)
cage1.sort()
cage2.sort()
print(len(cage1), end=' ')
for i in cage1:
    print(i, end=' ')
print()
print(len(cage2), end=' ')
for i in cage2:
    print(i, end=' ')
print()

# 6
# 1 2
# 1 1
# 0
# 1 5
# 2 4 6
# 1 5