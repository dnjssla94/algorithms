test = int(input())
case = list()

for i in range(test):
    candidate = int(input())
    case.append([])
    for j in range(candidate):
        case[i].append(list(map(int, input().split())))


def solution(testCase): 
    
    sotedDocument = sorted(testCase,key=lambda parameter_list: parameter_list[0])
    meetingGrade = sotedDocument[0][1]
    maxPerson = 1
    for i in range(1,len(sotedDocument)):
        if sotedDocument[i][1] < meetingGrade:
            meetingGrade = sotedDocument[i][1]
            maxPerson += 1
    print(maxPerson)

for i in range(test):
    solution(case[i])