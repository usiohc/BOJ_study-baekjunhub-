n = int(input())
i = 2
while True:
    if n % i == 0:
        n = n // i
        print(i)
        continue
    elif n % i < n:
        i = i+1
        continue
    break