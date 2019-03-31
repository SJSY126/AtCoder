def cal_temperture(x):
    return abs((t - x * 0.006) - a)


n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
cal_temp = list(map(cal_temperture, h))

print(cal_temp.index(min(cal_temp))+1)
