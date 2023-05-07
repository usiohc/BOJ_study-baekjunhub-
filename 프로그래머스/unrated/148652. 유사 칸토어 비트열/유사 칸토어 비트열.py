def solution(n, l, r):
    '''
    1 1개
    11011 4개
    11011 11011 00000 11011 11011 index index 3, 8, 11 12 13 14 15 18 21 | 16개
    25*5 = 125 | 16+16+0+16+16 64
    125*5 = 625 | 64+64+0+64+64
    '''
    
    answer = r-l+1 # 1의 개수
    # print(answer)
    
    for i in range(l-1,r):
        while i>0:
            n1, n2 = divmod(i, 5)
            # print(i, n1, n2)
            
            if n1==2 or n2==2:
                answer-=1
                # print(answer)
                break
                
            i = n1


    return answer