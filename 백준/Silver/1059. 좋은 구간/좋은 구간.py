s = int(input())
array = list(map(int, input().split()))
n = int(input())
array.append(0)
array.sort()

cnt = 0
for i in range(len(array)):
    if array[i] == n or array[i+1] == n:
        cnt = 0
        break
    elif array[i] < n and array[i+1] > n:
        cnt = (n - array[i]) * (array[i+1] - n) - 1
        break
print(cnt)