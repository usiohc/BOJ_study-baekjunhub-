import itertools

a, b = map(int, input().split())
a = [i for i in range(1,a+1)]
# b = [i for i in range(1,b+1)]
result = list(itertools.product(a, repeat=b))

for nums in result:
    print(*nums)