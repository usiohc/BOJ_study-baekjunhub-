a, b = input().split()

if len(a) == len(b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            break
        if a[i] == '8':
            cnt += 1
    print(cnt)
else:
    print(0)