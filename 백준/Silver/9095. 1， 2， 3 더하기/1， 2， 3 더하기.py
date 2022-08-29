def add(x):
    if x == 1:
        return 1
    elif x==2:
        return 2
    elif x==3:
        return 4
    else:
        return add(x-1) + add(x-2) + add(x-3)

t = int(input())
for _ in range(t):
    print(add(int(input())))