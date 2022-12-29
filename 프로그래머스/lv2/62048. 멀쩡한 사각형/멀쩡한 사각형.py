import math

def solution(w,h):
    w, h = max(w, h), min(w, h)
    g = math.gcd(w, h)

    if g > 1:
        return w*h - (w+h-g)
    else:
        return w*h - (w+h-1)