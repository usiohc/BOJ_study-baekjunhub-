n = int(input())
tiles = [0 for _ in range(n+1)]
if n == 1:
    print(1)
else:
    tiles[1], tiles[2] = 1, 2
    for i in range(3, n+1):
        tiles[i] = (tiles[i-2] + tiles[i-1]) % 15746
    print(tiles[n])