def solution(n, k):
    answer = 0

    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    rev_base = rev_base[::-1]

    nums = list(map(int, filter(bool, rev_base.split('0'))))

    for num in nums:
        if num < 2:
            continue

        FLAG = True
        for i in range(2, int(num ** 0.5 + 1)):
            if num % i == 0:
                FLAG = False
                break
        if FLAG:
            answer += 1


    return answer