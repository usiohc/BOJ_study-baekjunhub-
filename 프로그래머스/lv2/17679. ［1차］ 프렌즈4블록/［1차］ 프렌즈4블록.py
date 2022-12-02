def find(b):
    chk_b = set()
    for i in range(m-1):
        for j in range(n-1):
            if b[i][j] and b[i][j] == b[i][j+1] == b[i+1][j] == b[i+1][j+1]:
                chk_b.update({(i, j), (i+1, j), (i, j+1), (i+1, j+1)})
    return chk_b

def remove(chk_b, b):
    b = [list(r) for r in b]
    for ij in chk_b:
        i, j = ij
        b[i][j] = ''
    return b

def move(b):
    cnt = 0
    for i in range(m-1):
        for j in range(n):
            if b[i][j] and not b[i+1][j]:
                b[i][j], b[i+1][j] = b[i+1][j], b[i][j]
                cnt += 1
    return cnt, b

def solution(l_m, l_n, board):
    global m, n
    answer = 0
    m, n = l_m, l_n
    
    
    while True:
        chk_b = find(board)
        answer += len(chk_b)
        board = remove(chk_b, board)
        cnt = 1
        while cnt:
            cnt, board = move(board)
            
        if not cnt and not len(chk_b):
            break

    return answer