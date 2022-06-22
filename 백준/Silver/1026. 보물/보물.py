n = int(input())
nums_a = sorted(list(map(int, input().split())))
nums_b = list(map(int, input().split()))

result = 0
for i in range(n):
    b = max(nums_b)
    nums_b.pop(nums_b.index(b))
    result += nums_a[i] * b

print(result)