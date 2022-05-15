import sys

n = int(input())

Xs = list(map(int, sys.stdin.readline().split()))
Xs_sort = sorted(list(set(Xs)))
temp = []

Xs_dic = {Xs_sort[i]: i for i in range(len(Xs_sort))}

for i in Xs:
    print(Xs_dic[i], end=' ')