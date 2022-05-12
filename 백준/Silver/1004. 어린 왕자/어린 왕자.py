import math

TC = int(input())

for i in range(TC):
    x1, y1, x2, y2 = map(int, input().split())
    count = 0
    n = int(input())
    for c_i in range(n):
        cx, cy, cr = map(int, input().split())

        xyd1 = math.sqrt((x1-cx)**2 + (y1-cy)**2)
        xyd2 = math.sqrt((x2-cx)**2 + (y2-cy)**2)

        if (xyd1 < cr and xyd2 > cr) or (xyd1 > cr and xyd2 < cr):
            count += 1

    print(count)