def solution(dartResult):
    char_result = []
    char_dart = []
    
    for i in range(len(dartResult)):
        if dartResult[i].isnumeric():
            if dartResult[i] == '0' and dartResult[i-1] == '1':
                char_dart[0] = '10'
                continue
            char_result.append(char_dart)
            char_dart = []
        char_dart.append(dartResult[i])
    else:
        char_result.append(char_dart)
    # print(char_result)
    
    scores = {'S': 1, 'D': 2, 'T': 3}
    score_result = [0]    
    for i in range(1, len(char_result)):
        answer = int(char_result[i][0]) ** scores[char_result[i][1]]
        score_result.append(answer)
        if char_result[i][-1] == '*':
            score_result[i-1] *= 2
            score_result[i] *= 2
        elif char_result[i][-1] == '#':
            score_result[i] *= -1
        # print(score_result)
    return sum(score_result)