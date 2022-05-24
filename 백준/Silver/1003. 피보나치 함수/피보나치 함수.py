testcase = int(input())
for i in range(testcase):
    zero, one = 1, 0
    n = int(input())
    for _ in range(n):
        zero, one = one, zero+one
    print(zero, one)