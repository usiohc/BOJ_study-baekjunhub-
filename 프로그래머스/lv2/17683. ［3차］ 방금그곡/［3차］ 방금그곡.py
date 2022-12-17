def solution(m, musicinfos):
    result = []
    
    for musicinfo in musicinfos:
        info = musicinfo.split(',')
        s = info[0].split(':')
        e = info[1].split(':')
        
        t = (int(e[0]) - int(s[0])) * 60 + int(e[1]) - int(s[1])

        tmp = to_hash(info[3])
        tmp = tmp * (t // len(tmp)) + tmp[:t%len(tmp)]
        
        if to_hash(m) in tmp:
            result.append([info[2], t])

    if len(result) == 0:
        return "(None)"
    
    else:
        return sorted(result, key = lambda x: (-x[1]))[0][0]

def to_hash(m):
    return m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")