import math
xa, ya, xb, yb, xc, yc = map(int, input().split())
xb -= xa
xc -= xa
yb -= ya
yc -= ya
xa = 0
ya = 0
teihen = math.sqrt(xb**2 + yb**2)
h = abs(-yb*xc + xb*yc)/math.sqrt(xb**2 + yb**2)
ans = 0.5 * teihen * h
print(ans)
