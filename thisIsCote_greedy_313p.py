memberNum = int(input())
member = list(map(int,input().split()))
result = 0
i = 0
member.sort()
# 방법 1:

# 방법 2:
result = 0
count = 0
for i in member:
    count += 1
    if count == i:
        result +=1
        count=0

print("방법1 결과: ",result)
