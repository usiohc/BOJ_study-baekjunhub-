m = int(input())
n = int(input())
num_sum = 0
num_min = 10**6

for i in range(m , n+1):
    for j in range(2, i+1):
        if j == i:
            num_sum += j
            if num_min > i:
                num_min = i
            break
        if i % j == 0:
            break

if num_sum==0:
    print(-1)
else:
    print(num_sum)
    print(num_min)