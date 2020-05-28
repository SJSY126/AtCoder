import math
A, B, H, M = map(int, input().split())

h_angle = 360 / 12 * H + 360 / 12 / 60 * M
m_angle = 360/60*M

dif_angle = (h_angle - m_angle)

c2 = A**2 + B**2-2*A*B*math.cos(dif_angle/180*math.pi)

print(math.sqrt(c2))
