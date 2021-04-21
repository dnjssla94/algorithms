
data = input()

one = 0
zero = 0

for i in range(len(data)):
    if data[i] == '0':
        if i == 0:
            zero += 1
        else:
            if data[i-1] == '1':
                zero += 1
    else:
        if i == 0:
            one += 1
        else:
            if data[i-1] == '0':
                one += 1

print(min(one,zero))

            