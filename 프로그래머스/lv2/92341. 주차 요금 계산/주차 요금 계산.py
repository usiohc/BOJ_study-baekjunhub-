import math

def solution(fees, records):
    answer = []
    dic = {}
    last_time = 23 * 60 + 59
    
    for i in records:
        time, car, history = i.split(' ')
        h, m = time.split(':')
        time = int(h) * 60 + int(m)
        
        if history == 'IN':
            if car not in dic:
                dic[car] = [time, 0]
            else:
                dic[car] = [time, dic[car][1]]
        else:
            dic[car] = [-1, dic[car][1] + time - dic[car][0]]
            
    cars = sorted(dic.keys())
    for i in cars:
        mm = dic[i][1]
        if dic[i][0] >= 0:
            mm = mm + last_time - dic[i][0]
        
        answer.append(fees[1] + math.ceil(max(0, mm - fees[0]) / fees[2]) * fees[3])
    return answer
