
from collections import Counter

def solution(A):
    resultList = [0 for i in range(len(A))]
    temp = []
    count = Counter(A)
    for i in range(len(A)):
        if count[A[i]] == 1:
            resultList[A[i]-1] = A[i]
            print(resultList)
        else:
            temp.append(A[i])
            print(temp)

solution([6,2,3,5,6,3])