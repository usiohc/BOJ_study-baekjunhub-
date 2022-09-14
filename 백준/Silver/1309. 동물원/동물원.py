n = int(input())
minus2 = 3
minus1 = 7

for i in range(3, n+1):
    minus1, minus2 = (minus2 + minus1*2)%9901, minus1
if n == 1:
    print(minus2)
else:
    print(minus1)