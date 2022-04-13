a, b, price = map(int, input().split())
if b >= price:
    print(-1)
else:
    print(int(a/(price-b)+1))
