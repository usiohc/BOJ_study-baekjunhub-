def solution(name):
    answer = 0
    min_move = len(name) - 1
    
    for s in name[::-1]:
        if s == 'A':
            min_move -= 1
        else:
            break
    else:
        return answer
        
    for i in range(len(name)):
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        n = i + 1
        while n < len(name) and name[n] == 'A':
            n += 1
        min_move = min(min_move, 2*i+len(name)-n, 2*(len(name)-n)+i)
    
    return answer+min_move