def div_two(n):
    result = 0
    while n != 0:
        n //= 2
        result += n
    return result

def div_five(n):
    result = 0
    while n != 0:
        n //= 5
        result += n
    return result

n, m = map(int, input().split())

if m == 0:
    print(0)
else:
    print(min(div_two(n)-div_two(m)-div_two(n-m),
              div_five(n)-div_five(m)-div_five(n-m)))