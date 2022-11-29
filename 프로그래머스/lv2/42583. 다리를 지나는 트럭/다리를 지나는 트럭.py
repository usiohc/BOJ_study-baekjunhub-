def solution(b_l, w, t_ws):
    answer = 0
    
    b = [0 for _ in range(b_l)]
    b_s = 0
    while b:
        b_s -= b[0]
        answer += 1
        b.pop(0)
        if t_ws:
            if b_s + t_ws[0] <= w:
                b_s += t_ws[0]
                b.append(t_ws.pop(0))
            else:
                b.append(0)
                
    return answer