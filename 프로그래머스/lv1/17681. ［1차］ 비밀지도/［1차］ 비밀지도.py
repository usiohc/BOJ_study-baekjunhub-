def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        n1 = format(arr1[i], 'b') 
        n1 = '0' * (n - len(n1)) + n1
        n2 = format(arr2[i], 'b')
        n2 = '0' * (n - len(n2)) + n2

        s = ''
        for x, y in zip(n1, n2):
            if x == '1' or y == '1':
                s += '#'
            else:
                s += ' '
        answer.append(s)
        
    return answer