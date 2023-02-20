s = list(map(int, input()))

lst = [s[0]]

for i in range(1, len(s)):
    if lst[-1] != s[i]:
        lst.append(s[i])
if len(lst)==1:
    print(0)
else:
    print(min(lst.count(1), lst.count(0)))