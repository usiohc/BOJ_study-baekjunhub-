n, m = map(int, input().split())
array = [[0]*(m+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

for i in range(1, n+1):
    for j in range(1, m+1):
        array[i][j] += max(array[i][j-1], array[i-1][j], array[i-1][j-1])

print(array[n][m])