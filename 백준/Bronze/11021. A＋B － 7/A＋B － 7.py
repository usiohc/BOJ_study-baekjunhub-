t = int(input())
case = []

for i in range(t):
    case.append(sum(list(map(int, input().split()))))

for i in range(len(case)):
    print('Case #{0}: {1}'.format(i+1, case[i]))