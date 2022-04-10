alpabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

temp = list(input())
temp_time = 0

for unit in alpabet:
    for i in unit:
        for t in temp:
            if i == t:
                temp_time += alpabet.index(unit)+3

print(temp_time)