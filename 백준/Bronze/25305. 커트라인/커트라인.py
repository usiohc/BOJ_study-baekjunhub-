n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True) # 큰 수부터 정렬 (역정렬)
print(nums[k-1])
