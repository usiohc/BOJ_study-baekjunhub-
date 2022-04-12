n = int(input())
count = 0
for _ in range(n):
    temp_str = list(input())
    err = 0

    for i in range(len(temp_str)-1):
        if temp_str[i] != temp_str[i+1]:
            temp_new = temp_str[i+1:]
            if temp_new.count(temp_str[i]) > 0:
                err += 1
                continue
    if err == 0:
        count += 1
print(count)