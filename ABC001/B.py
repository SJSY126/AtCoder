m = int(input())
km = m / 1000

if km < 0.1:
    vv = 00
elif 0.1 <= km and km <= 5:
    vv = 10 * km
elif 6 <= km and km <= 30:
    vv = km + 50
elif 35 <= km and km <= 70:
    vv = (km - 30) / 5 + 80
elif 70 < km:
    vv = 89

vv = str(int(vv))
if len(vv) == 1:
    vv = "0" + vv

print(vv)
