def solution(plans):
    answer = []
    stack = []
    
    dic_plans = {}
    times = {}
    for p in plans:
        h, m = map(int, p[1].split(':'))
        dic_plans[p[0]] = [h*60 + m, int(p[2])]
        times[h*60 + m] = p[0]

    now = min(times.keys())
    while len(answer) < len(plans):
        if stack:
            dic_plans[stack[-1]][1] -= 1
            if dic_plans[stack[-1]][1] == 0:
                answer.append(stack.pop())
        
        if now in times.keys():
            stack.append(times[now])
        
        now += 1
    
    
    # print(stack)
    # print(answer)
    return answer