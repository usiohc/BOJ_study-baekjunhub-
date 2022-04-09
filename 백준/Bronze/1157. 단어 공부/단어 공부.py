temp_str = input().upper()
temp_list = list(set(temp_str))
temp_count = [temp_str.count(i) for i in temp_list]

if temp_count.count(max(temp_count)) > 1:
    print('?')
else:
    print(temp_list[temp_count.index(max(temp_count))])
