import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque()
for i in range(n):
    cmdnum = 0
    cmd = input().rstrip()
    if cmd[-1].isnumeric():
        cmd, cmdnum = map(str, cmd.split())

    if cmd == 'push':
        queue.append(int(cmdnum))
    elif cmd == 'pop':
        if queue:
            tmp = queue.popleft()
            print(tmp)
        else:
            print(-1)
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif cmd == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)