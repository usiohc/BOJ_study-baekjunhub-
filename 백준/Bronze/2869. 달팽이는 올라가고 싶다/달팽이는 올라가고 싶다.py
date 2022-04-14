from math import ceil
a, b, v = map(int, input().split())
v = v - b
now = a-b
left = ceil(v/now)
print(left)