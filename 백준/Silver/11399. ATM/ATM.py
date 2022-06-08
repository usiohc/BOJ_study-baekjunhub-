import itertools

n = int(input())
times = sorted(list(map(int, input().split())))

print(sum(list(itertools.accumulate(times))))