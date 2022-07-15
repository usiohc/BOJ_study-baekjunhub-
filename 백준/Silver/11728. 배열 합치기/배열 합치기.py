n, m = map(int, input().split())
array = list(map(int, input().split()))
array.extend(map(int, input().split()))
print(*sorted(array))