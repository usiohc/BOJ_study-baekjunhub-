import sys

lst = [int(sys.stdin.readline()) for _ in range(int(input()))]
lst.sort()
result = 0
rank = 1
for el in lst:
	result += abs(el-rank)
	rank += 1

print(result)