import itertools
import sys

input = sys.stdin.readline
n = int(input())

min_result = 1e9

players = [i for i in range(n)]
combi = list(itertools.combinations(players, n//2))
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))

for i in range(len(combi)//2):
    tmps_start = list(itertools.combinations(combi[i], 2))
    tmps_link = list(itertools.combinations(combi[-(i+1)], 2))
    result_start = 0
    result_link = 0
    for tmp_start in tmps_start:
        result_start += nums[tmp_start[0]][tmp_start[1]] + nums[tmp_start[1]][tmp_start[0]]
    for tmp_link in tmps_link:
        result_link += nums[tmp_link[0]][tmp_link[1]] + nums[tmp_link[1]][tmp_link[0]]

    min_result = min(abs(result_start - result_link), min_result)

print(min_result)