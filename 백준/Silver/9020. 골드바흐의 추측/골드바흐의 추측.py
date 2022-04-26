def isPrime(num):
    for n in range(2, int(num**0.5)+1):
        if num % n ==0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())

    for i in range(n//2, 1, -1):
        temp = n - i

        if isPrime(i) and isPrime(temp):
            print(i, temp)
            break