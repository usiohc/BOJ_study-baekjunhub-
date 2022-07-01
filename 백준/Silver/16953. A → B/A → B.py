a, b = map(int, input().split())
cnt = 0

def x2():
    global b, cnt
    b //= 2
    cnt += 1


def add1():
    global b, cnt
    b = int(str(b)[:-1])
    cnt += 1


while True:
    if b%2 == 0:
        x2()
    elif str(b)[-1] == '1':
        add1()
    else:
        break

    if a>=b:
        break

if a==b:
    print(cnt + 1)
else:
    print(-1)