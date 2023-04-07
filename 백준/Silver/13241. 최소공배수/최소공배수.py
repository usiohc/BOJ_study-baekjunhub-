a, b = map(int, input().split())
num = a*b

while b:
    if a>b:
        a, b = b, a
    b %= a

print(num//a)