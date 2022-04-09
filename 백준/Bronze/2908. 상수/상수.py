num1, num2 = map(int, input().split())

rnum1 = num1//100 + (num1//10%10)*10 + (num1%10)*100
rnum2 = num2//100 + (num2//10%10)*10 + (num2%10)*100

print(max(rnum1, rnum2))