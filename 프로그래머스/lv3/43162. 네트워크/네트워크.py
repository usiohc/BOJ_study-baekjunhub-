def dfs(x):
    visited[x] = True
    for i in range(n):
        if n != i and not visited[i]:
            if array[x][i] == 1:
                visited[i] = True
                dfs(i)            
        
def solution(num, computers):
    global array, visited, n
    answer = 0
    n, array = num, computers

    visited = [False]*n
    for i in range(n):
        print(visited)
        if not visited[i]:
            dfs(i)
            answer += 1
            
    return answer