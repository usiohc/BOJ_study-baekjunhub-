n = int(input())
words = [list(map(str, input())) for _ in range(n)]
alpha = {}
for word in words:
    for i in range(len(word)):
        if not word[i] in alpha:
            alpha.setdefault(word[i], 10**(len(word)- i -1))
        else:
            alpha[word[i]] += 10**(len(word)-i-1)

nums = []
for i in alpha.values():
    nums.append(i)
nums.sort(reverse=True)

result = 0
for i in range(len(nums)):
    result += (9-i) * nums[i]

print(result)