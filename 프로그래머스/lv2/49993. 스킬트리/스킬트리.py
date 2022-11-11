def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        learn = ''        
        for s in st:
            if s in skill:
                learn += s
        
        if skill.startswith(learn):
            answer += 1
                
        
    
    return answer