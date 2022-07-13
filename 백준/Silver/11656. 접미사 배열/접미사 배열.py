S = input()

string = []
for i in range(len(S)) :
    string.append(S[i:])

string.sort()
for i in string :
    print(i)