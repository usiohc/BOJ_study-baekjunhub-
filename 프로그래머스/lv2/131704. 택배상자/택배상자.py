# def solution(order):
#     answer = 0
    
#     ctb = [i for i in range(len(order), 0, -1)]
#     asst = [0]
    
#     for o in order:
#         if o == asst[-1]:
#             asst.pop()
#             answer += 1
#         elif o in ctb:
#             answer += 1
#             idx = ctb.index(o)
#             for _ in range(len(ctb)-idx-1):
#                 asst.append(ctb.pop())
#             # asst += ctb[idx+1:][::-1]
#             # del ctb[idx:]
#         else:
#             break
            
#     return answer

def solution(order):
    asst = []
    num = 1
    i = 0
    
    while num <= len(order):
        asst.append(num)
        
        while asst[-1] == order[i]:
            del asst[-1]
            i += 1
            if len(asst) == 0:
                break

        num += 1

    return i