import sys

n, m = map(int, input().split())

s = []
for i in range(n):
    s.append(sys.stdin.readline())
s_check = []
for i in range(m):
    s_check.append(sys.stdin.readline())

count = 0
for i in s_check:
    if i in s:
        count += 1
print(count)