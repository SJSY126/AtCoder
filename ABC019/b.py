s = list(input())
i = 0
ans = [""] * len(s)
count = 1
while i < len(s)-1:
    if s[i] == s[i+1]:
        count += 1
    else:
        ans[i] = s[i] + str(count)
        count = 1
    i += 1
    if i == len(s)-1:
        ans[i] = s[i] + str(count)

print("".join(ans))
