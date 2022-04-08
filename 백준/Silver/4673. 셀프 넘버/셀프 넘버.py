nums = []
for num in range(1, 10000 + 1):
    temp = num + num//1000 + num%1000//100 + num%100//10 + num%10
    if temp not in nums:
        nums.append(temp)

for num in range(1, 10000 + 1):
    if num not in nums:
        print(num)