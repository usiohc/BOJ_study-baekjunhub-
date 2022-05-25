import itertools
import sys

input = sys.stdin.readline

_, m = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))
sum_list = [0]
sum_list += list(itertools.accumulate(nums))

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    print(sum_list[b]-sum_list[a-1])