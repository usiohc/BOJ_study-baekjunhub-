def solution(files):
    hnt = []
    for file in files:
        head, num, tail = '', '', ''
        idx = 0
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                for j in range(5, 0, -1):
                    if file[i:i+j].isdigit():
                        num = file[i:i+j]
                        idx = i+j
                        break
                tail = file[idx:]
                break
        hnt.append([head, num, tail])        
    
    hnt.sort(key= lambda x:(x[0].upper(), int(x[1])))
    answer = [file[0]+file[1]+file[2] for file in hnt]
    return answer