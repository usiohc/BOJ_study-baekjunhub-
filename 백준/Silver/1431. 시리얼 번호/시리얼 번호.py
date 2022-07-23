import re

n = int(input())
lines = sorted([input() for _ in range(n)])
lines.sort(key= lambda x:(len(x),
                          sum(list(map(int, re.findall(r'\d', x)))),
                          x))

print(*lines, sep='\n')