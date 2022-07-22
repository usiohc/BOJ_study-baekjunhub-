import heapq
import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))
for i in range(n-1):
    for j in sorted(tuple(map(int, input().split()))):
        if nums[0] < j:
            heapq.heappop(nums)
            heapq.heappush(nums, j)

print(nums[0])