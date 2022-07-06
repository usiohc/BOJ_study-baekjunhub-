from collections import deque

n, k = map(int, input().split())
queue = deque()
queue.append(n)
maxnum = 10 ** 5
d = [0] * (maxnum+1)

while queue:
    q = queue.popleft()
    if q == k:
        print(d[q])
        break
    for dx in (q-1, q+1, q*2):
        if 0 <= dx <= maxnum and not d[dx]:
            d[dx] = d[q] + 1
            queue.append(dx)