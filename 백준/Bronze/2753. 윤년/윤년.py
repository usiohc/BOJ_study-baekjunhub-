t = int(input())
print('1' if (t % 4 == 0 and not t % 100 == 0) or t % 400 == 0 else '0')