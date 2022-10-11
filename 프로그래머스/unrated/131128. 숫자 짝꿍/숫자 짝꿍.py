def solution(X, Y):
    answer = ''
    dict_xy = {'X':{str(i):X.count(str(i)) for i in range(9,-1,-1)},
               'Y':{str(i):Y.count(str(i)) for i in range(9,-1,-1)}}
    for i in range(9,-1,-1):
        answer += str(i) * min(dict_xy['X'][str(i)], dict_xy['Y'][str(i)])
    
    if not answer:
        answer = '-1'
    elif answer[0] == '0':
        answer = '0'
    return answer