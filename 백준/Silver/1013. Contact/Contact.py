import re

t = int(input())
for _ in range(t):
    a = input()
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(a)
    if m:
        print("YES")
    else:
        print("NO")