n = int(input())
result = [0]*10
digit = 1

while n>0:
    while n%10 != 9:
        for i in str(n):
            result[int(i)] += digit
        n -= 1

    for i in range(10):
        result[i] += (n//10 +1) *digit

    result[0] -= digit
    digit *= 10
    n //= 10

print(*result)