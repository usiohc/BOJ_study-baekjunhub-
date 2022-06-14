import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    vps = list(input().rstrip())

    if vps[0] == ')' or vps[-1] == '(':
        print('NO')
        continue

    count = 0
    for char in vps:
        if char == '(':
            count += 1
        if char == ')':
            count -= 1
        if count < 0:
            break

    if count == 0:
        print('YES')
    else:
        print('NO')