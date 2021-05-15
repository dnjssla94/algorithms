# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()

number = ['0','1','2','3','4','5','6','7','8','9']
text = []
data = {}

text_index=[]
for i in range(len(user_input)):
	if user_input[i] not in number:
		text_index.append(i)
index = 0

for i in text_index:	#문자 위치 인덱스
	index += 1
	if user_input[i] not in text:	#해당문자가 처음이라면
		text.append(user_input[i]) # 문자를 사용정보에 넣어주고
		if index == len(text_index): #따라오는 숫자 구하기
			temp = user_input[i+1:len(user_input)]
		else:
			temp = user_input[i+1:text_index[index]]
		data[user_input[i]] = int(temp)
		
	else: #해당 문자가 처음이 아니라면
		if index == len(text_index): #따라오는 숫자 구하기
			temp = user_input[i+1:len(user_input)]
		else:
			temp = user_input[i+1:text_index[index]]
		data[user_input[i]] += int(temp)

result = ''
for k, v in data.items():
	result += k
	result += str(v)
print(result)
