n = int(input())
distances = list(map(int, input().split()))
costs = list(map(int, input().split()))
costs.pop()

tmp = costs[0]
result = 0
for i in range(n-1):
    if costs[i] < tmp:
        tmp = costs[i]
    result += tmp * distances[i]
print(result)