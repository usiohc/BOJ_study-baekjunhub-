import sys
input = sys.stdin.readline

n, k = map(int, input().split())
countrys = [tuple(map(int, input().split())) for _ in range(n)]
countrys.sort(key=lambda x: (-x[1], -x[2], -x[3]))

idx = 0
for i in range(len(countrys)):
    if countrys[i][0] == k:
        idx = i

for i in range(n):
    if countrys[idx][1:] == countrys[i][1:]:
        print(i+1)
        break