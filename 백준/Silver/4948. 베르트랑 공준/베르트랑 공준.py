def isPrime(num):
    if num == 1:
        return False
    else:
        for n in range(2, int(num**0.5)+1):
            if num % n ==0:
                return False
        return True

Num_list = list(range(2,246912))
Sort_list = []
for i in Num_list:
    if isPrime(i):
         Sort_list.append(i)

while True:
    m = int(input())
    n = m*2

    if m == 0:
        break
    count = 0
    for i in Sort_list:
        if m < i <= n:
            count += 1
    print(count)