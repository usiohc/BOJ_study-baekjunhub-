import sys
input = sys.stdin.readline

n = int(input())
ks = sorted([int(input()) for _ in range(n)], reverse=True)

kgs = []
for i in range(n):
    kgs.append(ks[i]*(i+1))

print(max(kgs))