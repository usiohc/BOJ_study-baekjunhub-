from collections import Counter

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list_cnt = Counter(n_list)
for i in m_list:
    if i in n_list_cnt:
        print(n_list_cnt[i], end=' ')
    else:
        print(0, end=' ')
