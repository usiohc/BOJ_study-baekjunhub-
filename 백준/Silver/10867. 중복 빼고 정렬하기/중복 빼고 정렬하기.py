n = int(input())

array = list(map(int, input().split()))
array = list(set(array))
array.sort()
print(*array)