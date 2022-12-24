N = int(input())
filename = [input() for _ in range(N)]

result = list(filename[0]) 
for i in range(N):
    for j in range(len(result)):
        if result[j] != filename[i][j]: 
            result[j]='?'
print(''.join(result))