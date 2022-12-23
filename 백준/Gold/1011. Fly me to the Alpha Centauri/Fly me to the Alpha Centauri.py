import sys

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    n = y-x

    i, x, y = 1, 1, 1
    while n>x:
        x = x + y
        i += 1
        if i%2==0:
            y += 1

    print(i)