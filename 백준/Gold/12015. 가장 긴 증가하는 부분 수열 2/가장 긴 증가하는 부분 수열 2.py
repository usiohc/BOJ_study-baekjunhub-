a = int(input())
nums = list(map(int, input().split()))
lis = [0]

for num in nums:
    if lis[-1] < num:
        lis.append(num)
    else:
        start, end = 0, len(lis)

        while start<end:
            mid = (start+end)//2
            if lis[mid] < num:
                start = mid+1
            else:
                end = mid
                
        lis[end] = num

print(len(lis)-1)