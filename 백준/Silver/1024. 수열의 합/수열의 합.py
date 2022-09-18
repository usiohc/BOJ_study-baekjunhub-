N,L=map(int,input().split())
 
for i in range(L,101):
    Sum=0
    start=int((2*N-i**2+i)/(2*i))
    if start<0:
        continue
    for j in range(start,start+i):
        Sum+=j
    if Sum==N:
        for j in range(start,start+i):
            print(j,end=' ')
        exit()
 
print(-1)