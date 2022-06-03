import sys
input = sys.stdin.readline

n = int(input())

triangle = [list(map(int, input().split())) for _ in range(n)]

# 누적합의 형태로 for문을 사용
# 제일 왼쪽과 오른쪽은 한번만 계산하면 되기 때문에 index error를 방지하기위해 if문을 사용함
# i는 depth, j는 col이라고 보면 될듯
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            # 제일 왼쪽
            triangle[i][j] = triangle[i][j] + triangle[i-1][j]
        elif j == i:
            # 제일 오른쪽
            triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
        else:
            # 아닐때
            triangle[i][j] = triangle[i][j] + max(triangle[i-1][j], triangle[i-1][j-1])

print(max(triangle[-1]))