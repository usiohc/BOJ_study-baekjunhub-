t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    k_0 = [x for x in range(1, n+1)]
    for k in range(k):
        for i in range(1, n):
            k_0[i] += k_0[i-1]
    print(k_0[-1])