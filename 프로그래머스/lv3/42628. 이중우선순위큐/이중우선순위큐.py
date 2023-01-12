def solution(operations):
    answer = [0, 0]
    
    que = []
    for o in operations:
        l, r = o.split()
        if l == 'I':
            que.append(int(r))
        elif l == 'D' and len(que) != 0:
            if r[0] == '-':
                que.remove(min(que))
            else:
                que.remove(max(que))
    
    return [max(que), min(que)] if que else [0, 0]