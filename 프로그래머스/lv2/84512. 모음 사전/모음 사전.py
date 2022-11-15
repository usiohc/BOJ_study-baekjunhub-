
def dfs(a):
    global al, answer, word
    
    answer += 1

    if a == word:
        return True
    elif len(a) == 5:
        return False

    for t_a in al:
        if dfs(a+t_a):
            return True

def solution(w):
    global al, answer, word
    word = w
    al = ['A', 'E', 'I', 'O','U']
    answer = 0
    
    for a in al:
        if dfs(a):
            return answer