def solution(price, money, count):
    result = sum(price*c for c in range(1, count+1)) - money
    return 0 if result<0 else result