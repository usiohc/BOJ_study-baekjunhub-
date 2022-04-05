# A + B 2차원 리스트 활용 해서 출력
t = int(input())
case = []

for i in range(t):
    case.append(list(map(int, input().split())))

for i in range(len(case)):
    print(f'Case #{i+1}: {case[i][0]} + {case[i][1]} = {sum(case[i])}')