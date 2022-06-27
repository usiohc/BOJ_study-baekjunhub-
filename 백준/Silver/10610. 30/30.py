n = sorted(list(map(int, input())), reverse=True)
tmp = sum(n)
if tmp % 3 != 0 or n[-1] != 0:
    print(-1)
else:
    print(''.join(map(str, n)))