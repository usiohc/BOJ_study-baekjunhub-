import sys, math
input = sys.stdin.readline

INF = float('inf')
n,m = map(int,input().split())
bundle,unit = INF,INF
for _ in range(m):
    a,b = map(int,input().split())
    bundle = min(bundle,a)
    unit = min(unit, b)
    
if bundle > unit*6:
    print(unit*n)
elif bundle < n%6*unit:
    print(bundle*math.ceil(n/6))
else:
    print(bundle*(n//6)+unit*(n%6))