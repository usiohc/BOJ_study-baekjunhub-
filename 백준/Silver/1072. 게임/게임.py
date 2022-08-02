from math import floor
import sys
input = sys.stdin.readline

x, y = map(int, input().split())
e = floor(100 * y / x)
start, end = 0, 1000000000

if e >= 99: 
    print(-1)
else:
    while start <= end:
        mid = (start + end) // 2
        ix, iy = x + mid, y + mid
        
        if floor(100 * iy / ix) > e:
            end = mid - 1
        else:
            start = mid + 1
            
    print(end + 1)