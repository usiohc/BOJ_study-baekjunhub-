import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    data.sort(key=lambda x: x[0])

    result = 1
    tmp = data[0][1]
    for i in range(1, len(data)):
        if tmp > data[i][1]:
            tmp = min(tmp, data[i][1])
            result += 1

    print(result)