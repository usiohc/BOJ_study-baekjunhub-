def solution(name, yearning, photo):
    answer = []
    
    ny_dic = {n:y for n, y in zip(name, yearning)}
    
    for p in photo:
        cnt = 0
        for el in p:
            if el in ny_dic:
                cnt += ny_dic[el]
        answer.append(cnt)
        
    
    return answer