from copy import deepcopy

n = int(input())
Anums = list(map(int, input().split()))
sort_Anums = deepcopy(sorted(Anums))
Pnums = [0]*n
for i in range(n):
    tmp = Anums.index(sort_Anums[i])
    Anums[tmp] = -1
    Pnums[tmp] = i

print(*Pnums)