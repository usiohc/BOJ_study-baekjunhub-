def dfs(array, now, target, cnt):
    if now == target:
        result.append(cnt)
    
    for i in range(l):
        s = now[:i] + now[i+1:]
        for w in range(len(array)):
            if s == array[w][:i]+array[w][i+1:]:
                tmp_now = array.pop(w)
                dfs(array, tmp_now, target, cnt+1)
                array.insert(w, tmp_now)
                
def solution(begin, target, words):
    global l, result
    l = len(begin)
    result = []
    
    if target not in words:
        return 0
    else:
        dfs(words, begin, target, 0)

        return min(result)