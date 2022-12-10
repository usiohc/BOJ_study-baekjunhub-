def solution(s):
    str_lst = {}
    num_lst = []
    
    for i in range(len(s)):
        if s[i] in str_lst.keys():
            num_lst.append(i-str_lst[s[i]])
            str_lst[s[i]] = i
        else:
            num_lst.append(-1)
            str_lst[s[i]] = i
    return num_lst