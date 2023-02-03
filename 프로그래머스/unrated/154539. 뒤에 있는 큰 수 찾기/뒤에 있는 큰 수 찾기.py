def solution(numbers): 
    result = [-1] * len(numbers)
    stack = []
    for i in range(len(numbers)):
        while stack and stack[-1][0] < numbers[i]:
            result[stack.pop()[1]] = numbers[i]
        stack.append((numbers[i], i))
    
    return result