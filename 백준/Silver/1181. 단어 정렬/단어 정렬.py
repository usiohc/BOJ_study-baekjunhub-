import sys

n = int(input())

strs = []
for _ in range(n):
    strs.append(sys.stdin.readline())

strs = list(set(strs))
strs.sort()
strs = sorted(strs, key=lambda x : len(x))

print(''.join(strs), end='')