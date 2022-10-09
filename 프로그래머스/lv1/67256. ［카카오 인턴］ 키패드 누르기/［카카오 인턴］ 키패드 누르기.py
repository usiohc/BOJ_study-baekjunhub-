def solution(numbers, hand): 
    result = ''
    lhand = [0,3]
    rhand = [2,3]
    for e in numbers:
        num = [(e-1)%3, (e-1)//3]
        if e in (1, 4, 7):
            result += 'L'
            lhand = num[:]
        elif e in (3, 6, 9):
            result += 'R'
            rhand = num[:]
        else:
            if e == 0:
                num = [1, 3]
        
            if abs(num[0]-lhand[0]) + abs(num[1]-lhand[1]) < abs(num[0]-rhand[0]) + abs(num[1]-rhand[1]):
                result += 'L'
                lhand = num[:]
            elif abs(num[0]-lhand[0]) + abs(num[1]-lhand[1]) > abs(num[0]-rhand[0]) + abs(num[1]-rhand[1]):
                result += 'R'
                rhand = num[:]
            else:
                if hand == 'right':
                    result += 'R'
                    rhand = num[:]
                else:
                    result += 'L'
                    lhand = num[:]
                
    return result