def isok(x):
    for i in range(x):
        if chess[x] == chess[i] or abs(chess[x] - chess[i]) == abs(x-i):
            return False
    return True

def chk_queen(x):
    global result
    if x == n:
        result += 1
        return
    else:
        for i in range(n):
            chess[x] = i
            if isok(x):
                chk_queen(x+1)

n = int(input())
chess = [0] * n
result = 0

chk_queen(0)
print(result)