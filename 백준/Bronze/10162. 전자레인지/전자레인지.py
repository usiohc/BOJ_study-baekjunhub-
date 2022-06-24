cooking = int(input())
times = [300, 60, 10]
result = [0, 0, 0]
if cooking % 10 != 0:
    print(-1)
else:
    for i in range(3):
        result[i] = cooking // times[i]
        cooking %= times[i]
    print(*result)