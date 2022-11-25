def solution(record):
    answer = []
    users = {}
    chk_name = []
    
    for r in record:
        r = list(r.split())
        
        if r[0] in ('Enter', 'Change'):
            users[r[1]] = r[2]
        chk_name.append([r[0], r[1]])
    
    for cn in chk_name:
        if cn[0] == 'Enter':
            answer.append(f'{users[cn[1]]}님이 들어왔습니다.')
        elif cn[0] == 'Leave':
            answer.append(f'{users[cn[1]]}님이 나갔습니다.')
            
    return answer