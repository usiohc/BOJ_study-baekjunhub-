from collections import Counter

TC = int(input())

for _ in range(TC):
    n = int(input())
    items = []
    for _ in range(n):
        _, item = input().split()
        items.append(item)

    result = 1
    items_cnt = Counter(items)
    for k in items_cnt:
        result *= items_cnt[k] + 1

    print(result-1)