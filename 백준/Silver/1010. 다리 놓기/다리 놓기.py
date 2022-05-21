import math

TC = int(input())

for _ in range(TC):
    m, n = map(int, input().split())
    temp = math.factorial(n)//(math.factorial(m)*math.factorial(n-m))
    print(temp)