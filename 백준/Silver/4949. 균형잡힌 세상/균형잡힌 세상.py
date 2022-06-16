import sys
input = sys.stdin.readline

while True:
    chars = list(input().rstrip())
    if len(chars) == 1 and chars[0] == '.':
        break

    stack = []
    flag = True

    for char in chars:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] == '[':
                flag = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif char == ']':
            if not stack or stack[-1] == '(':
                flag = False
                break
            elif stack[-1] == '[':
                stack.pop()

    if flag == True and not stack:
        print('yes')
    else:
        print('no')