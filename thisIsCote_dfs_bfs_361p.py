

def calFailure(N, stages, target):
    tryPlayer = 0
    failPlayer = 0
    for i in range(len(stages)):
        if stages[i] >= target:
            tryPlayer += 1
        if stages[i] == target:
            failPlayer += 1
    if tryPlayer == 0:
        return 0
    else:    
        return failPlayer/tryPlayer
    

def solution(N, stages):
    answer = []
    data = []
    for i in range(1,N+1):
        failRate = calFailure(N,stages, i)
        data.append([failRate,i])
    data.sort(key=lambda x: (-x[0],x[1]))
    for i in range(N):
        answer.append(data[i][1])
    return answer


# def solution(N, stages):
#     answer = []
#     data = []
#     stageLength = len(stages)
#     for i in range(1,N+1):
#         tryPlayer = 0
#         failPlayer = 0
#         failRate=0
#         for j in range(stageLength):
#             if stages[j] >= i:
#                 tryPlayer += 1
#             if stages[j] == i:
#                 failPlayer += 1
#         if tryPlayer == 0: 
#             failRate = 0
#         else: 
#             failRate =  failPlayer/tryPlayer
#         data.append([failRate,i])
#     data.sort(key=lambda x: -x[0])
#     for i in data:
#         answer.append(i[1])
#     # answer = [i[1] for i in data]
#     return answer