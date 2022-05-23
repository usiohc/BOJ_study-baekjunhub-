import itertools

a, b = map(int, input().split())
a = [i for i in range(1,a+1)]
result = list(itertools.combinations_with_replacement(a, b))

for nums in result:
    print(*nums)