n, w, h = map(int, input().split())

wh = w**2 + h**2
for _ in range(n):
    case = int(input())
    if case**2 <= wh:
        print('DA')
    else:
        print('NE')