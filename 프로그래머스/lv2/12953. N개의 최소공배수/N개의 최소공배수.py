import math

def solution(arr):
    # answer = math.lcm(map(int, arr))
    answer = 0

    num = 1
    for el in arr:
        num *= el
    
    for i in range(max(arr), num+1):
        Flag = True
        for el in arr:
            if i%el!=0:
                Flag = False
                break
        if Flag:
            answer = i
            break
            
    return answer