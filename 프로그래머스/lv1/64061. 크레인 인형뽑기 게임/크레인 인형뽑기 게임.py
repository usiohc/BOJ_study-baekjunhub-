def solution(board, moves):
    answer = 0
    dolls = []
    for i in moves:
        i-=1
        for j in range(len(board)):
            if board[j][i] > 0:
                dolls.append(board[j][i])
                board[j][i] = 0
                break
        
        if len(dolls) > 1:
            for j in range(1, len(dolls)):
                if dolls[j] == dolls[j-1]:
                    dolls.pop(j)
                    dolls.pop(j-1)
                    answer += 2
        
    return answer