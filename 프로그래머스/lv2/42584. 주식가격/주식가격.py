def solution(prices):
    answer = []
    l = len(prices)
    for i in range(l-1):
        tmp = l-i-1
        for j in range(i+1,l):
            if prices[j] < prices[i]:
                tmp = j - i
                break
        answer.append(tmp)
    return answer+[0]