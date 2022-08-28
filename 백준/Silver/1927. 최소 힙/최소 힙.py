import heapq
import sys
input = lambda : sys.stdin.readline().strip()
n=int(input())
a=[int(input()) for i in range(n)]
h=[]
for i in a:
    if i == 0:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h, i)
