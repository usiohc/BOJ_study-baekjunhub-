dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

import heapq
from collections import deque

def solution(land, h):
    answer = 0
    n = len(land)
    
    visited = [[-1]*n for _ in range(n)]
    heap = [(0,0,0)]

    while heap:
        v, x, y = heapq.heappop(heap)

        if visited[x][y] == -1:
            visited[x][y] = v
            answer += v
        else:
            continue

        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]

            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1:
                nv = abs(land[x][y] - land[nx][ny])
                if nv <= h:
                    nv = 0
                heapq.heappush(heap, (nv, nx, ny))
                # heap으로 최소값부터 순차 탐색하는 알고리즘 작성

    # print(*visited, sep='\n')

    return answer