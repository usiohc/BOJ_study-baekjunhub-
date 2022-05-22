import itertools

n, m = map(int, input().split())
n = [i for i in range(1,n+1)]

if m == 1:
    print(*n, sep='\n')
else:
    result = list(itertools.permutations(n, m))
    for nums in result:
        print(*nums)