import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
m = int(input())
start, end = 0, max(s)
while start <= end:
    mid = (start + end) // 2
    num = 0
    for i in s:
        if i >= mid: 
            num += mid
        else: 
            num += i
    if num <= m: 
        start = mid + 1
    else: 
        end = mid - 1
print(end)