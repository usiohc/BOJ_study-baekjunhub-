def solution(price, money, count):
    result = sum(list(price*c for c in range(1, count+1))) - money
    if result < 0:
        result = 0
    return 0 if result<0 else result