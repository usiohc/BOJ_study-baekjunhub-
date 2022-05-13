import sys

n = int(input())

nums = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    nums.append([y, x])
nums.sort()

for y, x in nums:
    print(x, y)