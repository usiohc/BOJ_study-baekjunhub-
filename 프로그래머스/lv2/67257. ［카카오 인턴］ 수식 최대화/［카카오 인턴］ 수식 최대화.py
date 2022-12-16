from itertools import permutations

def solution(expression):
    answer = []
    oper = ['+', '-', '*']
    oper = list(permutations(oper, 3))

    for op in oper:
        tmp_list = []
        for el in expression.split(op[0]):
            tmp = [f'({i})' for i in el.split(op[1])]
            tmp_list.append(f'({op[1].join(tmp)})')

        answer.append(abs(eval(op[0].join(tmp_list))))

    return max(answer)