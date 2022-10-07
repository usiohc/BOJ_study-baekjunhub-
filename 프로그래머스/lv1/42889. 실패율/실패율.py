def solution(N, stages):
    stage = {}
    stage_user = [0] + [stages.count(i) for i in range(1, N+ 2)]
    
    for i in range(1, N+1):
        if sum(stage_user[i:]) == 0:
            stage[str(i)] = 0
        else:
            stage[str(i)] = stage_user[i] /sum(stage_user[i:])
            
    # print(stage_user)
    # print(stage)

    dict_stage = list(zip(stage.keys(), stage.values()))
    dict_stage.sort(reverse=True, key=lambda x: x[1])
    answer = [int(dict_stage[i][0]) for i in range(N)]
    
    return answer