def binary_search(num, start, end):
    while start <= end:
        i = (start+end) // 2
        if n_nums[i] == num:
            return True
        elif n_nums[i] > num:
            end = i - 1
        elif n_nums[i] < num:
            start = i + 1

    return False


t = int(input())
for _ in range(t):
    n = int(input())
    n_nums = sorted(list(map(int, input().split())))
    m = int(input())
    m_nums = list(map(int, input().split()))

    for m_num in m_nums:
        result = binary_search(m_num, 0, n-1)
        if result:
            print(1)
        else:
            print(0)