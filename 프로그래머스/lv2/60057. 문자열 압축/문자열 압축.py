def solution(s):
    answer = len(s)
    
    if answer == 1:
        return answer 
    
    for l in range(1, len(s)+1):
        lst = [s[i:i+l] for i in range(0, len(s), l)]
        dic = {sl:[1] for sl in set(lst)}
        leng = len(s)
        
        for i in range(len(lst)-1):
            if lst[i] == lst[i+1]:
                leng -= l
                dic[lst[i]][-1] += 1
            else:
                if dic[lst[i]][-1] > 1:
                    dic[lst[i]].append(1)
                    
        for v_lst in dic.values():
            for v in v_lst:
                if v > 1:
                    leng += len(str(v))
        answer = min(answer, leng)
        
    return answer