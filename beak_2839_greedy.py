sugar = int(input())

a = sugar // 5
def solution(sugar):
    for i in range(a,-1,-1):
        remainSugar = sugar - (i * 5)
        if (remainSugar % 3) == 0:
            result = i + (remainSugar // 3)
            return result
    return -1

r = solution(sugar)
print(r)