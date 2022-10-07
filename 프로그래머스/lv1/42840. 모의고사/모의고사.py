def solution(answers):
    answer = [0,0,0]
    cnt = len(answers)
    users = [[1,2,3,4,5] * (cnt//5 +1)
            ,[2,1,2,3,2,4,2,5] * (cnt//8 +1)
            ,[3,3,1,1,2,2,4,4,5,5] * (cnt//10 +1)]

    for i in range(cnt):
        if answers[i] == users[0][i]:
            answer[0] += 1
        if answers[i] == users[1][i]:
            answer[1] += 1
        if answers[i] == users[2][i]:
            answer[2] += 1

    result = []
    for i in range(3):
        if answer[i] == max(answer):
            result.append(i+1)
    
    return result