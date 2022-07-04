n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

def dfs(x, y):
    global cnt
    if x<=-1 or x>= n or y<=-1 or y>=n:
        return False

    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

    return False

result = []
for i in range(n):
    for j in range(n):
        cnt = 0
        if dfs(i, j):
           result.append(cnt)

result.sort()
print(len(result), *result, sep='\n')