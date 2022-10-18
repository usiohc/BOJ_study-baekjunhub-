def solution(s):
    if len(s) == 2 and s[0] == s[1]:
        return 1
    if len(s) % 2 == 1:
        return 0
    
    stack = [s[0]]
    
    for v in s[1:]:
        if len(stack) > 0 and stack[-1] == v:
            stack.pop()
        else:
            stack.append(v)
            
    return 0 if stack else 1