import heapq

def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k:
        return -1

    n = len(food_times)
    heap = []
    for i in range(n):
        heapq.heappush(heap, (food_times[i], i+1))

    l_cost = 0
    while heap:
        if (heap[0][0]-l_cost)*n > k:
            heap.sort(key= lambda x:x[1])
            return heap[k%n][1]
        else:
            ft = heapq.heappop(heap)
            k -= (ft[0] - l_cost) * n
            l_cost = ft[0]
            n -= 1 

    return -1