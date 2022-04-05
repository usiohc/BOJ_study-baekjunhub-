ab = []

while(True):
    a, b = map(int, input().split())
    if a == b == 0:
        break
    ab.append(a+b)

for i in ab:
    print(i)