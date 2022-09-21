T = int(input())

for _ in range(T):
    a, b = map(int, input().split(' '))
    num_a = 0
    num_b = 0

    if a == 0:
        num_a = 0
    elif a == 1:
        num_a = 500
    elif 2 <= a <= 3:
        num_a = 300
    elif 4 <= a <= 6:
        num_a = 200
    elif 7 <= a <= 10:
        num_a = 50
    elif 11 <= a <= 15:
        num_a = 30
    elif 16 <= a <= 21:
        num_a = 10

    if b == 0:
        num_b = 0
    if b == 1:
        num_b = 512
    elif 2 <= b <= 3:
        num_b = 256
    elif 4 <= b <= 7:
        num_b = 128
    elif 8 <= b <= 15:
        num_b = 64
    elif 16 <= b <= 31:
        num_b = 32

    print((num_a + num_b) * 10000)