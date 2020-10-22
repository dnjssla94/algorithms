
case = []
while True:
    test = list(map(int, input().split()))
    if test[0]==0 and test[1]==0 and test[2]==0: break
    case.append(test)
# print(case)
for i in range(len(case)):
    result = 0
    l = case[i][0]
    p = case[i][1]
    v = case[i][2]
    full = v // p
    # print('full: ',full)
    remain = v % p
    if remain <= l: result = (full*l)+remain
    else: result = (full+1) * l
    print('Case ',i+1,': ',result,sep='')


