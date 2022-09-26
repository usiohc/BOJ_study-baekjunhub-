def solution(n):
    answer = ''
    array = [int(i) for i in str(n)]
    array.sort(reverse=True)
    
    for i in range(len(array)):
        answer += str(array[i])
    
    return int(answer)