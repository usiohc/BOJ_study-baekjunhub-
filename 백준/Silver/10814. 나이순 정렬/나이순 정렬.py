import sys

n = int(input())

n_list = []
for i in range(n):
    temp = sys.stdin.readline().rstrip().split()
    n_list.append(temp)

n_list = sorted(n_list, key= lambda x: int(x[0]))

for i in n_list:
    print(i[0], i[1])