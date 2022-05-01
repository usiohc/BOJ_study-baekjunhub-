import sys

n, m = map(int, input().split())
chess_list = []
count_list = []
for _ in range(n):
    temp_list = []
    temps = sys.stdin.readline().rstrip()
    for o in range(m):
        temp_list.append(temps[o])
    chess_list.append(temp_list)
# print(chess_list)


def isok(i, j):
    count_W = 0
    count_B = 0
    for x in range(i, i+8):
        for y in range(j, j+8):
            if (x-i+y-j) % 2 == 0:
                if chess_list[x][y] != 'W':
                    count_W += 1
            else:
                if chess_list[x][y] != 'B':
                    count_W += 1
    for x in range(i, i+8):
        for y in range(j, j+8):
            if (x-i+y-j) % 2 == 0:
                if chess_list[x][y] != 'B':
                    count_B += 1
            else:
                if chess_list[x][y] != 'W':
                    count_B += 1
    return count_B if count_W > count_B else count_W

for i in range(n-7):
    for j in range(m-7):
        count_list.append(isok(i, j))

print(min(count_list))