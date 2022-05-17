import sys

def binarySearch(m):
    global n_nums

    start = 0
    end = len(n_nums) - 1
    mid = (start+end)//2

    while end - start >= 0:
        # print(mid)
        if n_nums[mid] == m:
            return 1
        elif n_nums[mid] <= m:
            start = mid+1
        else:
            end = mid-1
        mid = (end+start) // 2
    return 0


input()
n_nums = list(map(int, sys.stdin.readline().split()))
n_nums.sort()
input()
m_nums = list(map(int, sys.stdin.readline().split()))

for i in m_nums:
    temp = binarySearch(i)
    print(temp, end=' ')