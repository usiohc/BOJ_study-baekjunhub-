def solution(lottos, win_nums):    
    cnt = sum([1 if num in win_nums else 0 for num in lottos])
    answer = [6 if cnt == lottos.count(0) == 0 else 7-cnt-lottos.count(0), 6 if 7-cnt>6 else 7-cnt]
    return answer