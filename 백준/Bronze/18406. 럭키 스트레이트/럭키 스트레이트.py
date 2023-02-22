n = list(map(int, input()))
l, r = n[:len(n)//2],n[len(n)//2:]
if  sum(l) == sum(r):
    print('LUCKY')
else:
    print('READY')