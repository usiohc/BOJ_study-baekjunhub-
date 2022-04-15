def fibo_recursion(n):
    if n <= 1:
        return n
    return fibo_recursion(n-1) + fibo_recursion(n-2)

n = int(input())
print(fibo_recursion(n))