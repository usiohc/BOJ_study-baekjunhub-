import itertools
from collections import Counter

def solution(orders, course):
    answer = []
    max_values= []
    menus = []

    for c in course:
        menu = []
        for order in orders:
            cb = itertools.combinations(sorted(order), c)
            menu += [a for a in list(cb)]
        if len(menu)>=1:
            max_values.append(Counter(menu).most_common(1)[0][1])
            menus.append(menu)

    for _max, menu in zip(max_values, menus):
        for k, v in Counter(menu).items():
            if _max == v and v >=2:
                answer.append(''.join(k))
    return sorted(answer)