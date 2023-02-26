ax, ay, bx, by, cx, cy = map(int, input().split())
if ((ax-bx)*(ay-cy)==(ay-by)*(ax-cx)):
    print(-1.0)
else:
    ab = ((ax-bx)**2 + (ay-by)**2)**0.5
    ac = ((ax-cx)**2 + (ay-cy)**2)**0.5
    bc = ((bx-cx)**2 + (by-cy)**2)**0.5
    l = [ab+ac, ab+bc, ac+bc]
    print(2*(max(l) - min(l)))