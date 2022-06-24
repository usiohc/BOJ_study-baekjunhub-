moneys = [500, 100, 50, 10, 5, 1]
mymoney = 1000 - int(input())
cnt = 0

for money in moneys:
    cnt += mymoney // money
    mymoney %= money

print(cnt)