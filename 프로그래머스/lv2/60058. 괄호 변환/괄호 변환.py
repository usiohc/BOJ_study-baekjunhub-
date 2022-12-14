def solution(p):
    if not p:
        return ""

    u,v = seperate(p)
    if is_ok(u):
        return u + solution(v)
    else:
        answer = '('+solution(v)+')'

        for i in u[1:-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer

def seperate(p):
    l = 0
    r = 0
    for idx, i in enumerate(p):
        if i == '(':
            l += 1
        elif i == ')':
            r += 1
        if l == r:
            return p[:idx + 1], p[idx + 1:]

def is_ok(u):
    stack = []

    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True