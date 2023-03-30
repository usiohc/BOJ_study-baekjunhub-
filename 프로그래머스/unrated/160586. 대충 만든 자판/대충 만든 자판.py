def solution(keymap, targets):
    answer = []
    
    keys = {}
    for k in keymap:
        for i in range(len(k)):
            if k[i] in keys:
                keys[k[i]] = min(keys[k[i]], i+1)
            else:
                keys[k[i]] = i+1
    
    
    for target in targets:
        answer.append(0)
        for t in target:
            if t not in keys:
                answer[-1] = -1
                break
            answer[-1] += keys[t]
            
    return answer