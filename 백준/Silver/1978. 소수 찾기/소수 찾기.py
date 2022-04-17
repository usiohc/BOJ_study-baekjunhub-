n = int(input())
count = 0
num_list = list(map(int, input().split()))
if len(num_list)== n:
    for temp in num_list:
        for i in range(2, temp+1):
            if i == temp:
                count += 1
                break
            if temp % i == 0:
                break
print(count)