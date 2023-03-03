from collections import deque

def chk_possible(array):
    for x, y, a in array:
        if a == 0:
            # 0행, 보의 한쪽 끝부분, 다른 기둥 위
            if y == 0 or [x-1, y, 1] in array or [x, y, 1] in array or [x, y-1, 0] in array:
                continue
            return True
        else:
            # 한쪽 끝부분이 기둥 위
            if ([x-1, y, 1] in array and [x+1, y, 1] in array) or [x, y-1, 0] in array or [x+1, y-1, 0] in array :
                continue
            return True
    return False
def solution(n, build_frame):
    answer = []
    # build_frame.sort(key= lambda x: (x[1], x[0], -x[3]))    
    que = deque(build_frame)
    
    for i in range(len(que)):
        x, y = que[i][0], que[i][1]
        a, b = que[i][2], que[i][3]
        if b == 1:
            answer.append([x, y, a])
            if chk_possible(answer):
                answer.remove([x, y, a])
        else:
            answer.remove([x, y, a])
            if chk_possible(answer):
                answer.append([x, y, a])
    
    return sorted(answer)