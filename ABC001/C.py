def round(x): return (x*2+1)//2


deg, dis = map(int, input().split())

a = 360 / 16
b = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
     "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "N"]
c = [i for i in range(13)]

deg = deg / 10
dir = b[int((deg + 11.25)//a)]

dis /= 60
dis = round(dis * 10) / 10

if 0 <= dis and dis <= 0.2:
    w = c[0]
    dir = "C"
elif dis <= 1.5:
    w = c[1]
elif dis <= 3.3:
    w = c[2]
elif dis <= 5.4:
    w = c[3]
elif dis <= 7.9:
    w = c[4]
elif dis <= 10.7:
    w = c[5]
elif dis <= 13.8:
    w = c[6]
elif dis <= 17.1:
    w = c[7]
elif dis <= 20.7:
    w = c[8]
elif dis <= 24.4:
    w = c[9]
elif dis <= 28.4:
    w = c[10]
elif dis <= 32.6:
    w = c[11]
elif dis >= 32.7:
    w = c[12]

print(dir, w)
