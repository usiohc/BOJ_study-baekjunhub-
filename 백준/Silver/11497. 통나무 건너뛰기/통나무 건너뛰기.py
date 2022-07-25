import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    nums = [int(i) for i in input().split()]
    nums.sort(reverse=True)
    result = 0
    for i in range(n-2):
        result = max(result, nums[i] - nums[i+2])
    print(result)