import math
import sys

input = sys.stdin.readline

w, h ,x, y, p = map(int, input().rstrip().split())
r = h//2

count = 0
for _ in range(p):
    a, b = map(int, input().rstrip().split())
    # a, b = a - x, b - y
    # (a, b) (x, y+r)
    # (a, b) (x+w, y+r)

    result = 0
    if a < x:
        result = math.sqrt((a - x)**2 + (b - (y+r))**2)
    elif a > x + w:
        result = math.sqrt((a - (x+w))**2 + (b - (y+r))**2)
    else:
        if y <= b <= y+h:
            count += 1
        continue
    if result <= r:
        count += 1

print(count)