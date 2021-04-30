N = 10
def watch(x,y):#학생을 찾으면 T 못찾으면 F
    while 0 <= x:  #상
        x -= 1
    print(x,y)
    while x < N: #하
        x += 1
    while 0 <= y:  #좌
        y -= 1
    while y < N: #우
        y += 1
watch(5,5)