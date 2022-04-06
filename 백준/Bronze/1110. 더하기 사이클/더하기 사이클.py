n = int(input())
result = n
cycle = 0

while True:
    # l = left| //연산자 10자리 받기, r = right| % 연산자 1자리 나머지 받기
    l, r = result//10, result%10
    # result = (1자리값*10) + (l+r 값의 1자리값 가져옴)
    result = (r * 10) + (l + r) % 10
    cycle += 1
    if n == result:
        break

print(cycle)