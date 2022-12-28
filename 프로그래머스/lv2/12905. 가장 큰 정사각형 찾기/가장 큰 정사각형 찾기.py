def solution(board):
    answer = 0

    row = len(board)
    col = len(board[0])
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i][j-1], board[i-1][j]) +1

    for i in range(row):
        answer = max(answer, max(board[i]))
    
    return answer**2