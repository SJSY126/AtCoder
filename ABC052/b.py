n = int(input())
s = list(input())
ans = 0
x = 0
for i in range(len(s)):
    if s[i] == "I":
        x += 1
        ans = max(x, ans)
    else:
        x -= 1

print(ans)
