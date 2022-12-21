def solution(babbling):
    answer = 0
    lst = ["aya", "ye", "woo", "ma"]
    F_lst = [ "ayaaya", "yeye", "woowoo", "mama"]
    for b in babbling:
        for f in F_lst:
            if f in b:
                break
        else:
            for l in lst:
                if l in b:
                    b = b.replace(l, ' ')
            if b.strip() == '':
                answer += 1

    return answer