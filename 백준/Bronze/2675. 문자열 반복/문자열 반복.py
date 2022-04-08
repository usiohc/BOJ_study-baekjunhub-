tc = int(input())

for _ in range(tc):
    t, s = input().split()
    for i in s:
        print(i * int(t), end='')
    print()