n = int(input())
if n == 1:
    exit(print(1))
temp = 1
idx = 1
while True:
    temp = temp + idx*6
    if n < temp + 1:
        print(idx + 1)
        break
    idx += 1