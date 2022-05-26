Pn = [1, 1, 1, 2, 2]

for i in range(4, 100):
    temp = Pn[i-4] + Pn[i]
    Pn.append(temp)

n = int(input())

for _ in range(n):
    p = int(input())
    print(Pn[p-1])