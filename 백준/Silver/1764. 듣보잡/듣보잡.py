import sys
from collections import Counter

n, m = map(int, input().split())
n_list = []
for i in range(n):
    n_list.append(sys.stdin.readline().rstrip())

n_list = Counter(n_list)
count = 0
result = []
for i in range(m):
    temp = sys.stdin.readline().rstrip()
    if temp in n_list:
        count += 1
        result.append(temp)

result.sort()
print(count)
print(*result, sep='\n')