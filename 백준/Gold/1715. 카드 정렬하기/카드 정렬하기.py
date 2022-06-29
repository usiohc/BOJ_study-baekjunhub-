import sys, heapq
input = sys.stdin.readline

n = int(input())
cards = sorted([int(input()) for _ in range(n)])
heapq.heapify(cards)
result = 0

if n == 1:
    print(result)
else:
    while len(cards) != 1:
        card_a = heapq.heappop(cards)
        card_b = heapq.heappop(cards)
        tmp = card_a + card_b
        result += tmp
        heapq.heappush(cards, tmp)

    print(result)