def isok(s):
    if len(s) % 2 != 0 :
        return False
    stack = []
    for el in s:
        if el == "(" or el == "[" or el == "{":
            stack.append(el)
        else:
            if len(stack) == 0:
                return False
            else :
                a = stack.pop()
                case14 = a+el
                if case14 != "[]" and case14 != "()" and case14 != "{}":
                    return False
    if stack:
        return False
    else:
        return True
        
def solution(s):
    answer = 0
    
    for _ in range(len(s)):
        if isok(s):
            answer += 1
        s = s[1:]+s[0]
    
    return answer