
def solution(numbers):
    answer = []
    
    for n in numbers:
        if n % 2 == 0:
            answer.append(n+1)
        else:
            n = bin(n)[2:]
            
            tmp = 1
            for i in range(2, len(n)+1):
                if n[-i] == '0':
                    tmp = 10 ** (i-1)
                    break
            
            if tmp == 1:
                tmp = 10 ** len(n)
            
            n = int(n) + tmp - tmp//10
            answer.append(int(str(n), 2))
    return answer