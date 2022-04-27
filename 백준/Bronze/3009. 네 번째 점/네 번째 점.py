x, y = [], []
res_x, res_y = 0, 0

for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.sort(), y.sort()
for i in range(0, -2, -1):
    if x.count(x[i]) == 1:
        res_x = x[i]
    if y.count(y[i]) == 1:
        res_y = y[i]

print(res_x, res_y)