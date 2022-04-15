t = int(input())
for idx in range(t):
    h, w, n = map(int, input().split())

    wid = n//h+1
    hei = n%h
    if n % h ==0:
        wid = n//h
        hei = h
    print(hei*100+wid)