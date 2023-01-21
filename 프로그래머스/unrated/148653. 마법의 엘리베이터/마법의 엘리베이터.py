def solution(storey):
    answer = 0

    while storey != 0:
        num = storey % 10 

        if num >= 6:
            storey += 10 - num
            answer += 10 - num
        else:
            if num == 5 and storey//10 %10 >= 5:
                storey += 10 - num
                answer += 10 - num
            else:
                answer += num
            
        storey //= 10
        
    return answer