
topingNum = int(input())
douPrice, topingPrice = input().split()
douPrice = int(douPrice)
topingPrice = int(topingPrice)
douCal = int(input())
topingCal = list()
calPerDollor = list()

for i in range(topingNum):
    topingCal.append(int(input())) 

sorted_topingCal = sorted(topingCal, reverse=True)
# print(sorted_topingCal)

for i in range(topingNum + 1):
    topingCalSum = 0
    for j in range(i):
        topingCalSum += sorted_topingCal[j]
    calPerDollor.append((douCal+topingCalSum)/(douPrice+topingPrice*i))

sorted_calPerDollor = sorted(calPerDollor)

# print(sorted_calPerDollor)
print(int(sorted_calPerDollor[-1]))

