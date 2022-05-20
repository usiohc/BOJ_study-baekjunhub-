s = input()
s_list = [s[i] for i in range(len(s))]
for i in range(len(s)):
    for j in range(i):
        s_list.append(s[j:i+1])
print(len(set(s_list)))