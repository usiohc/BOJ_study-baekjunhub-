h, m = map(int, input().split())
t = int(input())

t = 60 * h + m + t
h, m = t // 60 % 24, t % 60

print(h, m)