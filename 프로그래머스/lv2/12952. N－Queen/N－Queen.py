

def solution(n):
    global answer
    
    answer = 0
    row = [0] * n
    
    def dfs(x):
        global answer
        
        if x == n:
            answer += 1
        else:
            for i in range(n):
                row[x] = i
                for i in range(x):
                    if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
                        break
                else:   
                    dfs(x+1)
                
    dfs(0)
    
    return answer