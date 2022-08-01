def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = list(set(report))
    
    reporteduser = {i:0 for i in id_list}
    for tmp in report:
        reporteduser[tmp.split()[1]] += 1
    
    for i in range(len(report)):
        user1, user2 = report[i].split()
        if reporteduser[user2] >= k:
            answer[id_list.index(user1)] += 1
    
    return answer