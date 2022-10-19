def solution(brown, yellow):
    answer = []
    x, y = 0, 0
    idx = 1
    while idx <= brown+yellow :
        if yellow % idx == 0:
            x = yellow//idx
            y = idx
            if x*2 + y*2 + 4 == brown:
                x += 2
                y += 2
                break
        idx += 1      
    return [max(x, y), min(x, y)]