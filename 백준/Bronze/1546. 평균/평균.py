n = int(input())
subject = list(map(int, input().split()))

subject.sort()
result = sum(subject) / n / subject[-1] * 100
print(result)