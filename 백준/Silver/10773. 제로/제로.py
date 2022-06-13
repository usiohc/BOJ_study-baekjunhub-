import sys
input = sys.stdin.readline

k = int(input())
result = []
for _ in range(k):
    tmp = int(input())
    if tmp != 0:
        result.append(tmp)
    else:
        result.pop()
print(sum(result))