from collections import Counter

def solution(topping):
    answer = 0
    
    dic = Counter(topping)
    a = set()
    b = set(topping)
    
    for i in range(len(topping)):
        num = topping[i]
        a.add(num)
        
        dic[num] -= 1
        if dic[num] < 1:
            b.remove(num)

        if len(a) == len(b):
            answer += 1
    
    return answer