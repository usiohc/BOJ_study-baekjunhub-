import math

n, k = map(int, input().split())
temp = math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
print(temp % 10007)