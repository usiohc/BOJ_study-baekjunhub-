import fractions

n = int(input())
rings = list(map(int, input().split()))

for i in range(1, n):
    temp = fractions.Fraction(rings[0], rings[i])
    print(f'{temp.numerator}/{temp.denominator}')