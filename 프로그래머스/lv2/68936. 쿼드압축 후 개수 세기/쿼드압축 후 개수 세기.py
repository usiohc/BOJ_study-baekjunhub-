def quard(x, y, n, arr):
    global answer
    chk = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != chk:
                n //= 2
                quard(x, y, n, arr)
                quard(x, y + n, n, arr)
                quard(x + n, y, n, arr)
                quard(x + n, y + n, n, arr)
                return

    answer[chk] += 1

    

def solution(arr):
    global answer
    answer = [0, 0]
    quard(0, 0, len(arr), arr)
    return answer