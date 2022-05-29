import sys

input = sys.stdin.readline
n = int(input())

times = [list(map(int, input().split())) for _ in range(n)]
times.sort(key = lambda x: (x[1], x[0]))

temp = times[0][1]
count = 1
for j in range(1, n):
    if times[j][0] >= temp:
        count += 1
        temp = times[j][1]

print(count)
