def solution(begin, end):
    lst = []
    if begin == 1:
        lst.append(0)
        begin += 1

    for n in range(begin, end+1):
        tmp = [1]
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                if n//i > 10**7:
                    tmp = [1]
                    continue
                    
                tmp.append(i)
                tmp.append(n//i)
                
        lst.append(max(tmp))
    return lst