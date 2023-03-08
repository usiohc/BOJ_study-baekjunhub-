def solution(m, n, puddles):
    array = [[0] * (m+1) for _ in range(n+1)]
    for x, y in puddles:
        array[y][x] = -1
    array[1][1] = 1
    
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if array[i][j] == -1:
                array[i][j] = 0
            else:
                array[i][j] += (array[i-1][j] + array[i][j-1]) % 1000000007
                
    
    return array[-1][-1]