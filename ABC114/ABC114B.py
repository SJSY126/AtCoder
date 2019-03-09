s = str(input())

slist = []
for i in s:
    slist.append(int(i))

x0 = 753
min = 999

for i in range(len(slist)-2):
    x = int(s[i:i+3])
    sabun = abs(x - x0)
    if min > sabun:
        min = sabun

print(min)
