def solution(n,a,b):
    answer = 0
    array = [0] * n
    array[a-1] = a
    array[b-1] = b
    Flag = True
    while Flag:
        answer += 1
        for i in range(0, n-1, 2):
            if 0 in array[i:i+2]:
                array[i//2] = max(array[i:i+2])
            else:
                Flag = False
                break
        n //= 2
    return answer