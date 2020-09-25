
change = int(input())

omanwon = 0
manwon = 0
ochunwon = 0
chunwon = 0
obeak = 0
beak = 0
oship = 0
ship = 0

while change >= 50000:
    change -= 50000
    omanwon +=1

while change >= 10000:
    change -= 10000
    manwon +=1

while change >= 5000:
    change -= 5000
    ochunwon +=1

while change >= 1000:
    change -= 1000
    chunwon +=1

while change >= 500:
    change -= 500
    obeak +=1

while change >= 100:
    change -= 100
    beak +=1

while change >= 50:
    change -= 50
    oship +=1

while change >= 10:
    change -= 10
    ship +=1

count = omanwon + manwon +ochunwon+chunwon+obeak+beak+oship+ship
print(count)

print("omanwon: ", omanwon)
print("manwon: ", manwon)
print("ochunwon: ", ochunwon)
print("chunwon: ", chunwon)
print("obeak: ", obeak)
print("obeak: ", beak)
print("oship: ", oship)
print("ship: ", ship)
