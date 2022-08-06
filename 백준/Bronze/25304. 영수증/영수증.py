import sys
input = sys.stdin.readline

def solve(target, datas) -> str:
    return 'Yes' if target == sum([x[0] * x[1] for x in datas]) else 'No'

x = int(input())
n = int(input())
datas = [list(map(int, input().split())) for _ in range(n)]

print(solve(x, datas))