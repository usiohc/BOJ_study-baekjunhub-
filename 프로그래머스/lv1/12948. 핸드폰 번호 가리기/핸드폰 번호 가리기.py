def solution(phone_number):
    answer = '*'*len(phone_number[-5::-1])+phone_number[-4:]
    return answer