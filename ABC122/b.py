s = list(input())
ans = 0
count = 0
for i in s:
    if i in "AGCT":
        count += 1
        ans = max(ans, count)
    else:
        count = 0

print(ans)
