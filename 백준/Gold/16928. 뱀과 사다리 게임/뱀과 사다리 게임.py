from collections import deque

n, m = map(int, input().split())
gamemap = [i for i in range(101)]
distance = [0] * 101
for i in range(n+m):
    x, y = map(int, input().split())
    gamemap[x] = y
    
p = 1
queue = deque([p])
while p != 100:
    p = queue.popleft()

    for j in range(1, 7):
        if p+j <= 100:
            if distance[gamemap[p+j]] == 0:
                queue.append(gamemap[p+j])
                distance[gamemap[p+j]] = distance[p] + 1

print(distance[-1])