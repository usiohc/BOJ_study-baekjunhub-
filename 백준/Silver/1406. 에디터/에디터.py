import sys
input = sys.stdin.readline

st1 = list(input().strip())
st2 = []
n = int(input())

for i in range(n):
    C = input().split()
    if C[0] == 'L' and st1:
        st2.append(st1.pop())
    elif C[0] == 'D' and st2:
        st1.append(st2.pop())
    elif C[0] == 'B' and st1:
        st1.pop()
    elif C[0] == 'P':
        st1.append(C[1])

st1.extend(reversed(st2))
print(''.join(st1))