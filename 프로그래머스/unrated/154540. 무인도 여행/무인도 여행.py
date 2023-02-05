import sys
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    global result
    answer = []
    maps = [list(m) for m in maps]
    
    def dfs(x, y):
        global result
        maps[x][y] = 'X'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if  0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != "X":
                result += int(maps[nx][ny])
                dfs(nx, ny)
        

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if 0 <= i < len(maps) and 0 <= j < len(maps[0]) and maps[i][j] != "X":
                result = int(maps[i][j])
                dfs(i, j)
                if result:
                    answer.append(result)

    if answer:
        return sorted(answer)
    return [-1]