c = int(input())
arr = []
for i in range(c):
    a, b = map(int, input().split())
    arr.append(a+b)
for i in arr:
    print(i)