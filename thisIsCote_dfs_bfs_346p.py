
def checkBalance(target):
    rCnt = 0
    lCnt = 0
    for i in range(len(target)):
        if target[i] == '(': rCnt += 1
        else: lCnt += 1
    if rCnt == lCnt: return True
    else: return False

def checkRight(target):
    tool = 0
    if checkBalance(target) == True:
        for i in range(len(target)):
            if target[i] == '(': tool += 1
            else: tool -= 1
            if tool < 0: return False
        return True
    else: return False

def stepTwo(target): # 문자열을 조건에 맞춘 두개의 균형잡힌 문자열 u,v로 반환한다.
    rCnt = 0
    lCnt = 0
    u = ''
    v = ''
    for i in range(len(target)):
        if target[i] == '(': rCnt += 1
        else: lCnt += 1
        if rCnt == lCnt: 
            u = target[:i+1]
            v = target[i+4:]
            break
    print('u2:',u)
    print('v2:',v)
    return [u,v]
    
def solution(p):
    answer = ''
    if p == '': return ''
    else:
        u,v = stepTwo(p)
        if checkRight(u) == True:
            print('u:',u)
            print('v:',v)
            answer += u
            answer += solution(v)
            return answer
        else:
            answer = '(' + solution(v) + ')'
            u = u[1:len(u)-1]
            for i in range(len(u)):
                if u[i]=='(': answer += ')'
                else: answer += '('
            return answer
        

test = input()
ans = solution(test)
print(ans)
 