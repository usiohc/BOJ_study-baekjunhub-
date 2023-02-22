def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)//2+1):
        ss = s[:i]
        cnt = 1
        zip_str = ''
        for j in range(i, len(s)+i, i):
            if ss == s[j:j+i]:
                cnt += 1
            else:
                if cnt > 1:
                    zip_str += str(cnt)+ss
                else:
                    zip_str += ss
                    
                ss = s[j:j+i]
                cnt = 1

        answer = min(answer, len(zip_str))
            
    return answer