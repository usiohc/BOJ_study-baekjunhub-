import sys

t = int(input())
tlist = []

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    tlist.append(a+b)

for i in tlist:
    print(i)
