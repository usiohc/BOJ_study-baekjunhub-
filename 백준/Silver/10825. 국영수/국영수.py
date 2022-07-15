import sys
input = sys.stdin.readline

n = int(input())

array = []
for _ in range(n):
    tmp = input().split()
    array.append((int(tmp[1]), int(tmp[2]), int(tmp[3]), tmp[0]))

array.sort(key=lambda x:(-x[0], x[1], -x[2], x[3]))

for v in array:
    print(v[3])