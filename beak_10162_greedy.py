

def solution(time):
    if (time % 10) > 0:
        print(-1)
        return
    if (time // 300) > 0:
        aNum = time // 300
        time = time - (aNum * 300)
    else: aNum = 0
    if (time // 60) > 0:
        bNum = time // 60
        time = time - (bNum * 60)
    else: bNum = 0
    if (time // 10) > 0:
        cNum = time // 10
        time = time - (cNum * 10)
    else: cNum = 0
    print(aNum, bNum, cNum)
    return



time = int(input())

solution(time)