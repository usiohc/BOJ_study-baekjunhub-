a,b = list(map(int,input().split()))
c,d = list(map(int,input().split()))

n = (b*c+a*d)
nn = b*d

def GCD(x,y):
    while y:
        x,y = y,x%y
    return x

gcd = GCD(n,nn)

n = int(n/gcd)
nn = int(nn/gcd)

print(f"{n} {nn}")