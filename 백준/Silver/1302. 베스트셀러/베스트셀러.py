import sys
input = sys.stdin.readline

n = int(input())
dic = {}
for _ in range(n):
    tmp = input().rstrip()
    if not tmp in dic:
        dic.setdefault(tmp, 1)
    else:
        dic[tmp] += 1

num = max(dic.values())
result = []
for k, v in dic.items():
    if v == num:
        result.append(k)
result.sort()
print(result[0])