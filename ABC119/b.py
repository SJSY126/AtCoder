n = int(input())
otosidamas = [[]*2]*n
BTCtoJPY = 380000.0
sum = 0

for i in range(len(otosidamas)):
    otosidamas[i] = input().split()
    otosidamas[i][0] = float(otosidamas[i][0])
    if otosidamas[i][1] == "BTC":
        sum += BTCtoJPY * otosidamas[i][0]
    else:
        sum += otosidamas[i][0]


print(sum)
