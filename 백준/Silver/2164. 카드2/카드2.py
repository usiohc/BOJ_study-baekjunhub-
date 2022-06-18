import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
que = deque()

que += [i for i in range(1, n+1)]


for i in range(1, len(que)):
    que.popleft()
    que.append(que.popleft())

print(*que)