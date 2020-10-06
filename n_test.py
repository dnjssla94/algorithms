# a = list(map(int, input().split()))

n = 7
p = [6,2,1,0,2,4,3]
c=  [3,6,6,2,3,7,6]

cencleCount = 0
mechul = 0
jeago = 0

def solution(n,p,c):
    global cencleCount
    global mechul
    global jeago
    answer = 0
    print(p)
    for i in range(n):
        if (p[i]+jeago) < c[i]:
            cencleCount += 1
            jeago = p[i] + jeago
            if cencleCount == 3:
                answer = mechul / (i+1)
                answer = '%.2f'% answer
                print(answer,"aaa")
                return answer
        elif (p[i]+jeago) >= c[i] and cencleCount == 0:
            mechul += (c[i]*100)
            jeago = (p[i]+jeago) - c[i]
            cencleCount = 0
        elif (p[i]+jeago) >= c[i] and cencleCount == 1:
            mechul += (c[i]*50)
            jeago = (p[i]+jeago) - c[i]
            cencleCount = 0
        elif (p[i]+jeago) >= c[i] and cencleCount == 2:
            mechul += (c[i]*25)
            jeago = (p[i]+jeago) - c[i]
            cencleCount = 0

    answer = mechul / n
    answer = '%.2f'% answer
    print(str(answer),"bbb")
    return answer
solution(n,p,c)

    





