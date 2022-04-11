alpabet = input()
croa = ['c=','c-','dz=','d-','lj','nj','s=','z=']

temp = 0
for i in croa:
    temp += alpabet.count(i)

print(len(alpabet)-temp)
