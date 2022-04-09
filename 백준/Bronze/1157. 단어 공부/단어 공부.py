temp_str = input().lower()
temp_dic = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}

for i in temp_str:
    if i in temp_dic:
        temp_dic[i] += 1

same_value = []
for k, v in temp_dic.items():
    if v == max(temp_dic.values()):
        same_value.append(v)
        key = k

if len(same_value) > 1:
    print('?')
else:
    print(key.upper())