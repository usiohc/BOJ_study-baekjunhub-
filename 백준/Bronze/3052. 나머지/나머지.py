numl = []
for i in range(10):
    numl.append(int(input()))
    numl[i] %= 42
print(len(list(set(numl))))