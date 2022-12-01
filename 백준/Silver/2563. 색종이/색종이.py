fullmap = [[0 for i in range(101)] for i in range(101)]

for t in range(int(input())):
    c, r = map(int, input().split())
    for i in range(r, r+10):
        for j in range(c, c+10):
            fullmap[i][j] += 1

ans = 0
for i in range(101):
    for j in range(101):
        if fullmap[i][j] >= 1:
            ans += 1
print(ans)