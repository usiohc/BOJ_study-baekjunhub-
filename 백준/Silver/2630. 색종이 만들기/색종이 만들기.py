import sys
input = sys.stdin.readline


def div_four(x, y, n):
    global zero, one
    divided = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if divided != paper[i][j]:
                div_four(x, y, n//2)
                div_four(x, y+n//2, n//2)
                div_four(x+n//2, y, n//2)
                div_four(x+n//2, y+n//2, n//2)
                return

    if divided == 0:
        zero += 1
        return
    else:
        one += 1
        return

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
zero = 0
one = 0

div_four(0, 0, n)
print(zero)
print(one)