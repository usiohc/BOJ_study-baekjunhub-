n = int(input())
array = list(map(int, input().split()))
arrayrev = array[::-1]
dpinc = [1] * n
dpdec = [1] * n

for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            dpinc[i] = max(dpinc[i], dpinc[j]+1)
        if arrayrev[i] > arrayrev[j]:
            dpdec[i] = max(dpdec[i], dpdec[j]+1)

dpdec.reverse()
result = [a+b-1 for a, b in zip(dpinc, dpdec)]
print(max(result))
