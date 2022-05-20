import math
import sys

n = int(input())

nums = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
nums.sort()

nums_rec = []

for i in range(1, n):
    nums_rec.append(nums[i]-nums[i-1])

gcd = nums_rec[0]
for i in range(1, len(nums_rec)):
    gcd = math.gcd(gcd, nums_rec[i])

result = []

for i in range(2, int(gcd**0.5) + 1):
    if gcd %i == 0:
        result.append(i)
        result.append(gcd//i)
result.append(gcd)
print(*sorted(set(list(result))))