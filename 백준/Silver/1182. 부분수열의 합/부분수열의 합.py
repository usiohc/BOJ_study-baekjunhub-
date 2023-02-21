from itertools import combinations
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, n+1):
    comb = combinations(arr, i)

    for c in comb:
        if sum(c) == s:
            cnt += 1

print(cnt)