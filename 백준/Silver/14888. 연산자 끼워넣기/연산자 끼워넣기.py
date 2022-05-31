import itertools

def plus(a, b):
    return a+b

def minus(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    if a < 0:
        return (abs(a)//b) * -1
    else:
        return a//b


n = int(input())
nums = list(map(int, input().split()))
p, mi, mu, d = map(int, input().split())
fours = ' '.join('+'*p+'-'*mi+'*'*mu+'/'*d).split()
permu = list(set(itertools.permutations(fours, n-1)))

result_list = []
for per in permu:
    a = nums[0]
    for i in range(1, n):
        b = nums[i]
        if per[i-1] == '+':
            a = plus(a, b)
        elif per[i-1] == '-':
            a = minus(a, b)
        elif per[i-1] == '*':
            a = mul(a, b)
        elif per[i-1] == '/':
            a = div(a, b)
    result_list.append(a)

print(max(result_list), min(result_list), sep='\n')