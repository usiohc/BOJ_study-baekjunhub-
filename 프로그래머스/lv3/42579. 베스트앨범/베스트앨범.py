def solution(genres, plays):
    answer = []
    
    songs = {s:[0, []] for s in set(genres)}
    for i in range(len(genres)):
        songs[genres[i]][0] += plays[i]
        songs[genres[i]][1] += [[plays[i], i]]
    songs = dict(sorted(songs.items(), key = lambda x: x[1][0], reverse=True))

    for k, v in songs.items():
        v[1].sort(key= lambda x:x[0], reverse=True)
        for vv in sorted(v[1], key= lambda x:x[0], reverse=True)[:2]:
            answer.append(vv[1])
    return answer