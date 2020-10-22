
network = dict()

computer = int(input())
edge = int(input())

for i in range(computer):
    network[i+1] = []


for i in range(edge):
    com1, com2 = map(int,input().split())
    network[com1].append(com2)
    network[com2].append(com1)
# print(network)

visit = []
need_visit = []
visit.append(1)
need_visit.extend(network[1])
while need_visit:
    temp = need_visit.pop()
    if temp not in visit:
        visit.append(temp)
        need_visit.extend(network[temp])
# print('visit: ', visit)
result = len(visit) - 1
print(result)

# 7
# 6
# 4 5
# 6 4
# 7 2
# 3 5
# 3 1
# 1 5
