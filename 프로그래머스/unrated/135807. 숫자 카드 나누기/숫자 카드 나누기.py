from math import gcd

def solution(arrayA, arrayB):
    answer = set()
    answer.add(0)
    a, b = arrayA[0], arrayB[0]

    for aa, ab in zip(arrayA[1:], arrayB[1:]):
        a, b = gcd(a, aa), gcd(b, ab)
    
    for aa in arrayA:
        if aa % b == 0:
            break
    else:
        answer.add(b)
        
    for ab in arrayB:
        if ab % a == 0:
            break
    else:
        answer.add(a)
        
    return max(answer)