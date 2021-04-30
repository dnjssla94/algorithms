from itertools import combinations

N = int(input())
data = []
teacher = []    #선생님 좌표
empty = []  #빈공간 좌표

for i in range(N):
    data.append(list(map(str, input().split())))
    for j in range(N):
        if data[i][j] == 'T': teacher.append([i,j])
        if data[i][j] == 'X': empty.append([i,j])

def watch(x,y,direction):#학생을 찾으면 T 못찾으면 F
    if direction == 0:
        while 0 <= x:  #상
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            x -= 1
        return False
    if direction == 1:
        while x < N: #하
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            x += 1
        return False
    if direction == 2:
        while 0 <= y:  #좌
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            y -= 1
        return False
    if direction == 3:
        while y < N: #우
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            y += 1
        return False


def process():
    for i,j in teacher:
        for d in range(4):
            temp = watch(i,j,d)  # 특정 선생님이 사방을 본다.
            if temp: return True    #학생을 발견하면 True
    return False

result = True
for target in combinations(empty,3): # 빈공간에 장애물 3개를 세우는 모든 경우에 대해서 검사

    for i,j in target:
        data[i][j] = 'O'
    
    result = process()   #현재 data에서 학생을 찾을수 있는지 검사
    if not result: break
    for i,j in target:
        data[i][j] = 'X'


if not result:
    print("YES")
else:
    print("NO")