s = list(input())

count_1 = 0
count_0 = 0

for i in s:
    if i == "1":
        count_1 += 1
    elif i == "0":
        count_0 += 1

ans = min(count_0, count_1) * 2
print(ans)
