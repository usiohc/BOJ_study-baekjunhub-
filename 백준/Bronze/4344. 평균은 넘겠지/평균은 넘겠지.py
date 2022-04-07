tc = int(input())

for i in range(tc):
    tclist = list(map(int, input().split()))

    avg = sum(tclist[1:]) / tclist[0]
    result = 0
    for j in tclist[1:]:
        if j > avg: result += 1

    f_result = round(result / tclist[0] * 100, 3)
    print(f'{f_result:.3f}%')