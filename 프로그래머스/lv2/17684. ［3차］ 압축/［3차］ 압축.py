def solution(msg):
    global dic, answer
    answer = []
    dic = {chr(i+64):i for i in range(1, 27)}
    
    i, j = 0, 1
    while j < len(msg)+1:
        if msg[i:j] in dic.keys():
            j += 1
        else:
            answer.append(dic[msg[i:j-1]])
            dic[msg[i:j]] = max(dic.values()) + 1
            i = j-1
    answer.append(dic[msg[i:j+1]]) 
    return answer