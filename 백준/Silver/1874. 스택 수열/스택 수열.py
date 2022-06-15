import sys
input = sys.stdin.readline

n = int(input())
stack = []
opr = []
count = 1
tmp = True
for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        opr.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        opr.append('-')
    else:
        tmp = False
if tmp == False:
    print('NO')
else:
    for i in opr:
        print(i)