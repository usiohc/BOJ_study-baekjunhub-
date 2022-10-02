def solution(s, n):
    answer = ''
    array = list(s) 
    for x in array:
        if x.isspace():
            answer += x
            continue

        num = ord(x) + n
        if x.isupper():
            if num > 90:
                num -= 26
        else:
            if num > 122:
                num -= 26
        answer += chr(num)
        
    return answer