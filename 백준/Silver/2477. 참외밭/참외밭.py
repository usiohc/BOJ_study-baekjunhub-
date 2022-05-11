k = int(input())
case_list = []
for _ in range(6):
    __, case = map(int, input().split())
    case_list.append(case)

square = 0
blank = 0
idx = 0
for i in range(6):
    temp = case_list[i] * case_list[(i+1) % 6]
    if square < temp:
        square = temp
        idx = i

blank = case_list[(idx+3) % 6] * case_list[(idx + 4) % 6]
print( k * (square - blank))