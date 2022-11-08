import heapq

def solution(s, K):
    answer = 0
    heapq.heapify(s)
    while s[0] < K:
        if len(s) <= 1:
            return -1
        else:
            answer += 1
            
            n1 = heapq.heappop(s)
            n2 = heapq.heappop(s)
            heapq.heappush(s, n1+ n2*2)
            
    return answer